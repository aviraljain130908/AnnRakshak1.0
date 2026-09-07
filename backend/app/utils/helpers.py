"""
Multilingual advisory dictionary for crop disease detection.
Covers all PlantVillage model classes with full 7-language support for
Indian-relevant crops (Tomato, Potato, Maize) and English+Hindi for others.
"""

ADVISORY_DICTIONARY = {

    # ──────────────────────────────────────────────
    # TOMATO DISEASES
    # ──────────────────────────────────────────────

    "tomato_early_blight": {
        "en": {
            "message": "Tomato Early Blight (Alternaria solani) detected on leaves.",
            "basic_advice": "Remove and destroy affected leaves. Avoid overhead watering. Apply copper-based fungicide or Mancozeb every 7–10 days.",
            "treatment": "Spray Mancozeb 75% WP @ 2.5 g/L or Chlorothalonil 75% WP @ 2 g/L. Repeat every 10 days."
        },
        "hi": {
            "message": "टमाटर में अर्ली ब्लाइट (झुलसा रोग) के लक्षण दिखाई दे रहे हैं।",
            "basic_advice": "प्रभावित पत्तियों को हटाकर नष्ट करें। पत्तियों पर सीधे पानी न डालें। मैंकोज़ेब या कॉपर-आधारित फफूंदनाशक का उपयोग करें।",
            "treatment": "मैंकोज़ेब 75% WP @ 2.5 ग्राम/लीटर का छिड़काव करें। 10 दिनों में दोहराएं।"
        },
        "mr": {
            "message": "टोमॅटोवर अर्ली ब्लाइटची लक्षणे आढळली आहेत.",
            "basic_advice": "बाधित पाने काढून जाळा. पानांवर थेट पाणी शिंपडणे टाळा. मॅन्कोझेब किंवा तांबे-आधारित बुरशीनाशक वापरा.",
            "treatment": "मॅन्कोझेब 75% WP @ 2.5 ग्राम/लिटर फवारणी करा. 10 दिवसांनी पुन्हा करा."
        },
        "pa": {
            "message": "ਟਮਾਟਰ 'ਤੇ ਅਰਲੀ ਬਲਾਈਟ ਦੇ ਲੱਛਣ ਦਿਖਾਈ ਦੇ ਰਹੇ ਹਨ।",
            "basic_advice": "ਪ੍ਰਭਾਵਿਤ ਪੱਤਿਆਂ ਨੂੰ ਹਟਾ ਕੇ ਸਾੜੋ। ਪੱਤਿਆਂ 'ਤੇ ਸਿੱਧਾ ਪਾਣੀ ਨਾ ਪਾਓ। ਮੈਂਕੋਜ਼ੇਬ ਜਾਂ ਕਾਪਰ ਉੱਲੀਨਾਸ਼ਕ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।",
            "treatment": "ਮੈਂਕੋਜ਼ੇਬ 75% WP @ 2.5 ਗ੍ਰਾਮ/ਲੀਟਰ ਛਿੜਕਾਅ ਕਰੋ। 10 ਦਿਨਾਂ ਬਾਅਦ ਦੁਹਰਾਓ।"
        },
        "ta": {
            "message": "தக்காளி இலையில் ஆரம்பகால கருகல் நோய் கண்டறியப்பட்டது.",
            "basic_advice": "பாதிக்கப்பட்ட இலைகளை அகற்றி அழிக்கவும். இலைகளில் நேரடியாக நீர் பாய்ச்சுவதை தவிர்க்கவும். மேன்கோசெப் பூஞ்சைக்கொல்லியை பயன்படுத்தவும்.",
            "treatment": "மேன்கோசெப் 75% WP @ 2.5 கிராம்/லிட்டர் தெளிக்கவும். 10 நாட்களுக்கு ஒருமுறை தெளிக்கவும்."
        },
        "te": {
            "message": "టమోటా ఆకులపై ముందస్తు ఆకు మచ్చల వ్యాధి గుర్తించబడింది.",
            "basic_advice": "బాధిత ఆకులను తొలగించి నాశనం చేయండి. ఆకులపై నేరుగా నీరు పడకుండా చూడండి. మాంకోజెబ్ లేదా రాగి-ఆధారిత శిలీంద్రనాశనిని ఉపయోగించండి.",
            "treatment": "మాంకోజెబ్ 75% WP @ 2.5 గ్రా/లీ పిచికారి చేయండి. 10 రోజులకు ఒకసారి చేయండి."
        },
        "bn": {
            "message": "টমেটো পাতায় আর্লি ব্লাইট রোগ শনাক্ত হয়েছে।",
            "basic_advice": "আক্রান্ত পাতাগুলি কেটে নষ্ট করুন। পাতায় সরাসরি জল দেওয়া বন্ধ করুন। ম্যানকোজেব বা কপার ছত্রাকনাশক স্প্রে করুন।",
            "treatment": "ম্যানকোজেব 75% WP @ 2.5 গ্রাম/লিটার স্প্রে করুন। ১০ দিন পর পুনরাবৃত্তি করুন।"
        }
    },

    "tomato_late_blight": {
        "en": {
            "message": "Tomato Late Blight (Phytophthora infestans) detected — this is a serious fast-spreading disease.",
            "basic_advice": "Act immediately. Remove all affected plant parts. Avoid wet foliage. Apply Metalaxyl+Mancozeb or Cymoxanil-based fungicide.",
            "treatment": "Spray Metalaxyl 8% + Mancozeb 64% WP @ 2.5 g/L or Cymoxanil 8% + Mancozeb 64% WP @ 3 g/L. Repeat every 7 days."
        },
        "hi": {
            "message": "टमाटर में लेट ब्लाइट (पछेती झुलसा) पाया गया — यह एक गंभीर और तेजी से फैलने वाली बीमारी है।",
            "basic_advice": "तत्काल कार्रवाई करें। प्रभावित पत्तियां और फल हटाएं। मेटालैक्सिल + मैंकोज़ेब का छिड़काव करें।",
            "treatment": "मेटालैक्सिल 8% + मैंकोज़ेब 64% WP @ 2.5 ग्राम/लीटर का छिड़काव करें। 7 दिनों में दोहराएं।"
        },
        "mr": {
            "message": "टोमॅटोवर लेट ब्लाइट आढळला — हा एक गंभीर वेगाने पसरणारा रोग आहे.",
            "basic_advice": "ताबडतोब उपाय करा. बाधित फांद्या आणि पाने काढून टाका. मेटालॅक्सिल + मॅन्कोझेब फवारणी करा.",
            "treatment": "मेटालॅक्सिल 8% + मॅन्कोझेब 64% WP @ 2.5 ग्राम/लिटर फवारणी करा. 7 दिवसांनी पुन्हा करा."
        },
        "pa": {
            "message": "ਟਮਾਟਰ 'ਤੇ ਲੇਟ ਬਲਾਈਟ ਮਿਲੀ ਹੈ — ਇਹ ਇੱਕ ਗੰਭੀਰ ਅਤੇ ਤੇਜ਼ੀ ਨਾਲ ਫੈਲਣ ਵਾਲੀ ਬਿਮਾਰੀ ਹੈ।",
            "basic_advice": "ਤੁਰੰਤ ਕਾਰਵਾਈ ਕਰੋ। ਪ੍ਰਭਾਵਿਤ ਹਿੱਸੇ ਹਟਾਓ। ਮੈਟਾਲੈਕਸਿਲ + ਮੈਂਕੋਜ਼ੇਬ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।",
            "treatment": "ਮੈਟਾਲੈਕਸਿਲ 8% + ਮੈਂਕੋਜ਼ੇਬ 64% WP @ 2.5 ਗ੍ਰਾਮ/ਲੀਟਰ ਛਿੜਕਾਅ ਕਰੋ। 7 ਦਿਨਾਂ ਬਾਅਦ ਦੁਹਰਾਓ।"
        },
        "ta": {
            "message": "தக்காளியில் லேட் ப்ளைட் நோய் கண்டறியப்பட்டது — இது மிக விரைவாக பரவக்கூடிய தீவிர நோய்.",
            "basic_advice": "உடனடியாக நடவடிக்கை எடுக்கவும். பாதிக்கப்பட்ட பகுதிகளை அகற்றவும். மெட்டாலாக்சில் + மேன்கோசெப் தெளிக்கவும்.",
            "treatment": "மெட்டாலாக்சில் 8% + மேன்கோசெப் 64% WP @ 2.5 கிராம்/லிட்டர் தெளிக்கவும். 7 நாட்களுக்கு ஒருமுறை செய்யவும்."
        },
        "te": {
            "message": "టమోటాలో లేట్ బ్లైట్ వ్యాధి గుర్తించబడింది — ఇది వేగంగా వ్యాపించే తీవ్రమైన వ్యాధి.",
            "basic_advice": "వెంటనే చర్య తీసుకోండి. బాధిత భాగాలను తొలగించండి. మెటలాక్సిల్ + మాంకోజెబ్ పిచికారి చేయండి.",
            "treatment": "మెటలాక్సిల్ 8% + మాంకోజెబ్ 64% WP @ 2.5 గ్రా/లీ పిచికారి చేయండి. 7 రోజులకు ఒకసారి."
        },
        "bn": {
            "message": "টমেটোতে লেট ব্লাইট রোগ শনাক্ত হয়েছে — এটি দ্রুত ছড়িয়ে পড়া একটি গুরুতর রোগ।",
            "basic_advice": "অবিলম্বে ব্যবস্থা নিন। আক্রান্ত অংশ সরিয়ে ফেলুন। মেটালাক্সিল + ম্যানকোজেব স্প্রে করুন।",
            "treatment": "মেটালাক্সিল 8% + ম্যানকোজেব 64% WP @ 2.5 গ্রাম/লিটার স্প্রে করুন। ৭ দিন পর পুনরাবৃত্তি করুন।"
        }
    },

    "tomato_bacterial_spot": {
        "en": {
            "message": "Tomato Bacterial Spot (Xanthomonas campestris) detected on leaves and/or fruit.",
            "basic_advice": "Remove infected plant material. Avoid working with wet plants. Apply copper-based bactericide. Ensure good air circulation.",
            "treatment": "Spray Copper Oxychloride 50% WP @ 3 g/L. Avoid applying during hot afternoon. Repeat every 10 days."
        },
        "hi": {
            "message": "टमाटर में बैक्टीरियल स्पॉट (जीवाणु चित्ती) के लक्षण पाए गए हैं।",
            "basic_advice": "संक्रमित पौधे के हिस्सों को हटाएं। गीले पौधों को न छुएं। कॉपर ऑक्सीक्लोराइड का छिड़काव करें।",
            "treatment": "कॉपर ऑक्सीक्लोराइड 50% WP @ 3 ग्राम/लीटर का छिड़काव करें। 10 दिनों में दोहराएं।"
        },
        "mr": {
            "message": "टोमॅटोवर बॅक्टेरियल स्पॉटची लक्षणे आढळली.",
            "basic_advice": "संसर्गित भाग काढा. ओल्या झाडांना स्पर्श करू नका. कॉपर ऑक्सीक्लोराइड फवारणी करा.",
            "treatment": "कॉपर ऑक्सीक्लोराइड 50% WP @ 3 ग्राम/लिटर फवारणी करा. 10 दिवसांनी पुन्हा करा."
        },
        "pa": {
            "message": "ਟਮਾਟਰ 'ਤੇ ਬੈਕਟੀਰੀਅਲ ਸਪਾਟ ਦੇ ਲੱਛਣ ਮਿਲੇ ਹਨ।",
            "basic_advice": "ਸੰਕ੍ਰਮਿਤ ਪੌਦੇ ਦੇ ਹਿੱਸਿਆਂ ਨੂੰ ਹਟਾਓ। ਕਾਪਰ ਆਕਸੀਕਲੋਰਾਈਡ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।",
            "treatment": "ਕਾਪਰ ਆਕਸੀਕਲੋਰਾਈਡ 50% WP @ 3 ਗ੍ਰਾਮ/ਲੀਟਰ ਛਿੜਕਾਅ ਕਰੋ। 10 ਦਿਨਾਂ ਬਾਅਦ ਦੁਹਰਾਓ।"
        },
        "ta": {
            "message": "தக்காளி இலையில் பாக்டீரியல் ஸ்பாட் நோய் கண்டறியப்பட்டது.",
            "basic_advice": "பாதிக்கப்பட்ட பகுதிகளை அகற்றவும். செம்பு ஆக்சிகுளோரைடு தெளிக்கவும்.",
            "treatment": "செம்பு ஆக்சிகுளோரைடு 50% WP @ 3 கிராம்/லிட்டர் தெளிக்கவும். 10 நாட்களுக்கு ஒருமுறை."
        },
        "te": {
            "message": "టమోటా ఆకులపై బ్యాక్టీరియల్ స్పాట్ వ్యాధి గుర్తించబడింది.",
            "basic_advice": "సోకిన భాగాలను తొలగించండి. కాపర్ ఆక్సీక్లోరైడ్ పిచికారి చేయండి.",
            "treatment": "కాపర్ ఆక్సీక్లోరైడ్ 50% WP @ 3 గ్రా/లీ పిచికారి చేయండి. 10 రోజులకు ఒకసారి."
        },
        "bn": {
            "message": "টমেটো পাতায় ব্যাকটেরিয়াল স্পট রোগ শনাক্ত হয়েছে।",
            "basic_advice": "আক্রান্ত অংশগুলি সরিয়ে ফেলুন। কপার অক্সিক্লোরাইড স্প্রে করুন।",
            "treatment": "কপার অক্সিক্লোরাইড 50% WP @ 3 গ্রাম/লিটার স্প্রে করুন। ১০ দিন পর পুনরাবৃত্তি।"
        }
    },

    "tomato_leaf_mold": {
        "en": {
            "message": "Tomato Leaf Mold (Passalora fulva) detected — common in humid greenhouse conditions.",
            "basic_advice": "Improve ventilation. Reduce leaf wetness. Remove affected leaves. Apply Chlorothalonil or Mancozeb fungicide.",
            "treatment": "Spray Chlorothalonil 75% WP @ 2 g/L. Ensure good airflow between plants. Repeat every 7–10 days in high humidity."
        },
        "hi": {
            "message": "टमाटर में लीफ मोल्ड (पत्ती फफूंद) के लक्षण पाए गए हैं।",
            "basic_advice": "हवा का संचार सुधारें। पत्तियों की नमी कम करें। क्लोरोथैलोनिल का छिड़काव करें।",
            "treatment": "क्लोरोथैलोनिल 75% WP @ 2 ग्राम/लीटर छिड़काव करें। 7-10 दिनों में दोहराएं।"
        },
        "mr": {
            "message": "टोमॅटोवर लीफ मोल्ड आढळले — दमट वातावरणात हे जास्त होते.",
            "basic_advice": "हवेचे परिसंचरण सुधारा. पाने ओली राहू देऊ नका. क्लोरोथॅलोनिल फवारणी करा.",
            "treatment": "क्लोरोथॅलोनिल 75% WP @ 2 ग्राम/लिटर फवारणी करा. 7-10 दिवसांनी पुन्हा करा."
        },
        "pa": {
            "message": "ਟਮਾਟਰ 'ਤੇ ਲੀਫ ਮੋਲਡ ਮਿਲਿਆ ਹੈ।",
            "basic_advice": "ਹਵਾ ਦੇ ਸੰਚਾਰ ਵਿੱਚ ਸੁਧਾਰ ਕਰੋ। ਕਲੋਰੋਥੈਲੋਨਿਲ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।",
            "treatment": "ਕਲੋਰੋਥੈਲੋਨਿਲ 75% WP @ 2 ਗ੍ਰਾਮ/ਲੀਟਰ ਛਿੜਕਾਅ ਕਰੋ। 7-10 ਦਿਨਾਂ ਬਾਅਦ ਦੁਹਰਾਓ।"
        },
        "ta": {
            "message": "தக்காளியில் இலை அச்சு நோய் கண்டறியப்பட்டது.",
            "basic_advice": "காற்றோட்டம் மேம்படுத்தவும். குளோரோதலோனில் தெளிக்கவும்.",
            "treatment": "குளோரோதலோனில் 75% WP @ 2 கிராம்/லிட்டர் தெளிக்கவும். 7-10 நாட்களுக்கு ஒருமுறை."
        },
        "te": {
            "message": "టమోటాలో ఆకు అచ్చు వ్యాధి గుర్తించబడింది.",
            "basic_advice": "గాలి చలనం మెరుగుపరచండి. క్లోరోథలోనిల్ పిచికారి చేయండి.",
            "treatment": "క్లోరోథలోనిల్ 75% WP @ 2 గ్రా/లీ పిచికారి చేయండి. 7-10 రోజులకు ఒకసారి."
        },
        "bn": {
            "message": "টমেটো পাতায় লিফ মোল্ড রোগ শনাক্ত হয়েছে।",
            "basic_advice": "বায়ু চলাচল উন্নত করুন। ক্লোরোথ্যালোনিল স্প্রে করুন।",
            "treatment": "ক্লোরোথ্যালোনিল 75% WP @ 2 গ্রাম/লিটার স্প্রে করুন। ৭-১০ দিন পর পুনরাবৃত্তি।"
        }
    },

    "tomato_septoria_leaf_spot": {
        "en": {
            "message": "Tomato Septoria Leaf Spot (Septoria lycopersici) detected — causes premature defoliation.",
            "basic_advice": "Remove lower infected leaves. Stake plants for better airflow. Apply Mancozeb or Azoxystrobin fungicide. Avoid wetting foliage.",
            "treatment": "Spray Azoxystrobin 23% SC @ 1 mL/L or Mancozeb 75% WP @ 2.5 g/L. Repeat every 7–10 days."
        },
        "hi": {
            "message": "टमाटर में सेप्टोरिया लीफ स्पॉट के लक्षण पाए गए हैं।",
            "basic_advice": "नीचे की प्रभावित पत्तियां हटाएं। एजोक्सीस्ट्रोबिन या मैंकोज़ेब का छिड़काव करें।",
            "treatment": "एजोक्सीस्ट्रोबिन 23% SC @ 1 mL/लीटर छिड़काव करें। 7-10 दिनों में दोहराएं।"
        },
        "mr": {
            "message": "टोमॅटोवर सेप्टोरिया लीफ स्पॉट आढळला.",
            "basic_advice": "खालची बाधित पाने काढा. अझोक्सीस्ट्रोबिन किंवा मॅन्कोझेब फवारणी करा.",
            "treatment": "अझोक्सीस्ट्रोबिन 23% SC @ 1 mL/लिटर फवारणी करा. 7-10 दिवसांनी पुन्हा करा."
        },
        "pa": {
            "message": "ਟਮਾਟਰ 'ਤੇ ਸੈਪਟੋਰੀਆ ਲੀਫ ਸਪਾਟ ਮਿਲਿਆ ਹੈ।",
            "basic_advice": "ਹੇਠਲੇ ਪ੍ਰਭਾਵਿਤ ਪੱਤੇ ਹਟਾਓ। ਅਜ਼ੋਕਸੀਸਟ੍ਰੋਬਿਨ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।",
            "treatment": "ਅਜ਼ੋਕਸੀਸਟ੍ਰੋਬਿਨ 23% SC @ 1 mL/ਲੀਟਰ ਛਿੜਕਾਅ ਕਰੋ। 7-10 ਦਿਨਾਂ ਬਾਅਦ ਦੁਹਰਾਓ।"
        },
        "ta": {
            "message": "தக்காளியில் செப்டோரியா இலை புள்ளி நோய் கண்டறியப்பட்டது.",
            "basic_advice": "கீழ் இலைகளை அகற்றவும். அசோக்ஸிஸ்ட்ரோபின் தெளிக்கவும்.",
            "treatment": "அசோக்ஸிஸ்ட்ரோபின் 23% SC @ 1 mL/லிட்டர் தெளிக்கவும். 7-10 நாட்களுக்கு ஒருமுறை."
        },
        "te": {
            "message": "టమోటాలో సెప్టోరియా ఆకు మచ్చ వ్యాధి గుర్తించబడింది.",
            "basic_advice": "దిగువ ఆకులను తొలగించండి. అజోక్సీస్ట్రోబిన్ పిచికారి చేయండి.",
            "treatment": "అజోక్సీస్ట్రోబిన్ 23% SC @ 1 mL/లీ పిచికారి చేయండి. 7-10 రోజులకు ఒకసారి."
        },
        "bn": {
            "message": "টমেটো পাতায় সেপ্টোরিয়া লিফ স্পট রোগ শনাক্ত হয়েছে।",
            "basic_advice": "নিচের আক্রান্ত পাতাগুলি সরিয়ে ফেলুন। অ্যাজোক্সিস্ট্রোবিন স্প্রে করুন।",
            "treatment": "অ্যাজোক্সিস্ট্রোবিন 23% SC @ 1 mL/লিটার স্প্রে করুন। ৭-১০ দিন পর পুনরাবৃত্তি।"
        }
    },

    "tomato_spider_mites": {
        "en": {
            "message": "Spider Mite infestation (Two-spotted Spider Mite) detected on tomato leaves.",
            "basic_advice": "Spray the undersides of leaves with water to dislodge mites. Apply acaricide (miticide). Avoid dusty conditions. Introduce predatory mites if available.",
            "treatment": "Spray Abamectin 1.8% EC @ 0.5 mL/L or Spiromesifen 22.9% SC @ 0.75 mL/L. Target leaf undersides. Repeat after 7 days."
        },
        "hi": {
            "message": "टमाटर की पत्तियों पर स्पाइडर माइट (मकड़ी घुन) का प्रकोप पाया गया।",
            "basic_advice": "पत्तियों के नीचे पानी का छिड़काव करें। अबामेक्टिन या स्पाइरोमेसिफेन कीटनाशक का उपयोग करें।",
            "treatment": "अबामेक्टिन 1.8% EC @ 0.5 mL/लीटर छिड़काव करें। पत्तियों के नीचे लगाएं। 7 दिनों में दोहराएं।"
        },
        "mr": {
            "message": "टोमॅटोवर स्पायडर माइट (कोळी माइट) आढळले.",
            "basic_advice": "पानांच्या खाली पाणी फवारा. अबामेक्टिन किटकनाशक वापरा.",
            "treatment": "अबामेक्टिन 1.8% EC @ 0.5 mL/लिटर फवारणी करा. पानांच्या खाली लक्ष द्या. 7 दिवसांनी पुन्हा करा."
        },
        "pa": {
            "message": "ਟਮਾਟਰ 'ਤੇ ਸਪਾਈਡਰ ਮਾਈਟ ਦਾ ਪ੍ਰਕੋਪ ਮਿਲਿਆ ਹੈ।",
            "basic_advice": "ਪੱਤਿਆਂ ਦੇ ਹੇਠਾਂ ਪਾਣੀ ਛਿੜਕੋ। ਅਬਾਮੈਕਟਿਨ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।",
            "treatment": "ਅਬਾਮੈਕਟਿਨ 1.8% EC @ 0.5 mL/ਲੀਟਰ ਛਿੜਕਾਅ ਕਰੋ। 7 ਦਿਨਾਂ ਬਾਅਦ ਦੁਹਰਾਓ।"
        },
        "ta": {
            "message": "தக்காளி இலையில் சிலந்தி பூச்சி தாக்குதல் கண்டறியப்பட்டது.",
            "basic_advice": "இலைகளின் கீழ் பகுதியில் நீர் தெளிக்கவும். அபாமெக்டின் தெளிக்கவும்.",
            "treatment": "அபாமெக்டின் 1.8% EC @ 0.5 mL/லிட்டர் தெளிக்கவும். 7 நாட்களுக்கு ஒருமுறை."
        },
        "te": {
            "message": "టమోటా ఆకులపై సాలీడు పురుగుల ఉద్ధృతి గుర్తించబడింది.",
            "basic_advice": "ఆకుల అడుగు భాగంలో నీరు పిచికారి చేయండి. అబామెక్టిన్ పిచికారి చేయండి.",
            "treatment": "అబామెక్టిన్ 1.8% EC @ 0.5 mL/లీ పిచికారి చేయండి. 7 రోజులకు ఒకసారి."
        },
        "bn": {
            "message": "টমেটো পাতায় স্পাইডার মাইট আক্রমণ শনাক্ত হয়েছে।",
            "basic_advice": "পাতার নিচে জল স্প্রে করুন। অ্যাবামেকটিন স্প্রে করুন।",
            "treatment": "অ্যাবামেকটিন 1.8% EC @ 0.5 mL/লিটার স্প্রে করুন। ৭ দিন পর পুনরাবৃত্তি।"
        }
    },

    "tomato_target_spot": {
        "en": {
            "message": "Tomato Target Spot (Corynespora cassiicola) detected — characterized by concentric ring lesions.",
            "basic_advice": "Remove affected leaves and debris. Apply Azoxystrobin or Chlorothalonil fungicide. Improve plant spacing for airflow.",
            "treatment": "Spray Azoxystrobin 23% SC @ 1 mL/L. Repeat every 10 days until symptoms are controlled."
        },
        "hi": {
            "message": "टमाटर में टार्गेट स्पॉट रोग के लक्षण मिले हैं।",
            "basic_advice": "प्रभावित पत्तियां और अवशेष हटाएं। एजोक्सीस्ट्रोबिन का छिड़काव करें।",
            "treatment": "एजोक्सीस्ट्रोबिन 23% SC @ 1 mL/लीटर छिड़काव करें। 10 दिनों में दोहराएं।"
        },
        "mr": {
            "message": "टोमॅटोवर टार्गेट स्पॉट आढळला.",
            "basic_advice": "बाधित पाने आणि अवशेष काढा. अझोक्सीस्ट्रोबिन फवारणी करा.",
            "treatment": "अझोक्सीस्ट्रोबिन 23% SC @ 1 mL/लिटर फवारणी करा. 10 दिवसांनी पुन्हा करा."
        },
        "pa": {
            "message": "ਟਮਾਟਰ 'ਤੇ ਟਾਰਗੇਟ ਸਪਾਟ ਮਿਲਿਆ ਹੈ।",
            "basic_advice": "ਪ੍ਰਭਾਵਿਤ ਪੱਤੇ ਹਟਾਓ। ਅਜ਼ੋਕਸੀਸਟ੍ਰੋਬਿਨ ਛਿੜਕਾਅ ਕਰੋ।",
            "treatment": "ਅਜ਼ੋਕਸੀਸਟ੍ਰੋਬਿਨ 23% SC @ 1 mL/ਲੀਟਰ ਛਿੜਕਾਅ ਕਰੋ। 10 ਦਿਨਾਂ ਬਾਅਦ ਦੁਹਰਾਓ।"
        },
        "ta": {
            "message": "தக்காளியில் டார்கெட் ஸ்பாட் நோய் கண்டறியப்பட்டது.",
            "basic_advice": "பாதிக்கப்பட்ட இலைகளை அகற்றவும். அசோக்ஸிஸ்ட்ரோபின் தெளிக்கவும்.",
            "treatment": "அசோக்ஸிஸ்ட்ரோபின் 23% SC @ 1 mL/லிட்டர் தெளிக்கவும். 10 நாட்களுக்கு ஒருமுறை."
        },
        "te": {
            "message": "టమోటాలో టార్గెట్ స్పాట్ వ్యాధి గుర్తించబడింది.",
            "basic_advice": "బాధిత ఆకులను తొలగించండి. అజోక్సీస్ట్రోబిన్ పిచికారి చేయండి.",
            "treatment": "అజోక్సీస్ట్రోబిన్ 23% SC @ 1 mL/లీ పిచికారి చేయండి. 10 రోజులకు ఒకసారి."
        },
        "bn": {
            "message": "টমেটোতে টার্গেট স্পট রোগ শনাক্ত হয়েছে।",
            "basic_advice": "আক্রান্ত পাতাগুলি সরিয়ে ফেলুন। অ্যাজোক্সিস্ট্রোবিন স্প্রে করুন।",
            "treatment": "অ্যাজোক্সিস্ট্রোবিন 23% SC @ 1 mL/লিটার স্প্রে করুন। ১০ দিন পর পুনরাবৃত্তি।"
        }
    },

    "tomato_yellow_leaf_curl_virus": {
        "en": {
            "message": "Tomato Yellow Leaf Curl Virus (TYLCV) detected — spread by whiteflies. Leaves curl upward and turn yellow.",
            "basic_advice": "Remove and destroy infected plants immediately to prevent spread. Control whitefly population with insecticides. Use reflective mulches to repel whiteflies.",
            "treatment": "Spray Imidacloprid 17.8% SL @ 0.5 mL/L or Thiamethoxam 25% WG @ 0.3 g/L to control whitefly vectors. No cure for infected plants — remove them."
        },
        "hi": {
            "message": "टमाटर में TYLCV वायरस (पीली पत्ती मोड़ रोग) पाया गया — यह सफेद मक्खी से फैलता है।",
            "basic_advice": "संक्रमित पौधों को तुरंत नष्ट करें। इमिडाक्लोप्रिड से सफेद मक्खी नियंत्रित करें।",
            "treatment": "इमिडाक्लोप्रिड 17.8% SL @ 0.5 mL/लीटर छिड़काव करें। संक्रमित पौधों को उखाड़ कर नष्ट करें।"
        },
        "mr": {
            "message": "टोमॅटोवर TYLCV विषाणू (पिवळी पानमोड रोग) आढळला — हा पांढऱ्या माशीमुळे पसरतो.",
            "basic_advice": "संक्रमित झाडे लगेच काढा. इमिडाक्लोप्रिडने पांढरी माशी नियंत्रित करा.",
            "treatment": "इमिडाक्लोप्रिड 17.8% SL @ 0.5 mL/लिटर फवारणी करा. संक्रमित झाडे उपटून नष्ट करा."
        },
        "pa": {
            "message": "ਟਮਾਟਰ 'ਤੇ TYLCV ਵਾਇਰਸ ਮਿਲਿਆ — ਇਹ ਚਿੱਟੀ ਮੱਖੀ ਤੋਂ ਫੈਲਦਾ ਹੈ।",
            "basic_advice": "ਸੰਕ੍ਰਮਿਤ ਪੌਦਿਆਂ ਨੂੰ ਤੁਰੰਤ ਨਸ਼ਟ ਕਰੋ। ਇਮਿਡਾਕਲੋਪ੍ਰਿਡ ਨਾਲ ਚਿੱਟੀ ਮੱਖੀ ਕੰਟਰੋਲ ਕਰੋ।",
            "treatment": "ਇਮਿਡਾਕਲੋਪ੍ਰਿਡ 17.8% SL @ 0.5 mL/ਲੀਟਰ ਛਿੜਕਾਅ ਕਰੋ। ਸੰਕ੍ਰਮਿਤ ਪੌਦੇ ਪੁੱਟ ਕੇ ਸਾੜੋ।"
        },
        "ta": {
            "message": "தக்காளியில் TYLCV வைரஸ் (மஞ்சள் இலை சுருள் வைரஸ்) கண்டறியப்பட்டது — வெள்ளை ஈ மூலம் பரவுகிறது.",
            "basic_advice": "பாதிக்கப்பட்ட செடிகளை உடனடியாக அகற்றவும். இமிடாக்ளோப்ரிடால் வெள்ளை ஈவை கட்டுப்படுத்தவும்.",
            "treatment": "இமிடாக்ளோப்ரிட் 17.8% SL @ 0.5 mL/லிட்டர் தெளிக்கவும். பாதிக்கப்பட்ட செடிகளை அழிக்கவும்."
        },
        "te": {
            "message": "టమోటాలో TYLCV వైరస్ గుర్తించబడింది — తెల్ల ఈగల ద్వారా వ్యాపిస్తుంది.",
            "basic_advice": "సోకిన మొక్కలను వెంటనే తొలగించండి. ఇమిడాక్లోప్రిడ్ తో తెల్ల ఈగలను నియంత్రించండి.",
            "treatment": "ఇమిడాక్లోప్రిడ్ 17.8% SL @ 0.5 mL/లీ పిచికారి చేయండి. సోకిన మొక్కలను తీసివేయండి."
        },
        "bn": {
            "message": "টমেটোতে TYLCV ভাইরাস শনাক্ত হয়েছে — সাদা মাছির মাধ্যমে ছড়ায়।",
            "basic_advice": "আক্রান্ত গাছগুলি অবিলম্বে নষ্ট করুন। ইমিডাক্লোপ্রিড দিয়ে সাদা মাছি নিয়ন্ত্রণ করুন।",
            "treatment": "ইমিডাক্লোপ্রিড 17.8% SL @ 0.5 mL/লিটার স্প্রে করুন। আক্রান্ত গাছ উপড়ে ফেলুন।"
        }
    },

    "tomato_mosaic_virus": {
        "en": {
            "message": "Tomato Mosaic Virus (ToMV) detected — mosaic-like yellowing and distortion of leaves.",
            "basic_advice": "No chemical cure. Remove and destroy infected plants. Disinfect tools with bleach solution. Control aphid populations. Use virus-resistant varieties for replanting.",
            "treatment": "Spray Imidacloprid 17.8% SL @ 0.5 mL/L to control aphid vectors. Wash hands and tools with soap before handling healthy plants."
        },
        "hi": {
            "message": "टमाटर में मोज़ेक वायरस के लक्षण पाए गए हैं।",
            "basic_advice": "कोई रासायनिक उपाय नहीं। संक्रमित पौधों को नष्ट करें। माहू नियंत्रण के लिए इमिडाक्लोप्रिड छिड़कें।",
            "treatment": "इमिडाक्लोप्रिड 17.8% SL @ 0.5 mL/लीटर छिड़काव करें। औजारों को ब्लीच से साफ करें।"
        },
        "mr": {
            "message": "टोमॅटोवर मोज़ेक विषाणू आढळला.",
            "basic_advice": "रासायनिक उपाय नाही. संक्रमित झाडे नष्ट करा. मावा नियंत्रणासाठी इमिडाक्लोप्रिड वापरा.",
            "treatment": "इमिडाक्लोप्रिड 17.8% SL @ 0.5 mL/लिटर फवारणी करा. साधने ब्लीचने स्वच्छ करा."
        },
        "pa": {
            "message": "ਟਮਾਟਰ 'ਤੇ ਮੋਜ਼ੇਕ ਵਾਇਰਸ ਮਿਲਿਆ ਹੈ।",
            "basic_advice": "ਕੋਈ ਰਸਾਇਣਕ ਇਲਾਜ ਨਹੀਂ। ਸੰਕ੍ਰਮਿਤ ਪੌਦੇ ਨਸ਼ਟ ਕਰੋ। ਇਮਿਡਾਕਲੋਪ੍ਰਿਡ ਛਿੜਕਾਅ ਕਰੋ।",
            "treatment": "ਇਮਿਡਾਕਲੋਪ੍ਰਿਡ 17.8% SL @ 0.5 mL/ਲੀਟਰ ਛਿੜਕਾਅ ਕਰੋ। ਔਜ਼ਾਰ ਬਲੀਚ ਨਾਲ ਸਾਫ਼ ਕਰੋ।"
        },
        "ta": {
            "message": "தக்காளியில் மொசைக் வைரஸ் கண்டறியப்பட்டது.",
            "basic_advice": "இரசாயன சிகிச்சை இல்லை. பாதிக்கப்பட்ட செடிகளை அழிக்கவும். இமிடாக்ளோப்ரிட் தெளிக்கவும்.",
            "treatment": "இமிடாக்ளோப்ரிட் 17.8% SL @ 0.5 mL/லிட்டர் தெளிக்கவும். கருவிகளை ப்ளீச்சால் சுத்தம் செய்யவும்."
        },
        "te": {
            "message": "టమోటాలో మొజాయిక్ వైరస్ గుర్తించబడింది.",
            "basic_advice": "రసాయన నివారణ లేదు. సోకిన మొక్కలను తొలగించండి. ఇమిడాక్లోప్రిడ్ పిచికారి చేయండి.",
            "treatment": "ఇమిడాక్లోప్రిడ్ 17.8% SL @ 0.5 mL/లీ పిచికారి చేయండి. పనిముట్లను బ్లీచ్ తో శుభ్రపరచండి."
        },
        "bn": {
            "message": "টমেটোতে মোজাইক ভাইরাস শনাক্ত হয়েছে।",
            "basic_advice": "কোনো রাসায়নিক প্রতিকার নেই। আক্রান্ত গাছ নষ্ট করুন। ইমিডাক্লোপ্রিড স্প্রে করুন।",
            "treatment": "ইমিডাক্লোপ্রিড 17.8% SL @ 0.5 mL/লিটার স্প্রে করুন। সরঞ্জাম ব্লিচ দিয়ে পরিষ্কার করুন।"
        }
    },

    "tomato_healthy": {
        "en": {
            "message": "Tomato plant appears healthy with no signs of disease.",
            "basic_advice": "Continue current watering, fertilization, and pest monitoring. Apply preventive fungicide spray during humid seasons.",
            "treatment": None
        },
        "hi": {
            "message": "टमाटर का पौधा स्वस्थ दिखाई दे रहा है।",
            "basic_advice": "वर्तमान सिंचाई और खाद प्रबंधन जारी रखें। आर्द्र मौसम में निवारक फफूंदनाशक का उपयोग करें।",
            "treatment": None
        },
        "mr": {
            "message": "टोमॅटोचे झाड निरोगी दिसत आहे.",
            "basic_advice": "नियमित पाणी आणि खत व्यवस्थापन सुरू ठेवा. दमट हवामानात प्रतिबंधात्मक बुरशीनाशक फवारणी करा.",
            "treatment": None
        },
        "pa": {
            "message": "ਟਮਾਟਰ ਦਾ ਪੌਦਾ ਸਿਹਤਮੰਦ ਦਿਖਾਈ ਦੇ ਰਿਹਾ ਹੈ।",
            "basic_advice": "ਮੌਜੂਦਾ ਸਿੰਚਾਈ ਅਤੇ ਖਾਦ ਪ੍ਰਬੰਧਨ ਜਾਰੀ ਰੱਖੋ।",
            "treatment": None
        },
        "ta": {
            "message": "தக்காளி செடி ஆரோக்கியமாக காணப்படுகிறது.",
            "basic_advice": "தற்போதைய நீர் மற்றும் உர நிர்வாகத்தை தொடரவும்.",
            "treatment": None
        },
        "te": {
            "message": "టమోటా మొక్క ఆరోగ్యంగా కనిపిస్తోంది.",
            "basic_advice": "ప్రస్తుత నీటిపారుదల మరియు ఎరువు నిర్వహణను కొనసాగించండి.",
            "treatment": None
        },
        "bn": {
            "message": "টমেটো গাছটি সুস্থ দেখাচ্ছে।",
            "basic_advice": "বর্তমান সেচ ও সার ব্যবস্থাপনা অব্যাহত রাখুন।",
            "treatment": None
        }
    },

    # ──────────────────────────────────────────────
    # POTATO DISEASES
    # ──────────────────────────────────────────────

    "potato_early_blight": {
        "en": {
            "message": "Potato Early Blight (Alternaria solani) detected on leaves.",
            "basic_advice": "Remove and destroy lower infected leaves. Apply Mancozeb or Chlorothalonil fungicide. Avoid overhead watering. Ensure good soil drainage.",
            "treatment": "Spray Mancozeb 75% WP @ 2.5 g/L. Repeat every 7–10 days starting at first symptom appearance."
        },
        "hi": {
            "message": "आलू में अर्ली ब्लाइट (अगेती झुलसा) के लक्षण पाए गए हैं।",
            "basic_advice": "निचली प्रभावित पत्तियां हटाएं। मैंकोज़ेब या क्लोरोथैलोनिल का छिड़काव करें।",
            "treatment": "मैंकोज़ेब 75% WP @ 2.5 ग्राम/लीटर छिड़काव करें। 7-10 दिनों में दोहराएं।"
        },
        "mr": {
            "message": "बटाट्यावर अर्ली ब्लाइट आढळला.",
            "basic_advice": "खालची बाधित पाने काढा. मॅन्कोझेब किंवा क्लोरोथॅलोनिल फवारणी करा.",
            "treatment": "मॅन्कोझेब 75% WP @ 2.5 ग्राम/लिटर फवारणी करा. 7-10 दिवसांनी पुन्हा करा."
        },
        "pa": {
            "message": "ਆਲੂ 'ਤੇ ਅਰਲੀ ਬਲਾਈਟ ਦੇ ਲੱਛਣ ਮਿਲੇ ਹਨ।",
            "basic_advice": "ਹੇਠਲੀਆਂ ਪ੍ਰਭਾਵਿਤ ਪੱਤੀਆਂ ਹਟਾਓ। ਮੈਂਕੋਜ਼ੇਬ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।",
            "treatment": "ਮੈਂਕੋਜ਼ੇਬ 75% WP @ 2.5 ਗ੍ਰਾਮ/ਲੀਟਰ ਛਿੜਕਾਅ ਕਰੋ। 7-10 ਦਿਨਾਂ ਬਾਅਦ ਦੁਹਰਾਓ।"
        },
        "ta": {
            "message": "உருளைக்கிழங்கு இலையில் ஆரம்பகால கருகல் நோய் கண்டறியப்பட்டது.",
            "basic_advice": "கீழ் இலைகளை அகற்றவும். மேன்கோசெப் தெளிக்கவும்.",
            "treatment": "மேன்கோசெப் 75% WP @ 2.5 கிராம்/லிட்டர் தெளிக்கவும். 7-10 நாட்களுக்கு ஒருமுறை."
        },
        "te": {
            "message": "బంగాళాదుంప ఆకులపై ముందస్తు ఆకు మచ్చ వ్యాధి గుర్తించబడింది.",
            "basic_advice": "దిగువ ఆకులను తొలగించండి. మాంకోజెబ్ పిచికారి చేయండి.",
            "treatment": "మాంకోజెబ్ 75% WP @ 2.5 గ్రా/లీ పిచికారి చేయండి. 7-10 రోజులకు ఒకసారి."
        },
        "bn": {
            "message": "আলু পাতায় আর্লি ব্লাইট রোগ শনাক্ত হয়েছে।",
            "basic_advice": "নিচের আক্রান্ত পাতাগুলি সরিয়ে ফেলুন। ম্যানকোজেব স্প্রে করুন।",
            "treatment": "ম্যানকোজেব 75% WP @ 2.5 গ্রাম/লিটার স্প্রে করুন। ৭-১০ দিন পর পুনরাবৃত্তি।"
        }
    },

    "potato_late_blight": {
        "en": {
            "message": "Potato Late Blight (Phytophthora infestans) detected — same pathogen that caused the Irish Famine. Extremely destructive.",
            "basic_advice": "Act immediately — this disease can destroy an entire crop in days under wet conditions. Remove all infected material. Apply systemic fungicide urgently.",
            "treatment": "Spray Metalaxyl 8% + Mancozeb 64% WP @ 2.5 g/L or Dimethomorph 50% WP @ 1.5 g/L. Repeat every 5–7 days in wet weather."
        },
        "hi": {
            "message": "आलू में पछेती झुलसा (लेट ब्लाइट) पाया गया — यह बेहद खतरनाक बीमारी है।",
            "basic_advice": "तत्काल उपाय करें — यह रोग गीले मौसम में पूरी फसल नष्ट कर सकता है। मेटालैक्सिल + मैंकोज़ेब का तुरंत छिड़काव करें।",
            "treatment": "मेटालैक्सिल 8% + मैंकोज़ेब 64% WP @ 2.5 ग्राम/लीटर छिड़काव करें। गीले मौसम में हर 5-7 दिनों में दोहराएं।"
        },
        "mr": {
            "message": "बटाट्यावर लेट ब्लाइट आढळला — हा अत्यंत विनाशकारी रोग आहे.",
            "basic_advice": "त्वरित उपाय करा. मेटालॅक्सिल + मॅन्कोझेब लगेच फवारणी करा.",
            "treatment": "मेटालॅक्सिल 8% + मॅन्कोझेब 64% WP @ 2.5 ग्राम/लिटर फवारणी करा. ओल्या हवामानात दर 5-7 दिवसांनी करा."
        },
        "pa": {
            "message": "ਆਲੂ 'ਤੇ ਲੇਟ ਬਲਾਈਟ ਮਿਲਿਆ — ਇਹ ਬਹੁਤ ਖਤਰਨਾਕ ਬਿਮਾਰੀ ਹੈ।",
            "basic_advice": "ਤੁਰੰਤ ਕਾਰਵਾਈ ਕਰੋ। ਮੈਟਾਲੈਕਸਿਲ + ਮੈਂਕੋਜ਼ੇਬ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।",
            "treatment": "ਮੈਟਾਲੈਕਸਿਲ 8% + ਮੈਂਕੋਜ਼ੇਬ 64% WP @ 2.5 ਗ੍ਰਾਮ/ਲੀਟਰ ਛਿੜਕਾਅ ਕਰੋ। ਗਿੱਲੇ ਮੌਸਮ ਵਿੱਚ ਹਰ 5-7 ਦਿਨਾਂ ਬਾਅਦ।"
        },
        "ta": {
            "message": "உருளைக்கிழங்கில் லேட் ப்ளைட் கண்டறியப்பட்டது — மிகவும் அழிவுகரமான நோய்.",
            "basic_advice": "உடனடியாக நடவடிக்கை எடுக்கவும். மெட்டாலாக்சில் + மேன்கோசெப் தெளிக்கவும்.",
            "treatment": "மெட்டாலாக்சில் 8% + மேன்கோசெப் 64% WP @ 2.5 கிராம்/லிட்டர் தெளிக்கவும். 5-7 நாட்களுக்கு ஒருமுறை."
        },
        "te": {
            "message": "బంగాళాదుంపలో లేట్ బ్లైట్ వ్యాధి గుర్తించబడింది — చాలా వినాశకరమైన వ్యాధి.",
            "basic_advice": "వెంటనే చర్య తీసుకోండి. మెటలాక్సిల్ + మాంకోజెబ్ పిచికారి చేయండి.",
            "treatment": "మెటలాక్సిల్ 8% + మాంకోజెబ్ 64% WP @ 2.5 గ్రా/లీ పిచికారి చేయండి. తడి వాతావరణంలో 5-7 రోజులకు ఒకసారి."
        },
        "bn": {
            "message": "আলুতে লেট ব্লাইট রোগ শনাক্ত হয়েছে — এটি অত্যন্ত বিধ্বংসী রোগ।",
            "basic_advice": "অবিলম্বে ব্যবস্থা নিন। মেটালাক্সিল + ম্যানকোজেব স্প্রে করুন।",
            "treatment": "মেটালাক্সিল 8% + ম্যানকোজেব 64% WP @ 2.5 গ্রাম/লিটার স্প্রে করুন। ভেজা আবহাওয়ায় ৫-৭ দিন পর পুনরাবৃত্তি।"
        }
    },

    "potato_healthy": {
        "en": {
            "message": "Potato plant appears healthy with no visible disease signs.",
            "basic_advice": "Continue regular watering and hilling. Monitor for early signs of blight, especially during humid/rainy periods.",
            "treatment": None
        },
        "hi": {
            "message": "आलू का पौधा स्वस्थ दिखाई दे रहा है।",
            "basic_advice": "नियमित सिंचाई और मिट्टी चढ़ाना जारी रखें। आर्द्र मौसम में झुलसा रोग के लिए निगरानी रखें।",
            "treatment": None
        },
        "mr": {
            "message": "बटाट्याचे झाड निरोगी दिसत आहे.",
            "basic_advice": "नियमित पाणी आणि माती भरणे सुरू ठेवा. दमट हवामानात ब्लाइटवर लक्ष ठेवा.",
            "treatment": None
        },
        "pa": {
            "message": "ਆਲੂ ਦਾ ਪੌਦਾ ਸਿਹਤਮੰਦ ਦਿਖਾਈ ਦੇ ਰਿਹਾ ਹੈ।",
            "basic_advice": "ਨਿਯਮਤ ਸਿੰਚਾਈ ਜਾਰੀ ਰੱਖੋ। ਬਰਸਾਤੀ ਮੌਸਮ ਵਿੱਚ ਝੁਲਸ ਰੋਗ 'ਤੇ ਨਜ਼ਰ ਰੱਖੋ।",
            "treatment": None
        },
        "ta": {
            "message": "உருளைக்கிழங்கு செடி ஆரோக்கியமாக காணப்படுகிறது.",
            "basic_advice": "தொடர்ந்து நீர் பாய்ச்சவும். மழை காலத்தில் ப்ளைட் நோய்க்கு கவனம் செலுத்தவும்.",
            "treatment": None
        },
        "te": {
            "message": "బంగాళాదుంప మొక్క ఆరోగ్యంగా కనిపిస్తోంది.",
            "basic_advice": "నీటిపారుదల కొనసాగించండి. తడి వాతావరణంలో బ్లైట్ కోసం పర్యవేక్షించండి.",
            "treatment": None
        },
        "bn": {
            "message": "আলু গাছটি সুস্থ দেখাচ্ছে।",
            "basic_advice": "নিয়মিত সেচ অব্যাহত রাখুন। আর্দ্র আবহাওয়ায় ব্লাইটের জন্য পর্যবেক্ষণ করুন।",
            "treatment": None
        }
    },

    # ──────────────────────────────────────────────
    # CORN / MAIZE DISEASES
    # ──────────────────────────────────────────────

    "corn_cercospora_leaf_spot": {
        "en": {
            "message": "Corn Gray Leaf Spot / Cercospora Leaf Spot detected — a major fungal disease of maize.",
            "basic_advice": "Use resistant varieties. Apply Azoxystrobin or Propiconazole fungicide. Rotate crops. Avoid overhead irrigation.",
            "treatment": "Spray Azoxystrobin 23% SC @ 1 mL/L or Propiconazole 25% EC @ 1 mL/L at early tassel stage. Repeat after 14 days."
        },
        "hi": {
            "message": "मक्का में सर्कोस्पोरा लीफ स्पॉट (धूसर पत्ती धब्बा) रोग पाया गया।",
            "basic_advice": "प्रतिरोधी किस्मों का उपयोग करें। एजोक्सीस्ट्रोबिन या प्रोपिकोनाज़ोल का छिड़काव करें। फसल चक्र अपनाएं।",
            "treatment": "एजोक्सीस्ट्रोबिन 23% SC @ 1 mL/लीटर छिड़काव करें। 14 दिनों में दोहराएं।"
        },
        "mr": {
            "message": "मक्यावर सर्कोस्पोरा लीफ स्पॉट आढळला.",
            "basic_advice": "प्रतिरोधक वाण वापरा. अझोक्सीस्ट्रोबिन फवारणी करा. पीक फेरपालट करा.",
            "treatment": "अझोक्सीस्ट्रोबिन 23% SC @ 1 mL/लिटर फवारणी करा. 14 दिवसांनी पुन्हा करा."
        },
        "pa": {
            "message": "ਮੱਕੀ 'ਤੇ ਸਰਕੋਸਪੋਰਾ ਲੀਫ ਸਪਾਟ ਮਿਲਿਆ ਹੈ।",
            "basic_advice": "ਰੋਧਕ ਕਿਸਮਾਂ ਵਰਤੋ। ਅਜ਼ੋਕਸੀਸਟ੍ਰੋਬਿਨ ਛਿੜਕਾਅ ਕਰੋ।",
            "treatment": "ਅਜ਼ੋਕਸੀਸਟ੍ਰੋਬਿਨ 23% SC @ 1 mL/ਲੀਟਰ ਛਿੜਕਾਅ ਕਰੋ। 14 ਦਿਨਾਂ ਬਾਅਦ ਦੁਹਰਾਓ।"
        },
        "ta": {
            "message": "சோளத்தில் சர்கோஸ்போரா இலை புள்ளி நோய் கண்டறியப்பட்டது.",
            "basic_advice": "எதிர்ப்பு சக்தியுள்ள ரகங்களை பயன்படுத்தவும். அசோக்ஸிஸ்ட்ரோபின் தெளிக்கவும்.",
            "treatment": "அசோக்ஸிஸ்ட்ரோபின் 23% SC @ 1 mL/லிட்டர் தெளிக்கவும். 14 நாட்களுக்கு ஒருமுறை."
        },
        "te": {
            "message": "మొక్కజొన్నలో సెర్కోస్పోరా ఆకు మచ్చ వ్యాధి గుర్తించబడింది.",
            "basic_advice": "నిరోధక రకాలు వాడండి. అజోక్సీస్ట్రోబిన్ పిచికారి చేయండి.",
            "treatment": "అజోక్సీస్ట్రోబిన్ 23% SC @ 1 mL/లీ పిచికారి చేయండి. 14 రోజులకు ఒకసారి."
        },
        "bn": {
            "message": "ভুট্টায় সার্কোস্পোরা লিফ স্পট রোগ শনাক্ত হয়েছে।",
            "basic_advice": "প্রতিরোধী জাত ব্যবহার করুন। অ্যাজোক্সিস্ট্রোবিন স্প্রে করুন।",
            "treatment": "অ্যাজোক্সিস্ট্রোবিন 23% SC @ 1 mL/লিটার স্প্রে করুন। ১৪ দিন পর পুনরাবৃত্তি।"
        }
    },

    "corn_common_rust": {
        "en": {
            "message": "Corn Common Rust (Puccinia sorghi) detected — orange-brown pustules on both leaf surfaces.",
            "basic_advice": "Use resistant hybrids. Apply Propiconazole or Tebuconazole fungicide at early infection. Destroy crop residues after harvest.",
            "treatment": "Spray Propiconazole 25% EC @ 1 mL/L or Tebuconazole 25.9% EC @ 1 mL/L. Repeat every 14 days."
        },
        "hi": {
            "message": "मक्का में कॉमन रस्ट (सामान्य किट्ट) के लक्षण पाए गए हैं।",
            "basic_advice": "प्रतिरोधी संकर किस्मों का उपयोग करें। प्रोपिकोनाज़ोल या टेबूकोनाज़ोल का छिड़काव करें।",
            "treatment": "प्रोपिकोनाज़ोल 25% EC @ 1 mL/लीटर छिड़काव करें। 14 दिनों में दोहराएं।"
        },
        "mr": {
            "message": "मक्यावर कॉमन रस्ट आढळला.",
            "basic_advice": "प्रतिरोधक संकरित वाण वापरा. प्रोपिकोनाझोल फवारणी करा.",
            "treatment": "प्रोपिकोनाझोल 25% EC @ 1 mL/लिटर फवारणी करा. 14 दिवसांनी पुन्हा करा."
        },
        "pa": {
            "message": "ਮੱਕੀ 'ਤੇ ਕਾਮਨ ਰਸਟ ਮਿਲਿਆ ਹੈ।",
            "basic_advice": "ਰੋਧਕ ਹਾਈਬ੍ਰਿਡ ਕਿਸਮਾਂ ਵਰਤੋ। ਪ੍ਰੋਪਿਕੋਨਾਜ਼ੋਲ ਛਿੜਕਾਅ ਕਰੋ।",
            "treatment": "ਪ੍ਰੋਪਿਕੋਨਾਜ਼ੋਲ 25% EC @ 1 mL/ਲੀਟਰ ਛਿੜਕਾਅ ਕਰੋ। 14 ਦਿਨਾਂ ਬਾਅਦ ਦੁਹਰਾਓ।"
        },
        "ta": {
            "message": "சோளத்தில் பொதுவான துரு நோய் கண்டறியப்பட்டது.",
            "basic_advice": "எதிர்ப்பு சக்தியுள்ள ரகங்களை பயன்படுத்தவும். புரோபிகோனசோல் தெளிக்கவும்.",
            "treatment": "புரோபிகோனசோல் 25% EC @ 1 mL/லிட்டர் தெளிக்கவும். 14 நாட்களுக்கு ஒருமுறை."
        },
        "te": {
            "message": "మొక్కజొన్నలో సాధారణ తుప్పు వ్యాధి గుర్తించబడింది.",
            "basic_advice": "నిరోధక సంకర రకాలు వాడండి. ప్రోపికోనజోల్ పిచికారి చేయండి.",
            "treatment": "ప్రోపికోనజోల్ 25% EC @ 1 mL/లీ పిచికారి చేయండి. 14 రోజులకు ఒకసారి."
        },
        "bn": {
            "message": "ভুট্টায় কমন রাস্ট রোগ শনাক্ত হয়েছে।",
            "basic_advice": "প্রতিরোধী হাইব্রিড জাত ব্যবহার করুন। প্রোপিকোনাজোল স্প্রে করুন।",
            "treatment": "প্রোপিকোনাজোল 25% EC @ 1 mL/লিটার স্প্রে করুন। ১৪ দিন পর পুনরাবৃত্তি।"
        }
    },

    "corn_northern_leaf_blight": {
        "en": {
            "message": "Northern Corn Leaf Blight (Exserohilum turcicum) detected — long cigar-shaped gray-green lesions on leaves.",
            "basic_advice": "Use resistant varieties. Apply Azoxystrobin or Propiconazole at tassel emergence. Remove infected crop debris after harvest.",
            "treatment": "Spray Azoxystrobin + Propiconazole (Amistar Top) @ 1 mL/L. Apply at 50% tassel emergence and repeat after 14 days."
        },
        "hi": {
            "message": "मक्का में नॉर्दर्न लीफ ब्लाइट के लक्षण पाए गए हैं।",
            "basic_advice": "प्रतिरोधी किस्मों का उपयोग करें। एजोक्सीस्ट्रोबिन + प्रोपिकोनाज़ोल का छिड़काव करें।",
            "treatment": "एजोक्सीस्ट्रोबिन + प्रोपिकोनाज़ोल @ 1 mL/लीटर छिड़काव करें। 14 दिनों में दोहराएं।"
        },
        "mr": {
            "message": "मक्यावर नॉर्दर्न लीफ ब्लाइट आढळला.",
            "basic_advice": "प्रतिरोधक वाण वापरा. अझोक्सीस्ट्रोबिन + प्रोपिकोनाझोल फवारणी करा.",
            "treatment": "अझोक्सीस्ट्रोबिन + प्रोपिकोनाझोल @ 1 mL/लिटर फवारणी करा. 14 दिवसांनी पुन्हा करा."
        },
        "pa": {
            "message": "ਮੱਕੀ 'ਤੇ ਨੌਰਦਰਨ ਲੀਫ ਬਲਾਈਟ ਮਿਲਿਆ ਹੈ।",
            "basic_advice": "ਰੋਧਕ ਕਿਸਮਾਂ ਵਰਤੋ। ਅਜ਼ੋਕਸੀਸਟ੍ਰੋਬਿਨ + ਪ੍ਰੋਪਿਕੋਨਾਜ਼ੋਲ ਛਿੜਕਾਅ ਕਰੋ।",
            "treatment": "ਅਜ਼ੋਕਸੀਸਟ੍ਰੋਬਿਨ + ਪ੍ਰੋਪਿਕੋਨਾਜ਼ੋਲ @ 1 mL/ਲੀਟਰ ਛਿੜਕਾਅ ਕਰੋ। 14 ਦਿਨਾਂ ਬਾਅਦ ਦੁਹਰਾਓ।"
        },
        "ta": {
            "message": "சோளத்தில் வடக்கு இலை கருகல் நோய் கண்டறியப்பட்டது.",
            "basic_advice": "எதிர்ப்பு சக்தியுள்ள ரகங்களை பயன்படுத்தவும். அசோக்ஸிஸ்ட்ரோபின் + புரோபிகோனசோல் தெளிக்கவும்.",
            "treatment": "அசோக்ஸிஸ்ட்ரோபின் + புரோபிகோனசோல் @ 1 mL/லிட்டர் தெளிக்கவும். 14 நாட்களுக்கு ஒருமுறை."
        },
        "te": {
            "message": "మొక్కజొన్నలో ఉత్తర ఆకు మాడు వ్యాధి గుర్తించబడింది.",
            "basic_advice": "నిరోధక రకాలు వాడండి. అజోక్సీస్ట్రోబిన్ + ప్రోపికోనజోల్ పిచికారి చేయండి.",
            "treatment": "అజోక్సీస్ట్రోబిన్ + ప్రోపికోనజోల్ @ 1 mL/లీ పిచికారి చేయండి. 14 రోజులకు ఒకసారి."
        },
        "bn": {
            "message": "ভুট্টায় নর্দার্ন লিফ ব্লাইট রোগ শনাক্ত হয়েছে।",
            "basic_advice": "প্রতিরোধী জাত ব্যবহার করুন। অ্যাজোক্সিস্ট্রোবিন + প্রোপিকোনাজোল স্প্রে করুন।",
            "treatment": "অ্যাজোক্সিস্ট্রোবিন + প্রোপিকোনাজোল @ 1 mL/লিটার স্প্রে করুন। ১৪ দিন পর পুনরাবৃত্তি।"
        }
    },

    "corn_healthy": {
        "en": {
            "message": "Corn/Maize plant appears healthy.",
            "basic_advice": "Continue regular fertilization (especially nitrogen). Monitor for rust and blight during humid periods.",
            "treatment": None
        },
        "hi": {
            "message": "मक्का का पौधा स्वस्थ दिखाई दे रहा है।",
            "basic_advice": "नियमित खाद (विशेषकर नाइट्रोजन) जारी रखें। आर्द्र मौसम में किट्ट और ब्लाइट पर नजर रखें।",
            "treatment": None
        },
        "mr": {
            "message": "मक्याचे झाड निरोगी दिसत आहे.",
            "basic_advice": "नियमित खत (विशेषतः नत्र) द्या. दमट हवामानात रस्ट आणि ब्लाइटवर लक्ष ठेवा.",
            "treatment": None
        },
        "pa": {
            "message": "ਮੱਕੀ ਦਾ ਪੌਦਾ ਸਿਹਤਮੰਦ ਦਿਖਾਈ ਦੇ ਰਿਹਾ ਹੈ।",
            "basic_advice": "ਨਿਯਮਤ ਖਾਦ ਜਾਰੀ ਰੱਖੋ। ਬਰਸਾਤੀ ਮੌਸਮ ਵਿੱਚ ਰਸਟ ਅਤੇ ਬਲਾਈਟ 'ਤੇ ਨਜ਼ਰ ਰੱਖੋ।",
            "treatment": None
        },
        "ta": {
            "message": "சோளச் செடி ஆரோக்கியமாக காணப்படுகிறது.",
            "basic_advice": "தொடர்ந்து உரமிடவும். ஈரமான காலத்தில் துரு மற்றும் கருகல் நோய்க்கு கவனம் செலுத்தவும்.",
            "treatment": None
        },
        "te": {
            "message": "మొక్కజొన్న మొక్క ఆరోగ్యంగా కనిపిస్తోంది.",
            "basic_advice": "ఎరువులు కొనసాగించండి. తడి వాతావరణంలో తుప్పు మరియు బ్లైట్ కోసం పర్యవేక్షించండి.",
            "treatment": None
        },
        "bn": {
            "message": "ভুট্টা গাছটি সুস্থ দেখাচ্ছে।",
            "basic_advice": "নিয়মিত সার দিন। আর্দ্র আবহাওয়ায় রাস্ট ও ব্লাইটের জন্য পর্যবেক্ষণ করুন।",
            "treatment": None
        }
    },

    # ──────────────────────────────────────────────
    # GENERIC FALLBACKS (English + Hindi)
    # ──────────────────────────────────────────────

    "generic_blight": {
        "en": {
            "message": "Blight disease detected on crop leaves.",
            "basic_advice": "Remove and destroy affected plant parts. Apply Mancozeb or Metalaxyl-based fungicide. Avoid wet foliage.",
            "treatment": "Spray Mancozeb 75% WP @ 2.5 g/L. In severe cases use Metalaxyl 8% + Mancozeb 64% WP @ 2.5 g/L. Repeat every 7–10 days."
        },
        "hi": {
            "message": "फसल की पत्तियों पर ब्लाइट रोग के लक्षण पाए गए हैं।",
            "basic_advice": "प्रभावित पौधे के हिस्सों को हटाएं। मैंकोज़ेब या मेटालैक्सिल का छिड़काव करें।",
            "treatment": "मैंकोज़ेब 75% WP @ 2.5 ग्राम/लीटर छिड़काव करें। 7-10 दिनों में दोहराएं।"
        }
    },

    "generic_rust": {
        "en": {
            "message": "Rust disease detected on crop leaves — orange/brown pustules visible.",
            "basic_advice": "Apply Propiconazole or Tebuconazole fungicide. Use resistant varieties in future. Remove infected debris.",
            "treatment": "Spray Propiconazole 25% EC @ 1 mL/L or Tebuconazole 25.9% EC @ 1 mL/L. Repeat every 14 days."
        },
        "hi": {
            "message": "फसल की पत्तियों पर किट्ट (रस्ट) रोग के लक्षण पाए गए हैं।",
            "basic_advice": "प्रोपिकोनाज़ोल या टेबूकोनाज़ोल का छिड़काव करें।",
            "treatment": "प्रोपिकोनाज़ोल 25% EC @ 1 mL/लीटर छिड़काव करें। 14 दिनों में दोहराएं।"
        }
    },

    "generic_powdery_mildew": {
        "en": {
            "message": "Powdery Mildew detected — white powdery coating on leaf surfaces.",
            "basic_advice": "Improve air circulation. Apply Sulphur-based fungicide or Myclobutanil. Avoid excess nitrogen fertilization.",
            "treatment": "Spray Wettable Sulphur 80% WP @ 3 g/L or Myclobutanil 10% WP @ 1 g/L. Repeat every 10–14 days."
        },
        "hi": {
            "message": "पत्तियों पर पाउडरी मिल्ड्यू (खर्रा रोग) के लक्षण पाए गए हैं।",
            "basic_advice": "हवा का संचार सुधारें। सल्फर या माइक्लोब्यूटेनिल का छिड़काव करें।",
            "treatment": "घुलनशील सल्फर 80% WP @ 3 ग्राम/लीटर छिड़काव करें। 10-14 दिनों में दोहराएं।"
        }
    },

    "generic_leaf_spot": {
        "en": {
            "message": "Leaf spot disease detected on crop leaves.",
            "basic_advice": "Remove infected leaves. Apply Mancozeb or Chlorothalonil fungicide. Improve plant spacing for air circulation.",
            "treatment": "Spray Mancozeb 75% WP @ 2.5 g/L or Chlorothalonil 75% WP @ 2 g/L. Repeat every 10 days."
        },
        "hi": {
            "message": "फसल की पत्तियों पर पत्ती धब्बा रोग के लक्षण पाए गए हैं।",
            "basic_advice": "प्रभावित पत्तियां हटाएं। मैंकोज़ेब या क्लोरोथैलोनिल का छिड़काव करें।",
            "treatment": "मैंकोज़ेब 75% WP @ 2.5 ग्राम/लीटर छिड़काव करें। 10 दिनों में दोहराएं।"
        }
    },

    # ──────────────────────────────────────────────
    # GENERIC DISEASE DETECTED (outside dictionary)
    # ──────────────────────────────────────────────

    "generic_disease": {
        "en": {
            "message": "A potential disease has been identified on the crop leaves.",
            "basic_advice": "Monitor the affected area closely. Remove visibly diseased leaves. Consult a local agronomist for crop-specific treatment advice.",
            "treatment": "As a precaution, apply Mancozeb 75% WP @ 2.5 g/L or Copper Oxychloride 50% WP @ 3 g/L. Repeat every 10 days while symptoms persist."
        },
        "hi": {
            "message": "फसल की पत्तियों पर एक संभावित रोग की पहचान हुई है।",
            "basic_advice": "प्रभावित क्षेत्र पर नजर रखें। रोगग्रस्त पत्तियां हटाएं। स्थानीय कृषि विशेषज्ञ से सलाह लें।",
            "treatment": "सावधानी के तौर पर मैंकोज़ेब 75% WP @ 2.5 ग्राम/लीटर या कॉपर ऑक्सीक्लोराइड 50% WP @ 3 ग्राम/लीटर का छिड़काव करें।"
        },
        "mr": {
            "message": "पिकाच्या पानांवर संभाव्य रोगाची ओळख झाली आहे.",
            "basic_advice": "बाधित भागावर लक्ष ठेवा. रोगट पाने काढा. स्थानिक कृषी तज्ज्ञाचा सल्ला घ्या.",
            "treatment": "सावधगिरी म्हणून मॅन्कोझेब 75% WP @ 2.5 ग्राम/लिटर किंवा कॉपर ऑक्सीक्लोराइड 50% WP @ 3 ग्राम/लिटर फवारणी करा."
        },
        "pa": {
            "message": "ਫਸਲ ਦੇ ਪੱਤਿਆਂ 'ਤੇ ਇੱਕ ਸੰਭਾਵਿਤ ਬਿਮਾਰੀ ਦੀ ਪਛਾਣ ਹੋਈ ਹੈ।",
            "basic_advice": "ਪ੍ਰਭਾਵਿਤ ਖੇਤਰ 'ਤੇ ਨਜ਼ਰ ਰੱਖੋ। ਰੋਗੀ ਪੱਤੇ ਹਟਾਓ। ਸਥਾਨਕ ਖੇਤੀਬਾੜੀ ਮਾਹਰ ਤੋਂ ਸਲਾਹ ਲਓ।",
            "treatment": "ਸਾਵਧਾਨੀ ਵਜੋਂ ਮੈਂਕੋਜ਼ੇਬ 75% WP @ 2.5 ਗ੍ਰਾਮ/ਲੀਟਰ ਜਾਂ ਕਾਪਰ ਆਕਸੀਕਲੋਰਾਈਡ 50% WP @ 3 ਗ੍ਰਾਮ/ਲੀਟਰ ਛਿੜਕਾਅ ਕਰੋ।"
        },
        "ta": {
            "message": "பயிர் இலைகளில் ஒரு சாத்தியமான நோய் கண்டறியப்பட்டது.",
            "basic_advice": "பாதிக்கப்பட்ட பகுதியை கவனமாக கண்காணிக்கவும். நோயுற்ற இலைகளை அகற்றவும். உள்ளூர் வேளாண் நிபுணரை அணுகவும்.",
            "treatment": "முன்னெச்சரிக்கையாக மேன்கோசெப் 75% WP @ 2.5 கிராம்/லிட்டர் அல்லது செம்பு ஆக்சிகுளோரைடு 50% WP @ 3 கிராம்/லிட்டர் தெளிக்கவும்."
        },
        "te": {
            "message": "పంట ఆకులపై ఒక సంభావ్య వ్యాధి గుర్తించబడింది.",
            "basic_advice": "బాధిత ప్రాంతాన్ని నిశితంగా పర్యవేక్షించండి. రోగగ్రస్త ఆకులను తొలగించండి. స్థానిక వ్యవసాయ నిపుణుడిని సంప్రదించండి.",
            "treatment": "జాగ్రత్తగా మాంకోజెబ్ 75% WP @ 2.5 గ్రా/లీ లేదా కాపర్ ఆక్సీక్లోరైడ్ 50% WP @ 3 గ్రా/లీ పిచికారి చేయండి."
        },
        "bn": {
            "message": "ফসলের পাতায় একটি সম্ভাব্য রোগ শনাক্ত হয়েছে।",
            "basic_advice": "আক্রান্ত স্থান মনোযোগ দিয়ে পর্যবেক্ষণ করুন। রোগাক্রান্ত পাতাগুলি সরিয়ে ফেলুন। স্থানীয় কৃষি বিশেষজ্ঞের পরামর্শ নিন।",
            "treatment": "সতর্কতা হিসাবে ম্যানকোজেব 75% WP @ 2.5 গ্রাম/লিটার বা কপার অক্সিক্লোরাইড 50% WP @ 3 গ্রাম/লিটার স্প্রে করুন।"
        }
    },

    # ──────────────────────────────────────────────
    # GENERAL HEALTHY & UNCERTAIN
    # ──────────────────────────────────────────────

    "healthy": {
        "en": {
            "message": "The crop leaves appear healthy with no visible signs of disease.",
            "basic_advice": "Maintain current irrigation and soil health management practices. Consider preventive fungicide during high-humidity periods.",
            "treatment": None
        },
        "hi": {
            "message": "फसल की पत्तियां स्वस्थ दिखाई दे रही हैं।",
            "basic_advice": "वर्तमान सिंचाई और देखभाल जारी रखें। अधिक आर्द्रता के दौरान निवारक फफूंदनाशक का उपयोग करें।",
            "treatment": None
        },
        "mr": {
            "message": "पिकाची पाने निरोगी दिसत आहेत.",
            "basic_advice": "नियमित पाणी आणि खतांचे नियोजन सुरू ठेवा.",
            "treatment": None
        },
        "pa": {
            "message": "ਫਸਲ ਦੇ ਪੱਤੇ ਸਿਹਤਮੰਦ ਦਿਖਾਈ ਦੇ ਰਹੇ ਹਨ।",
            "basic_advice": "ਮੌਜੂਦਾ ਸੰਚਾਈ ਅਤੇ ਦੇਖਭਾਲ ਜਾਰੀ ਰੱਖੋ।",
            "treatment": None
        },
        "ta": {
            "message": "பயிர் இலைகள் ஆரோக்கியமாக காணப்படுகின்றன.",
            "basic_advice": "தற்போதைய நீர் மற்றும் உர நிர்வாகத்தை தொடரவும்.",
            "treatment": None
        },
        "te": {
            "message": "పైరు ఆకులు ఆరోగ్యంగా కనిపిస్తున్నాయి.",
            "basic_advice": "ప్రస్తుత నీటి పారుదల మరియు పోషణను కొనసాగించండి.",
            "treatment": None
        },
        "bn": {
            "message": "ফসলটি সম্পূর্ণ সুস্থ বলে মনে হচ্ছে।",
            "basic_advice": "বর্তমান সেচ এবং যত্ন অব্যাহত রাখুন।",
            "treatment": None
        }
    },

    "uncertain": {
        "en": {
            "message": "The image analysis could not reach a confident diagnosis.",
            "basic_advice": "Please upload a clearer photo taken in good lighting with the diseased leaf filling the frame.",
            "treatment": None
        },
        "hi": {
            "message": "छवि से रोग का स्पष्ट पता नहीं चल सका।",
            "basic_advice": "कृपया अच्छी रोशनी में बीमार पत्ते की स्पष्ट फोटो अपलोड करें।",
            "treatment": None
        },
        "mr": {
            "message": "प्रतिमेवरून स्पष्ट निदान होऊ शकले नाही.",
            "basic_advice": "कृपया चांगल्या प्रकाशात स्पष्ट फोटो अपलोड करा.",
            "treatment": None
        },
        "pa": {
            "message": "ਤਸਵੀਰ ਤੋਂ ਸਪੱਸ਼ਟ ਬੀਮਾਰੀ ਦਾ ਪਤਾ ਨਹੀਂ ਲੱਗ ਸਕਿਆ।",
            "basic_advice": "ਕਿਰਪਾ ਕਰਕੇ ਚੰਗੀ ਰੋਸ਼ਨੀ ਵਿੱਚ ਸਾਫ਼ ਤਸਵੀਰ ਅਪਲੋਡ ਕਰੋ।",
            "treatment": None
        },
        "ta": {
            "message": "படத்திலிருந்து நோயை துல்லியமாகக் கண்டறிய முடியவில்லை.",
            "basic_advice": "நல்ல வெளிச்சத்தில் தெளிவான புகைப்படத்தைப் பதிவேற்றவும்.",
            "treatment": None
        },
        "te": {
            "message": "చిత్రం నుండి వ్యాధిని స్పష్టంగా గుర్తించలేకపోయాము.",
            "basic_advice": "దయచేసి మంచి కాంతిలో స్పష్టమైన ఫోటోను అప్‌లోడ్ చేయండి.",
            "treatment": None
        },
        "bn": {
            "message": "ছবি থেকে রোগটি স্পষ্টভাবে শনাক্ত করা যায়নি।",
            "basic_advice": "অনুগ্রহ করে ভালো আলোয় একটি স্পষ্ট ছবি তুলুন।",
            "treatment": None
        }
    }
}


