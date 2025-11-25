"""
Plant Care Tips Generator
Generates contextual care tips based on plant condition and history
"""

class TipGenerator:
    """
    Generate contextualized plant care tips
    """
    
    GENERAL_TIPS = {
        'watering': [
            'Water early in the morning to reduce evaporation',
            'Check soil moisture 2-3 inches deep before watering',
            'Water at the base, not on leaves',
            'Ensure pots have drainage holes',
            'Water until it drains from bottom'
        ],
        'fertilizing': [
            'Use balanced fertilizer (NPK 10-10-10)',
            'Feed during growing season every 2-4 weeks',
            'Dilute liquid fertilizers to half strength',
            'Never fertilize dry soil',
            'Organic compost is great alternative'
        ],
        'light': [
            'Rotate plant every week for even growth',
            'Clean leaves regularly to maximize light absorption',
            'Use grow lights for low-light conditions',
            'Afternoon shade helps in hot climates',
            'Morning sun is ideal for most plants'
        ],
        'pruning': [
            'Prune dead leaves and branches regularly',
            'Use sterilized tools to prevent disease',
            'Prune in spring for most plants',
            'Remove flowers as they fade to encourage more',
            'Cut above leaf nodes at 45-degree angle'
        ],
        'humidity': [
            'Mist leaves if air is very dry',
            'Group plants together to increase humidity',
            'Use pebble trays filled with water',
            'Avoid cold drafts and heat vents',
            'Place on humid areas like bathrooms'
        ]
    }
    
    DISEASE_PREVENTION = [
        'Inspect plants regularly for early signs',
        'Remove affected leaves immediately',
        'Improve air circulation around plants',
        'Avoid overhead watering',
        'Keep tools and pots clean',
        'Isolate new/sick plants from others',
        'Don\'t reuse soil from diseased plants'
    ]
    
    @staticmethod
    def get_seasonal_tips(season):
        """Get tips for specific season"""
        tips = {
            'spring': [
                'Resume fertilizing as growth starts',
                'Repot plants if needed',
                'Increase watering frequency',
                'Prune to shape plants',
                'Watch for new pests'
            ],
            'summer': [
                'Water more frequently',
                'Provide afternoon shade for heat-sensitive plants',
                'Monitor for heat stress',
                'Fertilize regularly',
                'Ensure good air circulation'
            ],
            'fall': [
                'Reduce fertilizing frequency',
                'Prepare for dormancy',
                'Water less frequently',
                'Monitor temperature changes',
                'Clear fallen leaves'
            ],
            'winter': [
                'Reduce watering significantly',
                'Minimize fertilizing',
                'Protect from cold drafts',
                'Reduce misting',
                'Provide supplemental light if needed'
            ]
        }
        return tips.get(season.lower(), [])
    
    @staticmethod
    def get_companion_plants():
        """Get companion planting suggestions"""
        return {
            'tomato': ['basil', 'carrot', 'marigold'],
            'lettuce': ['radish', 'strawberry', 'beet'],
            'basil': ['tomato', 'pepper', 'oregano'],
            'pepper': ['onion', 'spinach', 'basil'],
            'rose': ['lavender', 'thyme', 'rosemary']
        }


# Quick reference guide
PLANT_CARE_QUICK_REFERENCE = {
    'overwatering': {
        'signs': ['Yellow leaves', 'Soft stems', 'Foul soil smell', 'Root rot'],
        'fix': [
            'Stop watering immediately',
            'Improve drainage',
            'Repot in fresh soil',
            'Increase air circulation'
        ]
    },
    'underwatering': {
        'signs': ['Dry, brittle leaves', 'Wilting', 'Slow growth', 'Leaf drop'],
        'fix': [
            'Water thoroughly',
            'Establish consistent watering schedule',
            'Mulch soil surface',
            'Increase humidity'
        ]
    },
    'low_light': {
        'signs': ['Pale leaves', 'Leggy growth', 'No flowering', 'Slow growth'],
        'fix': [
            'Move to brighter location',
            'Use grow lights',
            'Prune competing plants',
            'Clean leaves for max absorption'
        ]
    },
    'pest_infestation': {
        'signs': ['Sticky residue', 'Holes in leaves', 'Webbing', 'Insects visible'],
        'fix': [
            'Isolate plant',
            'Spray with neem oil',
            'Remove affected leaves',
            'Repeat treatment weekly'
        ]
    }
}

print("✅ Tip Generator loaded")
print(f"Categories: {list(TipGenerator.GENERAL_TIPS.keys())}")
