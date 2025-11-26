"""
ML Model Configuration for AI Gardening Assistant
"""

PLANT_CLASSES = {
    0: "healthy",
    1: "fungal_disease",
    2: "bacterial_disease",
    3: "viral_disease",
    4: "pest_damage",
    5: "nutrient_deficiency",
    6: "water_stress"
}

RECOMMENDATIONS = {
    "healthy": {
        "title": "Your plant looks healthy!",
        "description": "Your plant appears to be in great condition.",
        "actions": [
            "Continue regular watering schedule",
            "Maintain current light conditions",
            "Monitor for any changes in leaf color"
        ]
    },
    "fungal_disease": {
        "title": "Fungal Disease Detected",
        "description": "Your plant shows signs of fungal infection.",
        "actions": [
            "Remove affected leaves",
            "Improve air circulation around the plant",
            "Apply fungicide (neem oil or sulfur spray)",
            "Reduce watering frequency",
            "Ensure soil is not waterlogged"
        ]
    },
    "bacterial_disease": {
        "title": "Bacterial Infection Detected",
        "description": "Your plant may have a bacterial infection.",
        "actions": [
            "Remove infected leaves and dispose of them",
            "Use sterilized tools for pruning",
            "Improve air circulation",
            "Apply copper-based fungicide",
            "Avoid overhead watering"
        ]
    },
    "viral_disease": {
        "title": "Viral Infection Suspected",
        "description": "Your plant shows symptoms of viral infection.",
        "actions": [
            "Isolate the plant from others",
            "Remove severely affected leaves",
            "Control insect vectors (aphids, whiteflies)",
            "No chemical cure exists - focus on plant care",
            "Consider replacing if infection is severe"
        ]
    },
    "pest_damage": {
        "title": "Pest Damage Detected",
        "description": "Your plant shows signs of pest damage.",
        "actions": [
            "Inspect plant for visible pests",
            "Apply insecticidal soap or neem oil",
            "Use natural predators (ladybugs, parasitic wasps)",
            "Increase humidity to deter spider mites",
            "Isolate plant to prevent pest spread"
        ]
    },
    "nutrient_deficiency": {
        "title": "Nutrient Deficiency",
        "description": "Your plant may lack essential nutrients.",
        "actions": [
            "Apply balanced fertilizer (NPK 10-10-10)",
            "Consider soil test to identify missing nutrients",
            "Water regularly to help nutrient uptake",
            "Add compost or organic matter to soil",
            "Feed every 2-4 weeks during growing season"
        ]
    },
    "water_stress": {
        "title": "Water Stress Detected",
        "description": "Your plant shows signs of watering issues.",
        "actions": [
            "Check soil moisture at 2-3 inches depth",
            "Adjust watering schedule if over/underwatering",
            "Ensure pot has drainage holes",
            "Water until it drains from bottom",
            "Repot if roots are bound or soil is compacted"
        ]
    }
}

