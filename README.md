# 🌱 AI Garden Assistant

A web-based platform that uses artificial intelligence to analyze plant images and provide instant feedback on plant health. Upload a photo of a plant and get instant diagnosis with practical gardening recommendations.

## 🎯 Features (MVP)

- **Plant Image Analysis**: Upload photos of plants for AI-powered diagnosis
- **Disease Detection**: Identifies fungal, bacterial, and viral diseases
- **Pest Detection**: Recognizes pest damage and infestation signs
- **Nutrient Analysis**: Detects nutrient deficiencies and water stress
- **Smart Recommendations**: Get actionable care tips based on diagnosis
- **Plant Library**: Browse care guides for popular garden plants
- **Confidence Scoring**: See confidence levels for each diagnosis

## 🚀 Tech Stack

### Frontend
- **React** 18.2 - UI framework
- **Axios** - HTTP client
- **CSS3** - Styling with responsive design

### Backend
- **Flask** 2.3 - Python web framework
- **TensorFlow/Keras** - ML/AI models
- **MobileNetV2** - Pre-trained image classification
- **CORS** - Cross-origin requests support

### ML/AI
- **TensorFlow** - Deep learning framework
- **MobileNetV2** - Lightweight model for plant classification
- **Transfer Learning** - Fine-tuned on plant disease datasets

### Deployment Ready
- **Frontend**: Vercel
- **Backend**: Render/Heroku
- **Database**: Firebase or MongoDB (optional)

## 📋 Project Structure

```
ai-garden/
├── frontend/                 # React application
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/       # Reusable React components
│   │   │   ├── Header.js
│   │   │   ├── Navigation.js
│   │   │   ├── ImageUpload.js
│   │   │   ├── DiagnosisResult.js
│   │   │   └── PlantLibrary.js
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   ├── .env.local            # Frontend configuration
│   └── package.json
├── backend/                  # Flask API
│   ├── app.py               # Main Flask application
│   ├── config.py            # Configuration
│   ├── .env                 # Environment variables
│   ├── requirements.txt      # Python dependencies
│   └── uploads/             # User uploaded images
└── ml-model/                # ML Model configuration
    └── model_config.py      # Plant classes and recommendations
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- Node.js 14+ and npm
- Git

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create Python virtual environment:
```bash
python -m venv venv
```

3. Activate virtual environment:
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

4. Install Python dependencies:
```bash
pip install -r requirements.txt
```

5. Create uploads directory:
```bash
mkdir uploads
```

6. Run Flask server:
```bash
python app.py
```

Server will start at `http://localhost:5000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install Node dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm start
```

Application will open at `http://localhost:3000`

## 🔧 Configuration

### Frontend (.env.local)
```
REACT_APP_API_URL=http://localhost:5000
REACT_APP_ENV=development
```

### Backend (.env)
```
FLASK_ENV=development
FLASK_APP=app.py
SECRET_KEY=your-secret-key-here
CORS_ORIGINS=*
```

## 📚 API Endpoints

### Health Check
- `GET /api/health` - Check backend status

### Plant Analysis
- `POST /api/analyze` - Upload image and get diagnosis
  - Request: `multipart/form-data` with `image` field
  - Response: JSON with diagnosis, confidence, and recommendations

### Plant Library
- `GET /api/plant-library` - Get all plants
- `GET /api/plant-library/<plant_name>` - Get specific plant info

### Recommendations
- `GET /api/recommendations` - Get all condition recommendations

## 🧠 AI Model

The application uses **MobileNetV2** with transfer learning:

### Plant Conditions Detected:
1. **Healthy** - Plant is in good condition
2. **Fungal Disease** - Fungal infections detected
3. **Bacterial Disease** - Bacterial infections detected
4. **Viral Disease** - Viral infections detected
5. **Pest Damage** - Pest or insect damage
6. **Nutrient Deficiency** - Lacks essential nutrients
7. **Water Stress** - Over/under-watering issues

### Model Features:
- Input: 224x224 RGB image
- Output: 7-class classification + confidence score
- Lightweight: Suitable for mobile and web deployment
- Fast inference: Real-time analysis

## 🌱 Plant Library

Includes care information for:
- Tomato
- Lettuce
- Rose
- Basil
- Pepper

Each plant includes:
- Watering schedule
- Light requirements
- Temperature range
- Soil type
- Common issues

## 🎨 UI/UX Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Drag & Drop**: Easy image upload
- **Real-time Preview**: See uploaded image before analysis
- **Confidence Visualization**: Bar chart showing diagnosis confidence
- **Intuitive Navigation**: Easy switching between features
- **Clean Typography**: Professional and accessible design
- **Color-coded Actions**: Visual indicators for severity

## 🔐 Security Considerations

- File size limit: 5MB
- Allowed formats: PNG, JPG, JPEG, GIF
- CORS enabled for cross-origin requests
- Secret key for session management
- Input validation on both frontend and backend

## 📱 Future Enhancements

- [ ] Watering reminders (push notifications)
- [ ] Garden progress tracker
- [ ] Personalized chatbot assistant
- [ ] Save diagnosis history
- [ ] Multi-language support
- [ ] Offline capability
- [ ] Camera integration
- [ ] Advanced analytics
- [ ] User authentication & profiles
- [ ] Social sharing features

## 🚀 Deployment

### Deploy Frontend to Vercel

```bash
cd frontend
npm run build
vercel
```

### Deploy Backend to Render

1. Push code to GitHub
2. Connect repository to Render
3. Set environment variables
4. Deploy with: `python app.py`

### Database Setup (Optional)

#### Firebase Setup:
1. Create Firebase project
2. Get credentials from Firebase Console
3. Set environment variables in `.env`

#### MongoDB Setup:
1. Create MongoDB Atlas cluster
2. Get connection string
3. Add to backend configuration

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check documentation
- Review API responses for error messages

## 🌍 Impact & SDG Alignment

### Sustainable Development Goals:
- **SDG 2 (Zero Hunger)**: Improves crop yield and food security
- **SDG 13 (Climate Action)**: Promotes sustainable gardening practices
- **SDG 11 (Sustainable Cities)**: Supports urban and community gardening

### Real-World Impact:
- ✅ Helps gardeners diagnose plant issues early
- ✅ Reduces crop losses from late detection
- ✅ Empowers beginners with accessible knowledge
- ✅ Supports small-scale farmers
- ✅ Promotes sustainable home gardening
- ✅ Increases plant survival rates

## 🎓 Learning Resources

- [TensorFlow Documentation](https://www.tensorflow.org/)
- [React Documentation](https://react.dev/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Plant Disease Datasets](https://www.kaggle.com/datasets)

---

Made with 🌿 for gardeners everywhere
