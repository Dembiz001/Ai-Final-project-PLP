"""
Gardening Chatbot Knowledge Base
Expert answers to common gardening questions
"""

GARDENING_FAQs = {
    "watering": {
        "question": "How often should I water my plants?",
        "answer": "Most vegetables need 1-1.5 inches of water per week. Check soil moisture 2-3 inches deep—if it's dry, water. During rainy season, reduce frequency. Early morning watering is best to reduce disease."
    },
    "soil": {
        "question": "What's the best soil for growing vegetables?",
        "answer": "Use well-draining loam soil with organic matter (compost). Good soil should: (1) drain water, (2) retain moisture, (3) have high organic content, (4) have balanced pH. Test soil annually."
    },
    "fertilizer": {
        "question": "When and how should I fertilize?",
        "answer": "Apply balanced fertilizer (NPK 10-10-10) every 2-4 weeks during growing season. Organic options: compost, manure, bone meal. Start light—excess nitrogen causes leaves but fewer fruits."
    },
    "pest_control": {
        "question": "How do I manage pests naturally?",
        "answer": "Best practices: (1) Inspect plants weekly, (2) Remove infected leaves, (3) Spray neem oil or insecticidal soap, (4) Use row covers on young plants, (5) Introduce natural predators (ladybugs), (6) Rotate crops."
    },
    "disease": {
        "question": "How do I prevent plant diseases?",
        "answer": "Prevention is key: (1) Avoid overhead watering, (2) Space plants for air circulation, (3) Remove dead leaves, (4) Sterilize tools, (5) Don't reuse diseased soil, (6) Rotate crops yearly."
    },
    "sunlight": {
        "question": "How much sunlight do vegetables need?",
        "answer": "Most vegetables need 6-8 hours of direct sunlight. Leafy greens tolerate 4-5 hours. Shade-loving: spinach, lettuce. Sun-lovers: tomato, peppers, eggplant. Hot climates: afternoon shade helps."
    },
    "temperature": {
        "question": "What temperature is best for gardening?",
        "answer": "Most vegetables grow best at 70-85°F (21-29°C). Cool-season: lettuce, spinach at 60-70°F. Warm-season: okra, watermelon at 75-95°F. Plant timing matters—know your local frost dates."
    },
    "season": {
        "question": "When should I plant in West Africa?",
        "answer": "Dry Season (Nov-Mar): best for most vegetables. Rainy Season (Apr-Oct): okra, cucumbers, beans thrive. Key: Start before heavy rains, use mulch to retain moisture, water during dry spells."
    },
    "composting": {
        "question": "How do I make compost?",
        "answer": "Layer: (1) Green waste (grass, leaves) 50%, (2) Brown waste (wood, straw) 50%. Add water, turn weekly. Ready in 2-3 months. Use aged compost (dark, crumbly) in soil to improve fertility and drainage."
    },
    "germination": {
        "question": "How do I start seeds successfully?",
        "answer": "Use seed trays with moist potting mix. Keep at 70-80°F. Provide bright light once sprouted. Harden off seedlings (expose gradually to sun) before transplanting. Direct seeding works for beans, maize, cassava."
    },
    "spacing": {
        "question": "How far apart should I plant?",
        "answer": "Proper spacing prevents disease and competition. Examples: tomato 24-36\", okra 12-18\", beans 4-6\", carrots 2-3\", cabbage 18-24\". Crowding reduces yield and invites pests."
    },
    "mulch": {
        "question": "Why should I use mulch?",
        "answer": "Mulch (straw, leaves, grass): (1) Retains soil moisture, (2) Keeps soil cool, (3) Prevents weeds, (4) Enriches soil as it decays, (5) Reduces watering frequency—use 2-3 inch layer."
    },
    "weeding": {
        "question": "How do I manage weeds?",
        "answer": "Weed early and often. Remove when small to prevent seed spread. Mulch to suppress weeds. Hand-pull or hoe. Avoid herbicides in food gardens. Regular weeding saves time later."
    },
    "harvesting": {
        "question": "When and how do I harvest?",
        "answer": "Harvest in early morning for best quality. Okra: pick young/tender (3-4 days growth). Carrots/onions: when mature. Leafy greens: outer leaves first. Handle gently to avoid bruising."
    },
    "crop_rotation": {
        "question": "What is crop rotation and why?",
        "answer": "Rotate crop families yearly: (1) Reduces pest/disease buildup, (2) Balances soil nutrients, (3) Improves soil health. Example: tomato → beans (fixes nitrogen) → leafy greens."
    },
    "organic": {
        "question": "How do I garden organically?",
        "answer": "Organic farming: (1) No synthetic chemicals, (2) Use compost/manure, (3) Companion planting, (4) Natural pest control, (5) Crop rotation, (6) Mulching. Healthier soil = healthier plants."
    },
    "water_conservation": {
        "question": "How can I save water in the garden?",
        "answer": "Water-saving tips: (1) Mulch heavily, (2) Water early morning/evening, (3) Drip irrigation (best), (4) Water soil not leaves, (5) Group plants by water needs, (6) Choose drought-tolerant crops."
    },
    "yield": {
        "question": "How can I increase my harvest?",
        "answer": "Maximize yield: (1) Good soil + regular fertilizing, (2) Consistent watering, (3) Sufficient sunlight, (4) Pest/disease control, (5) Proper spacing, (6) Successive planting (plant weekly for continuous harvest)."
    },
    "container": {
        "question": "Can I grow vegetables in containers?",
        "answer": "Yes! Best for small spaces. Use 5-gallon pots minimum. Good for: tomato, peppers, beans, carrots, lettuce. Ensure drainage holes. Use rich potting mix. Container plants need frequent watering/feeding."
    }
}

# Chatbot greeting & system messages
CHATBOT_SYSTEM = {
    "greeting": "🌱 Welcome to Gardener.ai Assistant! Ask me anything about gardening, plant care, pests, diseases, or best practices. I'm here to help your garden thrive!",
    "help_text": "Popular questions: watering, soil, fertilizer, pest_control, disease, sunlight, temperature, season, composting, germination, spacing, mulch, weeding, harvesting, crop_rotation, organic, water_conservation, yield, container",
    "unknown": "I'm not sure about that. Try asking about: watering, soil, pest control, diseases, fertilizer, sunlight, temperature, or seasonal planting. Type 'help' for more topics!"
}

def get_answer(question_key):
    """Get answer to common gardening question"""
    if question_key.lower() in GARDENING_FAQs:
        return GARDENING_FAQs[question_key.lower()]
    return None

def search_faq(query):
    """Search FAQ for related topics"""
    query = query.lower()
    matches = []
    
    for key, value in GARDENING_FAQs.items():
        if query in key or query in value.get("question", "").lower():
            matches.append({
                "key": key,
                "question": value.get("question", ""),
                "answer": value.get("answer", "")
            })
    
    return matches

print("✅ Chatbot knowledge base loaded")
print(f"Available topics: {len(GARDENING_FAQs)}")