# Plant care information - 30 West African crops + vegetables
PLANT_LIBRARY = {
    "okra": {
        "name": "Okra",
        "watering": "1-1.5 inches per week, frequent in dry season",
        "light": "6-8 hours of direct sunlight (loves heat)",
        "temp": "75-90°F (24-32°C)",
        "soil": "Well-draining loamy soil, tolerates poor soil",
        "common_issues": ["pest_damage", "fungal_disease", "water_stress"],
        "harvest": "50-60 days from planting"
    },
    "sorrel": {
        "name": "Sorrel (Roselle)",
        "watering": "Moderate, 1 inch per week",
        "light": "6-8 hours of direct sunlight",
        "temp": "70-85°F (21-29°C)",
        "soil": "Well-draining, slightly acidic soil",
        "common_issues": ["pest_damage", "fungal_disease"],
        "harvest": "90-120 days from planting"
    },
    "onion": {
        "name": "Onion",
        "watering": "1-1.5 inches per week, reduce after bulbing",
        "light": "6-8 hours of direct sunlight",
        "temp": "60-75°F (15-24°C)",
        "soil": "Rich, well-draining loamy soil",
        "common_issues": ["pest_damage", "fungal_disease", "nutrient_deficiency"],
        "harvest": "100-120 days from planting"
    },
    "watermelon": {
        "name": "Watermelon",
        "watering": "1.5-2 inches per week, consistent moisture",
        "light": "8+ hours of direct sunlight",
        "temp": "75-95°F (24-35°C)",
        "soil": "Sandy loam, well-draining",
        "common_issues": ["pest_damage", "fungal_disease", "water_stress"],
        "harvest": "70-100 days from planting"
    },
    "melon": {
        "name": "Melon (Cantaloupe)",
        "watering": "1.5 inches per week, reduce after fruit set",
        "light": "8+ hours of direct sunlight",
        "temp": "75-95°F (24-35°C)",
        "soil": "Sandy loam with organic matter",
        "common_issues": ["pest_damage", "fungal_disease"],
        "harvest": "70-90 days from planting"
    },
    "pumpkin": {
        "name": "Pumpkin/Squash",
        "watering": "1-2 inches per week",
        "light": "6-8 hours of direct sunlight",
        "temp": "70-85°F (21-29°C)",
        "soil": "Rich, well-composted soil",
        "common_issues": ["pest_damage", "fungal_disease", "nutrient_deficiency"],
        "harvest": "90-120 days from planting"
    },
    "carrot": {
        "name": "Carrot",
        "watering": "1 inch per week, consistent moisture",
        "light": "5-6 hours of sunlight (tolerates partial shade)",
        "temp": "60-70°F (15-21°C)",
        "soil": "Loose, well-draining, sandy loam",
        "common_issues": ["pest_damage", "fungal_disease"],
        "harvest": "60-80 days from planting"
    },
    "spinach": {
        "name": "Spinach",
        "watering": "Keep soil consistently moist",
        "light": "4-5 hours of sunlight (prefers cooler)",
        "temp": "50-70°F (10-21°C)",
        "soil": "Rich, well-draining loam",
        "common_issues": ["bacterial_disease", "pest_damage"],
        "harvest": "40-50 days from planting"
    },
    "cabbage": {
        "name": "Cabbage",
        "watering": "1.5-2 inches per week, consistent",
        "light": "6-8 hours of sunlight",
        "temp": "60-70°F (15-21°C)",
        "soil": "Rich, well-draining soil, high nitrogen",
        "common_issues": ["pest_damage", "fungal_disease", "bacterial_disease"],
        "harvest": "70-100 days from planting"
    },
    "eggplant": {
        "name": "Eggplant",
        "watering": "1-1.5 inches per week, consistent",
        "light": "8+ hours of direct sunlight",
        "temp": "75-85°F (24-29°C)",
        "soil": "Rich, well-draining loam",
        "common_issues": ["pest_damage", "fungal_disease", "nutrient_deficiency"],
        "harvest": "60-90 days from planting"
    },
    "cucumber": {
        "name": "Cucumber",
        "watering": "1-1.5 inches per week, consistent moisture",
        "light": "6-8 hours of direct sunlight",
        "temp": "70-95°F (21-35°C)",
        "soil": "Rich, well-draining loam with compost",
        "common_issues": ["pest_damage", "fungal_disease", "water_stress"],
        "harvest": "50-70 days from planting"
    },
    "beans": {
        "name": "Beans (Black-eyed peas)",
        "watering": "1 inch per week, more during pod development",
        "light": "6-8 hours of direct sunlight",
        "temp": "70-85°F (21-29°C)",
        "soil": "Well-draining loam, fixes nitrogen",
        "common_issues": ["pest_damage", "fungal_disease"],
        "harvest": "50-70 days from planting"
    },
    "maize": {
        "name": "Maize (Corn)",
        "watering": "1-1.5 inches per week, critical during tasseling",
        "light": "8+ hours of direct sunlight",
        "temp": "75-86°F (24-30°C)",
        "soil": "Rich, well-draining loam, high nitrogen",
        "common_issues": ["pest_damage", "fungal_disease", "nutrient_deficiency"],
        "harvest": "70-100 days from planting"
    },
    "groundnut": {
        "name": "Groundnut (Peanut)",
        "watering": "1-1.5 inches per week",
        "light": "8+ hours of direct sunlight",
        "temp": "75-85°F (24-29°C)",
        "soil": "Well-draining sandy loam",
        "common_issues": ["pest_damage", "fungal_disease", "water_stress"],
        "harvest": "90-150 days from planting"
    },
    "cassava": {
        "name": "Cassava",
        "watering": "Drought tolerant, water during dry spells",
        "light": "6-8 hours of sunlight",
        "temp": "75-86°F (24-30°C)",
        "soil": "Well-draining, tolerates poor soil",
        "common_issues": ["pest_damage", "fungal_disease"],
        "harvest": "12-24 months from planting"
    },
    "yam": {
        "name": "Yam",
        "watering": "1-1.5 inches per week, more at tuber formation",
        "light": "6-8 hours of sunlight",
        "temp": "75-86°F (24-30°C)",
        "soil": "Rich, well-draining, well-composted",
        "common_issues": ["pest_damage", "fungal_disease", "water_stress"],
        "harvest": "150-200 days from planting"
    },
    "calaloo": {
        "name": "Calaloo (Amaranth)",
        "watering": "Keep soil consistently moist",
        "light": "6-8 hours of sunlight",
        "temp": "70-85°F (21-29°C)",
        "soil": "Rich, well-draining loam",
        "common_issues": ["pest_damage", "fungal_disease"],
        "harvest": "50-60 days from planting"
    },
    "moringa": {
        "name": "Moringa",
        "watering": "Drought tolerant, minimal watering once established",
        "light": "8+ hours of direct sunlight",
        "temp": "77-86°F (25-30°C)",
        "soil": "Well-draining, tolerates poor soil",
        "common_issues": ["pest_damage"],
        "harvest": "40-60 days for leaves"
    },
    "ginger": {
        "name": "Ginger",
        "watering": "1-1.5 inches per week, reduce in dry season",
        "light": "Partial shade (4-5 hours)",
        "temp": "75-86°F (24-30°C)",
        "soil": "Rich, well-draining with organic matter",
        "common_issues": ["fungal_disease", "pest_damage"],
        "harvest": "8-10 months from planting"
    },
    "chili_pepper": {
        "name": "Chili Pepper",
        "watering": "1-1.5 inches per week",
        "light": "8+ hours of direct sunlight",
        "temp": "75-90°F (24-32°C)",
        "soil": "Rich, well-draining loam",
        "common_issues": ["pest_damage", "fungal_disease", "water_stress"],
        "harvest": "60-90 days from planting"
    },
    "sesame": {
        "name": "Sesame",
        "watering": "1 inch per week, drought tolerant",
        "light": "8+ hours of direct sunlight",
        "temp": "75-95°F (24-35°C)",
        "soil": "Well-draining loam",
        "common_issues": ["pest_damage", "fungal_disease"],
        "harvest": "90-120 days from planting"
    },
    "sorghum": {
        "name": "Sorghum",
        "watering": "Drought tolerant, 1 inch per week during growth",
        "light": "8+ hours of direct sunlight",
        "temp": "75-95°F (24-35°C)",
        "soil": "Well-draining, tolerates poor soil",
        "common_issues": ["pest_damage", "fungal_disease"],
        "harvest": "80-120 days from planting"
    },
    "millet": {
        "name": "Millet",
        "watering": "Drought tolerant, minimal watering",
        "light": "8+ hours of direct sunlight",
        "temp": "75-95°F (24-35°C)",
        "soil": "Well-draining, tolerates sandy soil",
        "common_issues": ["pest_damage"],
        "harvest": "60-90 days from planting"
    },
    "coconut": {
        "name": "Coconut",
        "watering": "Deep watering 2-3 times per week when young",
        "light": "8+ hours of direct sunlight",
        "temp": "75-95°F (24-35°C)",
        "soil": "Well-draining sandy soil",
        "common_issues": ["pest_damage", "fungal_disease"],
        "harvest": "2-3 years to first harvest"
    },
    "banana": {
        "name": "Banana",
        "watering": "Consistent moisture, 1.5-2 inches per week",
        "light": "6-8 hours of sunlight, shade tolerant",
        "temp": "78-86°F (26-30°C)",
        "soil": "Rich, well-draining with organic matter",
        "common_issues": ["fungal_disease", "pest_damage", "water_stress"],
        "harvest": "9-12 months from planting"
    },
    "plantain": {
        "name": "Plantain",
        "watering": "1.5-2 inches per week, consistent",
        "light": "6-8 hours of sunlight",
        "temp": "78-86°F (26-30°C)",
        "soil": "Rich, well-draining loam",
        "common_issues": ["fungal_disease", "pest_damage"],
        "harvest": "9-12 months from planting"
    },
    "mango": {
        "name": "Mango",
        "watering": "Deep watering, 1-2 inches per week",
        "light": "8+ hours of direct sunlight",
        "temp": "75-90°F (24-32°C)",
        "soil": "Well-draining loam with organic matter",
        "common_issues": ["fungal_disease", "pest_damage"],
        "harvest": "3-5 years to first harvest"
    },
    "guava": {
        "name": "Guava",
        "watering": "1 inch per week, tolerates drought",
        "light": "8+ hours of direct sunlight",
        "temp": "68-86°F (20-30°C)",
        "soil": "Well-draining, tolerates poor soil",
        "common_issues": ["pest_damage", "fungal_disease"],
        "harvest": "2-3 years to first harvest"
    },
    "pawpaw": {
        "name": "Pawpaw (Papaya)",
        "watering": "1.5 inches per week, reduce after flowering",
        "light": "8+ hours of direct sunlight",
        "temp": "75-95°F (24-35°C)",
        "soil": "Well-draining sandy loam",
        "common_issues": ["fungal_disease", "pest_damage", "water_stress"],
        "harvest": "9-12 months from planting"
    },
    "pineapple": {
        "name": "Pineapple",
        "watering": "1-1.5 inches per week, drought tolerant",
        "light": "6-8 hours of sunlight",
        "temp": "70-85°F (21-29°C)",
        "soil": "Well-draining sandy loam",
        "common_issues": ["pest_damage", "fungal_disease"],
        "harvest": "18-24 months from planting"
    }
}

MODEL_CONFIG = {
    "image_size": (224, 224),
    "batch_size": 32,
    "model_type": "MobileNetV2",
    "weights": "imagenet",
    "num_classes": 7
}
