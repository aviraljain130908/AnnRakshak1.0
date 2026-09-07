import os
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from fastapi import HTTPException, UploadFile, status

MAX_SIZE_MB = int(os.getenv("MAX_IMAGE_SIZE_MB", "5"))

async def validate_and_preprocess_image(file: UploadFile) -> Image.Image:
    """
    Step-by-step image validation & preprocessing:
    1. Check file extension
    2. Read & check file size
    3. Load into Pillow RGB
    4. Check blurriness with OpenCV Laplacian variance
    5. Resize to 224x224
    """
    # Step 1: Check File Extension
    filename = file.filename.lower() if file.filename else ""
    if not filename.endswith((".jpg", ".jpeg", ".png")):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"success": False, "error": "Unsupported image format. Allowed formats: JPG, JPEG, PNG"}
        )

    # Step 2: Read bytes into memory & Check Size
    contents = await file.read()
    size_mb = len(contents) / (1024 * 1024)
    if size_mb > MAX_SIZE_MB:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"success": False, "error": f"Image size exceeds maximum limit of {MAX_SIZE_MB} MB"}
        )

    # Step 3: Load into Pillow & Ensure RGB Format
    try:
        pil_image = Image.open(BytesIO(contents)).convert("RGB")
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"success": False, "error": "Invalid or corrupted image file."}
        )

    # Step 4: OpenCV Blurriness Check using Variance of Laplacian
    cv_image = np.array(pil_image)
    gray = cv2.cvtColor(cv_image, cv2.COLOR_RGB2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    
    # Blurriness threshold: 20.0 — outdoor crop photos with natural backgrounds
    # tend to score lower; 30.0 was rejecting valid field images
    if laplacian_var < 20.0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "success": False, 
                "error": f"Image is too blurry (Laplacian Variance: {round(laplacian_var, 2)}). Please upload a clearer leaf image."
            }
        )

    # Step 5: Resize Image using Resampling.LANCZOS for quality preservation
    resized_image = pil_image.resize((224, 224), Image.Resampling.LANCZOS)

    # Reset file seek point in case the route needs to save/read the raw file again
    await file.seek(0)

    return resized_image