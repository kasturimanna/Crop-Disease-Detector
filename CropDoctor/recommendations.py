# Crop disease database and recommendation system

DISEASE_DATA = {
    # ----------------------------------------------------
    # Model Classes (15 YOLO11 Classes)
    # ----------------------------------------------------
    "Pepper__bell___Bacterial_spot": {
        "disease": "Bacterial Spot",
        "crop": "Bell Pepper",
        "description": "A destructive bacterial disease affecting bell peppers, causing necrotic leaf spotting, defoliation, and fruit damage.",
        "symptoms": "Small, dark brown, water-soaked circular to irregular lesions with yellow halos on leaves. In severe cases, extensive defoliation occurs, exposing fruit to sunscald.",
        "causes": "Bacterium Xanthomonas campestris pv. vesicatoria, spread by rain splash, overhead irrigation, and contaminated seeds or tools.",
        "treatments": [
            "Apply copper-based bactericide sprays combined with Mancozeb at the earliest onset of symptoms.",
            "Remove and destroy heavily infected plant debris to reduce bacterial inoculums.",
            "Avoid handling or working among plants when the foliage is wet."
        ],
        "prevention": [
            "Plant certified disease-free and resistant bell pepper varieties.",
            "Use drip irrigation instead of overhead watering to keep foliage dry.",
            "Practice 2-3 year crop rotation away from solanaceous crops (peppers, tomatoes, potatoes)."
        ]
    },
    "Pepper__bell___healthy": {
        "disease": "Healthy",
        "crop": "Bell Pepper",
        "description": "The bell pepper plant exhibits vibrant, uniform green foliage with no detectable pathogen lesions or pest stress.",
        "symptoms": "Firm, glossy leaves with consistent green coloration and normal venation. No chlorosis, wilting, or necrotic tissue present.",
        "causes": "Optimal ambient conditions, adequate soil moisture, and balanced nutrient availability.",
        "treatments": [
            "No chemical treatment needed.",
            "Maintain regular watering and standard balanced NPK fertilization."
        ],
        "prevention": [
            "Inspect regularly for aphids, thrips, and mites.",
            "Ensure proper plant spacing for good canopy airflow.",
            "Maintain consistent soil moisture to prevent blossom end rot during fruit set."
        ]
    },
    "Potato___Early_blight": {
        "disease": "Early Blight",
        "crop": "Potato",
        "description": "A widespread fungal disease caused by Alternaria solani affecting potato foliage, stems, and tubers, leading to premature defoliation.",
        "symptoms": "Dark brown to black concentric circular rings ('target board' pattern) on older lower leaves, often surrounded by chlorotic yellow halos.",
        "causes": "Fungus Alternaria solani, surviving in infected crop residue and spreading during alternating warm wet and dry weather.",
        "treatments": [
            "Apply protective fungicides such as Chlorothalonil, Mancozeb, or copper hydroxide at first appearance of spots.",
            "Prune infected lower foliage to reduce fungal spore count and increase airflow.",
            "Apply bio-fungicides containing Bacillus subtilis for organic cultivation."
        ],
        "prevention": [
            "Practice a 3-year crop rotation with non-solanaceous crops.",
            "Avoid overhead irrigation; water at the soil base.",
            "Maintain balanced nitrogen and potassium fertility to prevent premature vine stress."
        ]
    },
    "Potato___Late_blight": {
        "disease": "Late Blight",
        "crop": "Potato",
        "description": "A devastating oomycete infection (Phytophthora infestans) that can rapidly destroy entire potato canopies and rot tubers.",
        "symptoms": "Water-soaked, dark brown to purplish-black lesions on leaves and stems, with white fungal-like fuzz appearing on leaf undersides in high humidity.",
        "causes": "Pathogen Phytophthora infestans, spreading rapidly through wind-borne sporangia during cool (10-20°C), wet, or fog-laden weather.",
        "treatments": [
            "Apply targeted systemic and contact fungicides (Metalaxyl, Dimethomorph, Mancozeb, or Cymoxanil) immediately upon detection.",
            "Rogue out and destroy infected vines immediately to prevent spread to tubers and neighboring fields.",
            "Kill vines 2 weeks before harvest to prevent tuber contamination."
        ],
        "prevention": [
            "Plant only certified disease-free seed tubers.",
            "Ensure wide row spacing and good air drainage.",
            "Eliminate cull piles and volunteer potato plants near production fields."
        ]
    },
    "Potato___healthy": {
        "disease": "Healthy",
        "crop": "Potato",
        "description": "The potato vine demonstrates vigorous vegetative growth with deep green leaves and healthy turgor, free from blight lesions.",
        "symptoms": "Lush green foliage, normal leaf morphology, and complete absence of target spots or water-soaked lesions.",
        "causes": "Favorable soil temperatures, balanced moisture, disease-free seed tubers, and optimal fertility.",
        "treatments": [
            "No chemical treatment needed.",
            "Continue balanced fertilization and hilling practices."
        ],
        "prevention": [
            "Scout fields twice weekly during cool, moist weather for early signs of blight.",
            "Hill soil properly around developing tubers to protect them from sunlight and spore wash.",
            "Maintain uniform soil moisture during tuber initiation and bulking."
        ]
    },
    "Tomato_Bacterial_spot": {
        "disease": "Bacterial Spot",
        "crop": "Tomato",
        "description": "A destructive bacterial infection caused by Xanthomonas species affecting tomato leaves, stems, and fruits, resulting in defoliation and sunscald.",
        "symptoms": "Small (less than 3mm), dark brown to black circular lesions on leaves, often greasy in appearance, surrounded by light yellow halos.",
        "causes": "Bacteria Xanthomonas perforans or X. vesicatoria, spread through splashed rain, overhead sprinklers, and contaminated seed or transplant stock.",
        "treatments": [
            "Apply fixed copper bactericide sprays combined with Mancozeb at early onset.",
            "Apply Actigard (acibenzolar-S-methyl) to activate plant systemic acquired resistance.",
            "Remove and safely discard severely infected plants."
        ],
        "prevention": [
            "Use certified disease-free seed and hot-water treated seeds.",
            "Adopt drip irrigation to prevent water splashing onto foliage.",
            "Sanitize tomato stakes, cages, and pruning shears between plants."
        ]
    },
    "Tomato_Early_blight": {
        "disease": "Early Blight",
        "crop": "Tomato",
        "description": "A common fungal infection caused by Alternaria linariae producing characteristic concentric ring spots on older leaves, progressing upward.",
        "symptoms": "Dark brown circular spots with distinctive concentric 'target' rings on lower leaves, surrounded by yellow chlorotic tissue.",
        "causes": "Fungus Alternaria linariae surviving in soil and plant residue, favored by warm temperatures (24-29°C) and heavy dew or rain.",
        "treatments": [
            "Apply protective fungicides such as Chlorothalonil, Mancozeb, or copper soap.",
            "Prune lower leaves up to 12-18 inches from the ground to prevent soil splash.",
            "Mulch heavily around the plant base to create a physical barrier against soil-borne spores."
        ],
        "prevention": [
            "Practice 3-year crop rotation away from tomatoes, potatoes, and peppers.",
            "Stake or cage plants to keep foliage elevated and dry.",
            "Water at the soil level using soaker hoses or drip lines."
        ]
    },
    "Tomato_Late_blight": {
        "disease": "Late Blight",
        "crop": "Tomato",
        "description": "A highly aggressive pathogen (Phytophthora infestans) that causes rapid collapse of tomato foliage, stem rot, and large greasy brown fruit lesions.",
        "symptoms": "Large, irregular, pale to dark water-soaked lesions that rapidly expand and turn brown and papery. White mildew-like fuzz appears on leaf undersides in high humidity.",
        "causes": "Phytophthora infestans oomycete spores carried over long distances on wind currents in wet, cool, overcast conditions.",
        "treatments": [
            "Apply systemic fungicides (Chlorothalonil, Copper, Mandipropamid, or Cymoxanil) promptly upon detection.",
            "Remove and bag infected plants completely on dry days to avoid spore dispersion.",
            "Never compost infected late blight plant material."
        ],
        "prevention": [
            "Select late blight resistant tomato varieties.",
            "Space plants generously to promote rapid air circulation.",
            "Avoid overhead watering; scout plants daily during periods of extended rainfall or high humidity."
        ]
    },
    "Tomato_Leaf_Mold": {
        "disease": "Leaf Mold",
        "crop": "Tomato",
        "description": "A fungal disease caused by Passalora fulva, frequent in greenhouses, high tunnels, and humid outdoor environments.",
        "symptoms": "Pale green to yellow spots on the upper leaf surface, with olive-green to grayish velvety fungal mold developing directly beneath on the leaf underside.",
        "causes": "Fungus Passalora fulva, thriving in high relative humidity (>85%) and moderate temperatures (21-24°C).",
        "treatments": [
            "Spray with copper fungicides, Chlorothalonil, or bio-fungicides like Trichoderma or Bacillus amyloliquefaciens.",
            "Prune dense inner foliage to lower relative humidity inside the canopy.",
            "In greenhouse/tunnel setups, increase ventilation and exhaust fan speed."
        ],
        "prevention": [
            "Grow leaf mold resistant varieties (hybrids with Cf resistance genes).",
            "Ensure continuous air circulation with fans in enclosed growing structures.",
            "Avoid wetting foliage during morning or evening waterings."
        ]
    },
    "Tomato_Septoria_leaf_spot": {
        "disease": "Septoria Leaf Spot",
        "crop": "Tomato",
        "description": "A destructive foliar fungal disease caused by Septoria lycopersici, resulting in severe lower canopy defoliation and reduced fruit yield.",
        "symptoms": "Numerous small (1.5-3mm), circular spots with gray or tan centers and dark brown margins. Tiny black speckles (pycnidia) are visible in the center of mature spots.",
        "causes": "Fungus Septoria lycopersici overwintering on tomato debris and solanaceous weeds, spread by splashing water droplets.",
        "treatments": [
            "Apply copper fungicides, Chlorothalonil, or Mancozeb every 7-10 days upon symptom onset.",
            "Strip off all affected lower leaves and dispose of them outside the garden.",
            "Apply organic neem oil or sulfur fungicides in rotation."
        ],
        "prevention": [
            "Mulch generously (straw, paper, or plastic) around plants to eliminate soil splash.",
            "Stake and prune tomatoes to maintain excellent air passage.",
            "Practice 2-3 year crop rotation and weed solanaceous wild plants nearby."
        ]
    },
    "Tomato_Spider_mites_Two_spotted_spider_mite": {
        "disease": "Spider Mites",
        "crop": "Tomato",
        "description": "Microscopic sap-feeding arachnids (Tetranychus urticae) that puncture plant cells, causing stippling, chlorosis, and severe yield loss in hot, dry conditions.",
        "symptoms": "Fine yellow or white stippling (tiny speckled dots) on upper leaf surfaces. Leaves turn bronze, dry out, and drop. Fine silky webbing visible on leaf undersides and stem joints.",
        "causes": "Two-spotted spider mites multiplying exponentially in hot (>27°C), dry, and dusty weather.",
        "treatments": [
            "Spray affected leaf undersides thoroughly with insecticidal soap, neem oil, or horticultural oils.",
            "Apply targeted miticides (Bifenazate, Abamectin, or Spiromesifen) if infestation is severe.",
            "Hose down foliage with water to knock mites off and increase local humidity."
        ],
        "prevention": [
            "Introduce natural biological control predators such as Phytoseiulus persimilis predatory mites or lacewings.",
            "Keep plants well-irrigated to reduce drought stress that attracts mites.",
            "Keep garden pathways and surrounding borders moist and dust-free."
        ]
    },
    "Tomato__Target_Spot": {
        "disease": "Target Spot",
        "crop": "Tomato",
        "description": "A fungal disease caused by Corynespora cassiicola attacking leaves, stems, and fruit, forming distinctive zoned necrotic lesions.",
        "symptoms": "Small, pinpoint brown spots that expand into circular brown lesions with distinct concentric rings and chlorotic yellow halos. Fruit may exhibit sunken brown craters.",
        "causes": "Fungus Corynespora cassiicola, thriving in warm (20-28°C), humid, and rainy conditions with prolonged leaf wetness.",
        "treatments": [
            "Apply fungicides with active ingredients like Azoxystrobin, Chlorothalonil, or Pyraclostrobin.",
            "Prune lower infected leaves to prevent upward progression of the fungus.",
            "Clear fallen infected leaves immediately from the soil surface."
        ],
        "prevention": [
            "Improve planting distance and use trellising for optimal air circulation.",
            "Avoid overhead watering; use micro-drip systems.",
            "Rotate crops with non-host plants (avoid planting after cucumber or soybean)."
        ]
    },
    "Tomato__Tomato_YellowLeaf__Curl_Virus": {
        "disease": "Yellow Leaf Curl Virus",
        "crop": "Tomato",
        "description": "A debilitating begomovirus (TYLCV) transmitted by whiteflies that severely stunts tomato growth and suppresses flower and fruit set.",
        "symptoms": "Dramatic upward cupping/curling of leaf margins, severe yellowing (chlorosis) between leaf veins, reduced leaf size, and severe plant stunting with flower drop.",
        "causes": "Tomato Yellow Leaf Curl Virus (TYLCV), transmitted by the silverleaf whitefly (Bemisia tabaci). Not transmitted by seed or mechanical contact.",
        "treatments": [
            "There is no cure once infected. Immediately remove and bag infected plants to protect remaining crops.",
            "Control whitefly populations using insecticidal soap, yellow sticky cards, or systemic insecticides (Imidacloprid, Dinotefuran).",
            "Spray organic neem oil or horticultural mineral oil to disrupt whitefly feeding."
        ],
        "prevention": [
            "Plant TYLCV-resistant tomato cultivars (look for TYLCV resistance coding on seed packets).",
            "Use insect-proof row covers (50-mesh netting) on young plants.",
            "Eradicate alternate weed hosts and clear old tomato residue immediately after harvest."
        ]
    },
    "Tomato__Tomato_mosaic_virus": {
        "disease": "Mosaic Virus",
        "crop": "Tomato",
        "description": "A highly persistent tobamovirus (ToMV) that causes mottled leaf coloring, foliage distortion, and uneven fruit ripening.",
        "symptoms": "Mottled light and dark green patterns ('mosaic') on leaves, leaf distortion, blister-like puckering, strap-like 'shoestring' leaves, and internal brown browning of fruit walls.",
        "causes": "Tomato Mosaic Virus (ToMV), extremely contagious and transmitted mechanically through hands, tools, smoking tobacco residue, and infected seeds.",
        "treatments": [
            "No chemical or biological cure exists. Promptly rogue out and destroy infected plants.",
            "Wash hands thoroughly with soap and water after handling plants.",
            "Disinfect all tools, stakes, and cages in a 10-20% bleach solution or trisodium phosphate."
        ],
        "prevention": [
            "Select ToMV-resistant varieties (labeled with 'T' or 'ToMV').",
            "Do not smoke or use tobacco products near tomato plants.",
            "Use certified virus-free seeds and heat-treat seeds prior to germination."
        ]
    },
    "Tomato_healthy": {
        "disease": "Healthy",
        "crop": "Tomato",
        "description": "The tomato plant exhibits vigorous growth, balanced turgor, deep green leaves, and clean stems with no signs of pathogen damage or pest stress.",
        "symptoms": "Firm, vibrant green foliage with even leaf margins, strong petioles, and healthy flowering clusters.",
        "causes": "Proper soil nutrition, consistent watering, ideal ambient temperature, and effective preventative pest/disease management.",
        "treatments": [
            "No chemical treatment required.",
            "Continue consistent watering and balanced fertilization (higher phosphorus/potassium during fruiting stage)."
        ],
        "prevention": [
            "Maintain mulch layer to prevent soil splash onto lower foliage.",
            "Prune suckers and stake plants to maintain excellent air penetration.",
            "Scout leaf undersides weekly for early signs of mites, aphids, or fungal spores."
        ]
    },

    # ----------------------------------------------------
    # Normalized Aliases for Common Calls
    # ----------------------------------------------------
    "Bell_Pepper_Bacterial_Spot": {
        "disease": "Bacterial Spot",
        "crop": "Bell Pepper",
        "description": "A destructive bacterial disease affecting bell peppers, causing necrotic leaf spotting, defoliation, and fruit damage.",
        "symptoms": "Small, dark brown, water-soaked circular to irregular lesions with yellow halos on leaves.",
        "causes": "Bacterium Xanthomonas campestris pv. vesicatoria, spread by rain splash and overhead watering.",
        "treatments": [
            "Apply copper-based bactericide sprays combined with Mancozeb.",
            "Remove and destroy heavily infected plant debris.",
            "Avoid handling plants when foliage is wet."
        ],
        "prevention": [
            "Plant certified disease-free and resistant bell pepper varieties.",
            "Use drip irrigation to keep foliage dry.",
            "Practice 2-3 year crop rotation away from solanaceous crops."
        ]
    },
    "Bell_Pepper_Healthy": {
        "disease": "Healthy",
        "crop": "Bell Pepper",
        "description": "The bell pepper plant exhibits vibrant, uniform green foliage with no detectable pathogen lesions or pest stress.",
        "symptoms": "Firm, glossy leaves with consistent green coloration and normal venation.",
        "causes": "Optimal ambient conditions, adequate soil moisture, and balanced nutrient availability.",
        "treatments": [
            "No chemical treatment needed.",
            "Maintain regular watering and standard balanced NPK fertilization."
        ],
        "prevention": [
            "Inspect regularly for aphids, thrips, and mites.",
            "Ensure proper plant spacing for canopy airflow."
        ]
    },
    "Potato_Early_Blight": {
        "disease": "Early Blight",
        "crop": "Potato",
        "description": "A widespread fungal disease caused by Alternaria solani affecting potato foliage, stems, and tubers.",
        "symptoms": "Dark brown to black concentric circular rings ('target board' pattern) on older lower leaves.",
        "causes": "Fungus Alternaria solani, surviving in infected crop residue.",
        "treatments": [
            "Apply protective fungicides such as Chlorothalonil, Mancozeb, or copper hydroxide.",
            "Prune infected lower foliage to reduce fungal spore count."
        ],
        "prevention": [
            "Practice a 3-year crop rotation with non-solanaceous crops.",
            "Avoid overhead irrigation; water at the soil base."
        ]
    },
    "Potato_Late_Blight": {
        "disease": "Late Blight",
        "crop": "Potato",
        "description": "A devastating oomycete infection (Phytophthora infestans) that can rapidly destroy entire potato canopies.",
        "symptoms": "Water-soaked, dark brown to purplish-black lesions on leaves and stems with white fungal-like fuzz.",
        "causes": "Pathogen Phytophthora infestans, spreading rapidly through wind-borne sporangia during cool, wet weather.",
        "treatments": [
            "Apply targeted systemic and contact fungicides (Metalaxyl, Mancozeb) immediately.",
            "Rogue out and destroy infected vines immediately."
        ],
        "prevention": [
            "Plant only certified disease-free seed tubers.",
            "Ensure wide row spacing and good air drainage."
        ]
    },
    "Potato_Healthy": {
        "disease": "Healthy",
        "crop": "Potato",
        "description": "The potato vine demonstrates vigorous vegetative growth with deep green leaves and healthy turgor.",
        "symptoms": "Lush green foliage, normal leaf morphology, and absence of target spots.",
        "causes": "Favorable soil temperatures, balanced moisture, and disease-free seed tubers.",
        "treatments": [
            "No chemical treatment needed.",
            "Continue balanced fertilization and hilling practices."
        ],
        "prevention": [
            "Scout fields twice weekly during cool, moist weather.",
            "Hill soil properly around developing tubers."
        ]
    },
    "Tomato_Yellow_Leaf_Curl": {
        "disease": "Yellow Leaf Curl Virus",
        "crop": "Tomato",
        "description": "A debilitating begomovirus (TYLCV) transmitted by whiteflies that severely stunts tomato growth.",
        "symptoms": "Upward curling of leaf margins, severe yellowing between veins, and stunted growth.",
        "causes": "Tomato Yellow Leaf Curl Virus (TYLCV), transmitted by whiteflies.",
        "treatments": [
            "Remove and bag infected plants immediately.",
            "Control whitefly populations using insecticidal soap or neem oil."
        ],
        "prevention": [
            "Plant TYLCV-resistant cultivars.",
            "Use insect-proof netting over young crops."
        ]
    },
    "Tomato_Mosaic_Virus": {
        "disease": "Mosaic Virus",
        "crop": "Tomato",
        "description": "A persistent tobamovirus (ToMV) causing mottled leaf coloration and foliage distortion.",
        "symptoms": "Mottled light and dark green patterns ('mosaic') on leaves, with blistering and stunting.",
        "causes": "Tomato Mosaic Virus (ToMV), transmitted mechanically via hands, tools, and seeds.",
        "treatments": [
            "Rogue out and destroy infected plants promptly.",
            "Disinfect tools and wash hands thoroughly."
        ],
        "prevention": [
            "Select ToMV-resistant varieties.",
            "Avoid using tobacco products near tomato crops."
        ]
    },
    "Tomato_Spider_Mites": {
        "disease": "Spider Mites",
        "crop": "Tomato",
        "description": "Sap-feeding arachnids (Tetranychus urticae) causing leaf stippling and bronzing in hot, dry conditions.",
        "symptoms": "Fine yellow/white stippling on upper leaves, bronzing, and delicate silk webbing on undersides.",
        "causes": "Two-spotted spider mites thriving in hot, dry, dusty environments.",
        "treatments": [
            "Spray leaf undersides thoroughly with insecticidal soap or neem oil.",
            "Apply miticide if infestation is severe."
        ],
        "prevention": [
            "Introduce predatory mites.",
            "Keep plants well-irrigated to alleviate drought stress."
        ]
    },
    "Tomato_Healthy": {
        "disease": "Healthy",
        "crop": "Tomato",
        "description": "The tomato plant exhibits vigorous growth, deep green leaves, and clean stems with no disease symptoms.",
        "symptoms": "Firm, vibrant green foliage with even leaf margins and healthy flowering clusters.",
        "causes": "Proper soil nutrition, consistent watering, and preventative pest management.",
        "treatments": [
            "No chemical treatment required.",
            "Continue consistent watering and balanced fertilization."
        ],
        "prevention": [
            "Maintain mulch to prevent soil splash.",
            "Prune suckers and stake plants to maintain airflow."
        ]
    }
}

