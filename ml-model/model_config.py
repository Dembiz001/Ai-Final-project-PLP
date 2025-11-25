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

# Plant care information
PLANT_LIBRARY = {
    "tomato": {
        "name": "Tomato",
        "watering": "1 inch per week, more during fruiting",
        "light": "6-8 hours of direct sunlight",
        "temp": "65-75°F (18-24°C)",
        "soil": "Rich, well-draining loam",
        "common_issues": ["fungal_disease", "pest_damage", "water_stress"]
    },
    "lettuce": {
        "name": "Lettuce",
        "watering": "Keep soil consistently moist",
        "light": "4-6 hours of sunlight (less in summer)",
        "temp": "60-70°F (15-21°C)",
        "soil": "Light, well-draining loam",
        "common_issues": ["bacterial_disease", "pest_damage"]
    },
    "rose": {
        "name": "Rose",
        "watering": "1-2 inches per week",
        "light": "6-8 hours of direct sunlight",
        "temp": "65-75°F (18-24°C)",
        "soil": "Well-draining, slightly acidic",
        "common_issues": ["fungal_disease", "pest_damage", "nutrient_deficiency"]
    },
    "basil": {
        "name": "Basil",
        "watering": "Keep soil moist but not soggy",
        "light": "6-8 hours of sunlight",
        "temp": "70-85°F (21-29°C)",
        "soil": "Rich, well-draining",
        "common_issues": ["pest_damage", "water_stress"]
    },
    "pepper": {
        "name": "Pepper",
        "watering": "1-2 inches per week",
        "light": "6-8 hours of direct sunlight",
        "temp": "70-85°F (21-29°C)",
        "soil": "Rich, well-draining",
        "common_issues": ["fungal_disease", "pest_damage", "nutrient_deficiency"]
    }
}

MODEL_CONFIG = {
    "image_size": (224, 224),
    "batch_size": 32,
    "model_type": "MobileNetV2",
    "weights": "imagenet",
    "num_classes": 7
}
