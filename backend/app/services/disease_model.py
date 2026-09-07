import os
import torch
from transformers import MobileNetV2ImageProcessor, AutoModelForImageClassification
from PIL import Image

# Crops whose predictions should be prioritized when the user specifies that crop
CROP_LABEL_KEYWORDS = {
    "tomato": ["tomato"],
    "potato": ["potato"],
    "corn": ["corn", "maize"],
    "maize": ["corn", "maize"],
    "wheat": ["wheat"],
    "rice": ["rice"],
    "pepper": ["pepper"],
    "apple": ["apple"],
    "grape": ["grape"],
}


def _clean_label(raw_label: str) -> str:
    """Converts raw model label to human-readable form."""
    return raw_label.replace("___", " - ").replace("_", " ").strip()


class DiseaseModelWrapper:
    """Wrapper class loading open-source Hugging Face pretrained plant disease model."""

    def __init__(self):
        self.model = None
        self.processor = None
        self.model_name = os.getenv(
            "MODEL_NAME",
            "linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification"
        )

    def load(self):
        """Loads model into CPU memory once during startup."""
        print(f"Loading AI Model: {self.model_name}...")
        try:
            self.processor = MobileNetV2ImageProcessor.from_pretrained(self.model_name)
            self.model = AutoModelForImageClassification.from_pretrained(self.model_name)
            self.model.eval()
            print("AI Disease Model loaded successfully.")
        except Exception as e:
            print(f"Failed to load Hugging Face model: {e}")
            self.model = None

    def predict(self, image: Image.Image, crop_type: str = "") -> dict:
        """
        Runs image prediction and returns:
        - prediction: top-1 label (crop-filtered if crop_type matches)
        - confidence: top-1 confidence score
        - alternatives: list of top-3 {label, confidence} dicts
        """
        if self.model is None or self.processor is None:
            return {
                "prediction": "Model Unavailable",
                "confidence": 0.0,
                "alternatives": []
            }

        inputs = self.processor(images=image, return_tensors="pt")

        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            probabilities = torch.nn.functional.softmax(logits, dim=-1)[0]

        # Build full ranked list of all predictions
        sorted_indices = torch.argsort(probabilities, descending=True)

        crop_keywords = CROP_LABEL_KEYWORDS.get(crop_type.lower().strip(), [])

        # Top-1 overall prediction
        top1_idx = sorted_indices[0].item()
        top1_label = _clean_label(self.model.config.id2label[top1_idx])
        top1_conf = round(float(probabilities[top1_idx].item()), 3)

        if crop_keywords:
            # Collect ALL classes belonging to this crop type
            crop_preds = []
            for idx in range(len(probabilities)):
                raw_label = self.model.config.id2label[idx].lower()
                if any(kw in raw_label for kw in crop_keywords):
                    crop_preds.append({
                        "label": _clean_label(self.model.config.id2label[idx]),
                        "confidence": float(probabilities[idx].item())
                    })

            if crop_preds:
                total_crop_prob = sum(p["confidence"] for p in crop_preds)
                best_crop = max(crop_preds, key=lambda p: p["confidence"])

                # Renormalize within the crop category if the model noticed the crop at all.
                # within-crop confidence = best_crop_prob / total_crop_prob
                # This solves the problem where the model spreads probability across
                # many crop-specific classes, each appearing low in absolute terms.
                MIN_CROP_PROB = 0.03  # model must assign >= 3% total to this crop
                if total_crop_prob >= MIN_CROP_PROB:
                    within_crop_conf = best_crop["confidence"] / total_crop_prob
                    primary_label = best_crop["label"]
                    primary_conf = round(within_crop_conf, 3)
                else:
                    # Model barely recognized this crop — genuinely uncertain
                    primary_label = best_crop["label"]
                    primary_conf = round(best_crop["confidence"], 3)
            else:
                # No model classes for this crop → fall back to global top-1
                primary_label = top1_label
                primary_conf = top1_conf
        else:
            primary_label = top1_label
            primary_conf = top1_conf

        # Top-3 alternatives from the global ranked list (excluding primary)
        alternatives = []
        seen_labels = {primary_label}
        for idx in sorted_indices:
            if len(alternatives) >= 3:
                break
            label = _clean_label(self.model.config.id2label[idx.item()])
            conf = round(float(probabilities[idx].item()), 3)
            if label not in seen_labels and conf >= 0.02:
                alternatives.append({"label": label, "confidence": conf})
                seen_labels.add(label)

        return {
            "prediction": primary_label,
            "confidence": primary_conf,
            "alternatives": alternatives
        }


# Global singleton instance
disease_model_instance = DiseaseModelWrapper()