import re

def get_recommendation(class_name):
    """
    Returns disease description, symptoms, cause, treatments, and prevention tips.
    If the class is a known 'Healthy' class, it returns customized health details.
    Uses fallback logic for classes not explicitly in the dictionary.
    """
    if not class_name:
        class_name = "Unknown"

    # 1. Exact match in dictionary
    if class_name in DISEASE_DATA:
        return DISEASE_DATA[class_name]

    # 2. Normalized underscore match (e.g. Pepper__bell___healthy -> Pepper_bell_healthy)
    norm_key = re.sub(r'_+', '_', class_name).strip('_')
    if norm_key in DISEASE_DATA:
        return DISEASE_DATA[norm_key]

    # 3. Case-insensitive & space/underscore insensitive lookup
    cleaned_lookup = class_name.lower().replace(" ", "_").replace("-", "_")
    cleaned_lookup = re.sub(r'_+', '_', cleaned_lookup).strip('_')
    for k, v in DISEASE_DATA.items():
        k_clean = re.sub(r'_+', '_', k.lower().replace(" ", "_").replace("-", "_")).strip('_')
        if k_clean == cleaned_lookup:
            return v

    # 4. Handle any healthy classes
    if "healthy" in class_name.lower():
        parts = re.sub(r'_+', '_', class_name).strip('_').split("_")
        crop = parts[0].title() if len(parts) > 0 else "Crop"
        if "bell" in class_name.lower() or "pepper" in class_name.lower():
            crop = "Bell Pepper"
        return {
            "disease": "Healthy",
            "crop": crop,
            "description": f"The {crop} leaf appears healthy with no visible signs of disease or pest damage.",
            "symptoms": "Green, uniform color, strong structure, and normal development appropriate for the growth stage.",
            "causes": "Optimal environmental conditions, adequate nutrient availability, and effective pest management.",
            "treatments": [
                "No treatment necessary.",
                "Continue standard watering and fertilization schedule."
            ],
            "prevention": [
                "Maintain good field sanitation.",
                "Inspect crops regularly for early signs of pests or disease.",
                "Apply balanced fertilizers and irrigate properly at root level."
            ]
        }

    # 5. General fallback parser for unseen classes
    parts = re.sub(r'_+', '_', class_name).strip('_').split("_")
    crop = parts[0].title() if len(parts) > 0 else "Crop"
    disease_words = parts[1:] if len(parts) > 1 else ["Disease"]
    disease = " ".join(disease_words).replace("_", " ").strip().title()
    disease_lower = disease.lower()

    if "blight" in disease_lower:
        desc = f"A type of plant disease caused by pathogenic organisms resulting in rapid chlorosis, browning, and tissue death."
        symp = "Dark, water-soaked spots on leaves or stems that expand rapidly and can kill the entire leaf or plant."
        cause = "Fungal or bacterial pathogens, often spread by splashing water or wind during wet conditions."
        treats = ["Apply appropriate copper-based or synthetic fungicides/bactericides.", "Prune and destroy infected plant parts."]
        prevs = ["Keep foliage dry, water at the soil level.", "Space plants for proper air circulation.", "Rotate crops yearly."]
    elif "rust" in disease_lower:
        desc = f"A fungal disease that affects plants, characterized by rusty or reddish-brown powdery spores on leaves and stems."
        symp = "Orange, yellow, or reddish-brown powdery pustules or spots, usually on the underside of leaves."
        cause = "Rust fungi spreading easily through wind-borne spores."
        treats = ["Apply sulfur or copper fungicides.", "Remove heavily infected leaves to limit spore spread."]
        prevs = ["Plant resistant crop varieties.", "Avoid overhead irrigation.", "Remove weed hosts near the crop."]
    elif "rot" in disease_lower:
        desc = f"A condition characterized by decay of plant tissue, usually caused by fungal or bacterial infection."
        symp = "Soft, mushy, discolored areas on leaves, stems, or fruit, often accompanied by an unpleasant odor."
        cause = "Soil-borne fungi or bacteria, usually thriving in overly wet or poorly drained soils."
        treats = ["Apply specialized fungicides.", "Improve drainage and reduce watering immediately.", "Remove decaying plant parts."]
        prevs = ["Avoid overwatering and ensure excellent soil drainage.", "Use clean seeds and planting materials.", "Rotate crops."]
    elif "spot" in disease_lower or "smut" in disease_lower:
        desc = f"A common plant disease that causes localized lesions on leaves, stems, or fruits, reducing photosynthesis."
        symp = "Small, dark spots on leaves, sometimes with a yellow halo or concentric rings."
        cause = "Fungi, bacteria, or other pathogens spreading via wind, rain, or tools."
        treats = ["Apply copper-based fungicides or bio-fungicides.", "Prune lower leaves to reduce soil splash."]
        prevs = ["Provide adequate spacing for airflow.", "Avoid watering foliage in the evening.", "Clean tools regularly."]
    elif "virus" in disease_lower or "curl" in disease_lower or "mosaic" in disease_lower:
        desc = f"A viral disease that disrupts the plant's normal growth, chlorophyll production, and development."
        symp = "Mottled yellow and green leaves, curling, stunting, distorted growth, or deformed fruit."
        cause = "Plant viruses, commonly transmitted by insect vectors like aphids, whiteflies, or thrips."
        treats = ["Immediately remove and destroy infected plants (no chemical cure exists).", "Control insect vectors using insecticidal soaps or neem oil."]
        prevs = ["Use certified virus-free seeds.", "Install insect-proof netting.", "Keep the area weed-free to eliminate alternate hosts."]
    elif "mite" in disease_lower or "pest" in disease_lower:
        desc = f"An infestation of tiny arachnids or insects that feed on the sap of the plant, causing stress and damage."
        symp = "Fine webbing on the undersides of leaves, stippling (tiny yellow dots) on upper surfaces, and bronzing of leaves."
        cause = "Spider mites or other sap-sucking pests, often thriving in hot, dry conditions."
        treats = ["Spray with insecticidal soap, neem oil, or miticides.", "Wash plants with a strong stream of water to dislodge pests."]
        prevs = ["Keep plants well-watered (stressed plants are more susceptible).", "Introduce natural predators like ladybugs or predatory mites."]
    else:
        desc = f"A disease affecting {crop} plants, leading to reduced health and yield."
        symp = "Discoloration, spots, or abnormal growth on the leaves."
        cause = "Pathogenic infection (fungus, bacteria, or virus)."
        treats = ["Identify the specific pathogen for targeted treatment.", "Apply general broad-spectrum copper fungicide."]
        prevs = ["Practice crop rotation.", "Maintain field hygiene.", "Avoid overhead irrigation."]

    return {
        "disease": disease,
        "crop": crop,
        "description": desc,
        "symptoms": symp,
        "causes": cause,
        "treatments": treats,
        "prevention": prevs
    }