def map_label_to_advisory_key(label: str) -> str:
    """
    Maps a cleaned model prediction label to an advisory dictionary key.
    Uses keyword matching to handle label variations from the PlantVillage model.
    """
    label_lower = label.lower().strip()

    # Healthy check (crop-specific first)
    if "healthy" in label_lower:
        if "tomato" in label_lower:
            return "tomato_healthy"
        if "potato" in label_lower:
            return "potato_healthy"
        if "corn" in label_lower or "maize" in label_lower:
            return "corn_healthy"
        return "healthy"

    # Tomato diseases
    if "tomato" in label_lower:
        if "bacterial spot" in label_lower:
            return "tomato_bacterial_spot"
        if "early blight" in label_lower:
            return "tomato_early_blight"
        if "late blight" in label_lower:
            return "tomato_late_blight"
        if "leaf mold" in label_lower:
            return "tomato_leaf_mold"
        if "septoria" in label_lower:
            return "tomato_septoria_leaf_spot"
        if "spider" in label_lower or "mite" in label_lower:
            return "tomato_spider_mites"
        if "target spot" in label_lower:
            return "tomato_target_spot"
        if "yellow leaf curl" in label_lower or "ylcv" in label_lower:
            return "tomato_yellow_leaf_curl_virus"
        if "mosaic" in label_lower:
            return "tomato_mosaic_virus"

    # Potato diseases
    if "potato" in label_lower:
        if "early blight" in label_lower:
            return "potato_early_blight"
        if "late blight" in label_lower:
            return "potato_late_blight"

    # Corn / Maize diseases
    if "corn" in label_lower or "maize" in label_lower:
        if "cercospora" in label_lower or "gray leaf" in label_lower:
            return "corn_cercospora_leaf_spot"
        if "common rust" in label_lower:
            return "corn_common_rust"
        if "northern leaf blight" in label_lower:
            return "corn_northern_leaf_blight"

    # Generic fallbacks based on disease type
    if "late blight" in label_lower or "early blight" in label_lower or "blight" in label_lower:
        return "generic_blight"
    if "rust" in label_lower:
        return "generic_rust"
    if "mildew" in label_lower or "powdery" in label_lower:
        return "generic_powdery_mildew"
    if "spot" in label_lower or "lesion" in label_lower:
        return "generic_leaf_spot"

    return "uncertain"


def get_advisory(advisory_key: str, lang: str = "en") -> dict:
    """
    Retrieves multilingual advisory based on advisory key and language.
    Falls back to English if requested language is unavailable.
    Falls back to 'uncertain' if the key is not found.
    """
    disease_dict = ADVISORY_DICTIONARY.get(advisory_key, ADVISORY_DICTIONARY["uncertain"])
    return disease_dict.get(lang, disease_dict.get("en"))
