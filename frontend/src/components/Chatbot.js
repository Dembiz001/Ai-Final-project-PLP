import React, { useState, useRef, useEffect } from 'react';
import './Chatbot.css';

const GARDENING_FAQS = {
  "watering": "How often should I water my plants?",
  "soil": "What's the best soil for growing vegetables?",
  "fertilizer": "When and how should I fertilize?",
  "pest_control": "How do I manage pests naturally?",
  "disease": "How do I prevent plant diseases?",
  "sunlight": "How much sunlight do vegetables need?",
  "temperature": "What temperature is best for gardening?",
  "season": "When should I plant in West Africa?",
  "composting": "How do I make compost?",
  "germination": "How do I start seeds successfully?",
  "spacing": "How far apart should I plant?",
  "mulch": "Why should I use mulch?",
  "weeding": "How do I manage weeds?",
  "harvesting": "When and how do I harvest?",
  "crop_rotation": "What is crop rotation and why?",
  "organic": "How do I garden organically?",
  "water_conservation": "How can I save water in the garden?",
  "yield": "How can I increase my harvest?",
  "container": "Can I grow vegetables in containers?"
};

const ANSWERS = {
  "watering": "Most vegetables need 1-1.5 inches of water per week. Check soil moisture 2-3 inches deep—if it's dry, water. During rainy season, reduce frequency. Early morning watering is best to reduce disease.",
  "soil": "Use well-draining loam soil with organic matter (compost). Good soil should: (1) drain water, (2) retain moisture, (3) have high organic content, (4) have balanced pH. Test soil annually.",
  "fertilizer": "Apply balanced fertilizer (NPK 10-10-10) every 2-4 weeks during growing season. Organic options: compost, manure, bone meal. Start light—excess nitrogen causes leaves but fewer fruits.",
  "pest_control": "Best practices: (1) Inspect plants weekly, (2) Remove infected leaves, (3) Spray neem oil or insecticidal soap, (4) Use row covers on young plants, (5) Introduce natural predators (ladybugs), (6) Rotate crops.",
  "disease": "Prevention is key: (1) Avoid overhead watering, (2) Space plants for air circulation, (3) Remove dead leaves, (4) Sterilize tools, (5) Don't reuse diseased soil, (6) Rotate crops yearly.",
  "sunlight": "Most vegetables need 6-8 hours of direct sunlight. Leafy greens tolerate 4-5 hours. Shade-loving: spinach, lettuce. Sun-lovers: tomato, peppers, eggplant. Hot climates: afternoon shade helps.",
  "temperature": "Most vegetables grow best at 70-85°F (21-29°C). Cool-season: lettuce, spinach at 60-70°F. Warm-season: okra, watermelon at 75-95°F. Plant timing matters—know your local frost dates.",
  "season": "Dry Season (Nov-Mar): best for most vegetables. Rainy Season (Apr-Oct): okra, cucumbers, beans thrive. Key: Start before heavy rains, use mulch to retain moisture, water during dry spells.",
  "composting": "Layer: (1) Green waste (grass, leaves) 50%, (2) Brown waste (wood, straw) 50%. Add water, turn weekly. Ready in 2-3 months. Use aged compost (dark, crumbly) in soil to improve fertility and drainage.",
  "germination": "Use seed trays with moist potting mix. Keep at 70-80°F. Provide bright light once sprouted. Harden off seedlings (expose gradually to sun) before transplanting. Direct seeding works for beans, maize, cassava.",
  "spacing": "Proper spacing prevents disease and competition. Examples: tomato 24-36\", okra 12-18\", beans 4-6\", carrots 2-3\", cabbage 18-24\". Crowding reduces yield and invites pests.",
  "mulch": "Mulch (straw, leaves, grass): (1) Retains soil moisture, (2) Keeps soil cool, (3) Prevents weeds, (4) Enriches soil as it decays, (5) Reduces watering frequency—use 2-3 inch layer.",
  "weeding": "Weed early and often. Remove when small to prevent seed spread. Mulch to suppress weeds. Hand-pull or hoe. Avoid herbicides in food gardens. Regular weeding saves time later.",
  "harvesting": "Harvest in early morning for best quality. Okra: pick young/tender (3-4 days growth). Carrots/onions: when mature. Leafy greens: outer leaves first. Handle gently to avoid bruising.",
  "crop_rotation": "Rotate crop families yearly: (1) Reduces pest/disease buildup, (2) Balances soil nutrients, (3) Improves soil health. Example: tomato → beans (fixes nitrogen) → leafy greens.",
  "organic": "Organic farming: (1) No synthetic chemicals, (2) Use compost/manure, (3) Companion planting, (4) Natural pest control, (5) Crop rotation, (6) Mulching. Healthier soil = healthier plants.",
  "water_conservation": "Water-saving tips: (1) Mulch heavily, (2) Water early morning/evening, (3) Drip irrigation (best), (4) Water soil not leaves, (5) Group plants by water needs, (6) Choose drought-tolerant crops.",
  "yield": "Maximize yield: (1) Good soil + regular fertilizing, (2) Consistent watering, (3) Sufficient sunlight, (4) Pest/disease control, (5) Proper spacing, (6) Successive planting (plant weekly for continuous harvest).",
  "container": "Yes! Best for small spaces. Use 5-gallon pots minimum. Good for: tomato, peppers, beans, carrots, lettuce. Ensure drainage holes. Use rich potting mix. Container plants need frequent watering/feeding."
};

