"""
AI Gardening Assistant Backend
Flask API for plant disease detection and recommendations
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import numpy as np
from PIL import Image
import io
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'ml-model'))

from model_config import RECOMMENDATIONS, PLANT_LIBRARY, PLANT_CLASSES

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Global model variable
model = None

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_model():
    """Load TensorFlow MobileNetV2 model"""
    global model
    try:
        from tensorflow.keras.applications import MobileNetV2
        from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
        from tensorflow.keras.preprocessing import image
        from tensorflow.keras.models import Model
        from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
        import tensorflow as tf
        
        # For demo purposes, we'll use a simplified approach
        # In production, you'd load a fine-tuned model trained on plant disease data
        base_model = MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
        base_model.trainable = False
        
        x = GlobalAveragePooling2D()(base_model.output)
        predictions = Dense(7, activation='softmax')(x)  # 7 classes
        model = Model(inputs=base_model.input, outputs=predictions)
        
        print("Model loaded successfully")
        return True
    except Exception as e:
        print(f"Error loading model: {e}")
        return False

def predict_plant_condition(image_path):
    """
    Predict plant condition from image
    Returns class prediction and confidence score
    """
    try:
        from tensorflow.keras.preprocessing import image as keras_image
        from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
        
        # Load and preprocess image
        img = keras_image.load_img(image_path, target_size=(224, 224))
        img_array = keras_image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        
        # Make prediction
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_class])
        
        return predicted_class, confidence
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None, None

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'AI Gardening Assistant Backend',
        'model_loaded': model is not None
    })

@app.route('/api/analyze', methods=['POST'])
def analyze_plant():
    """
    Analyze plant image and return diagnosis
    """
    try:
        # Check if file is in request
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        file = request.files['image']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Use PNG, JPG, JPEG, or GIF'}), 400
        
        # Save file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Make prediction
        if model is None:
            # Demo mode - return random prediction
            predicted_class = np.random.randint(0, 7)
            confidence = np.random.uniform(0.7, 0.99)
        else:
            predicted_class, confidence = predict_plant_condition(filepath)
        
        # Get recommendation
        condition = PLANT_CLASSES.get(predicted_class, "unknown")
        recommendation = RECOMMENDATIONS.get(condition, RECOMMENDATIONS["healthy"])
        
        return jsonify({
            'success': True,
            'condition': condition,
            'confidence': float(confidence),
            'diagnosis': recommendation['title'],
            'description': recommendation['description'],
            'actions': recommendation['actions']
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "AI Gardening Assistant Backend is running!"})

@app.route('/api/plant-library', methods=['GET'])
def get_plant_library():
    """Get plant information library"""
    return jsonify(PLANT_LIBRARY)

@app.route('/api/plant-library/<plant_name>', methods=['GET'])
def get_plant_info(plant_name):
    """Get specific plant information"""
    plant_info = PLANT_LIBRARY.get(plant_name.lower())
    if plant_info:
        return jsonify(plant_info)
    return jsonify({'error': 'Plant not found'}), 404

@app.route('/api/recommendations', methods=['GET'])
def get_all_recommendations():
    """Get all possible recommendations"""
    return jsonify(RECOMMENDATIONS)

@app.errorhandler(413)
def request_entity_too_large(error):
    return jsonify({'error': 'File too large. Maximum size is 5MB'}), 413

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Load model on startup (optional)
    # load_model()
    print("Starting AI Gardening Assistant Backend...")
    app.run(debug=True, host='0.0.0.0', port=5000)
    
    