function Chatbot() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    { type: 'bot', text: '🌱 Welcome to Gardener.ai Assistant! Ask me anything about gardening, plant care, pests, diseases, or best practices.' }
  ]);
  const [input, setInput] = useState('');
  const [suggestedTopics, setSuggestedTopics] = useState(Object.keys(GARDENING_FAQS).slice(0, 4));
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = (topic = null) => {
    const userMessage = topic || input.trim();
    
    if (!userMessage) return;

    // Add user message
    setMessages(prev => [...prev, { type: 'user', text: userMessage }]);
    setInput('');

    // Find matching answer
    const matchedTopic = Object.keys(GARDENING_FAQS).find(
      key => userMessage.toLowerCase().includes(key) || 
              userMessage.toLowerCase().includes(GARDENING_FAQS[key].toLowerCase().split('?')[0])
    );

    // Send bot response
    setTimeout(() => {
      if (matchedTopic && ANSWERS[matchedTopic]) {
        setMessages(prev => [...prev, {
          type: 'bot',
          text: ANSWERS[matchedTopic]
        }]);
        
        // Suggest next topics
        const otherTopics = Object.keys(GARDENING_FAQS)
          .filter(k => k !== matchedTopic)
          .sort(() => Math.random() - 0.5)
          .slice(0, 3);
        setSuggestedTopics(otherTopics);
      } else {
        setMessages(prev => [...prev, {
          type: 'bot',
          text: "I'm not sure about that. Try asking about: watering, soil, pest control, diseases, fertilizer, sunlight, temperature, or seasonal planting. 🌿"
        }]);
      }
    }, 300);
  };

  return (
    <>
      {/* Chatbot Toggle Button */}
      <button 
        className="chatbot-toggle"
        onClick={() => setIsOpen(!isOpen)}
        title="Gardening Assistant"
      >
        {isOpen ? '✕' : '💬'}
      </button>

      {/* Chatbot Window */}
      {isOpen && (
        <div className="chatbot-container">
          <div className="chatbot-header">
            <h3>🌱 Gardener.ai Assistant</h3>
            <button onClick={() => setIsOpen(false)}>✕</button>
          </div>

          <div className="chatbot-messages">
            {messages.map((msg, idx) => (
              <div key={idx} className={`message ${msg.type}`}>
                <span className="message-text">{msg.text}</span>
              </div>
            ))}
            <div ref={messagesEndRef} />
          </div>

          {/* Suggested Topics */}
          <div className="chatbot-suggestions">
            {suggestedTopics.length > 0 && (
              <>
                <small>Suggested:</small>
                <div className="suggestion-buttons">
                  {suggestedTopics.map(topic => (
                    <button
                      key={topic}
                      className="suggestion-btn"
                      onClick={() => handleSendMessage(GARDENING_FAQS[topic])}
                    >
                      {topic.replace('_', ' ')}
                    </button>
                  ))}
                </div>
              </>
            )}
          </div>

          {/* Input Area */}
          <div className="chatbot-input">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
              placeholder="Ask about gardening..."
            />
            <button onClick={() => handleSendMessage()}>Send</button>
          </div>
        </div>
      )}
    </>
  );
}

export default Chatbot;
