"""
Plant Disease Detection Model Handler
This module handles model loading and inference for plant disease detection
"""

import numpy as np
from pathlib import Path
import os

class PlantDiseaseModel:
    """
    Handles plant disease detection using pre-trained models
    """
    
    def __init__(self, model_type='mobilenetv2'):
        """
        Initialize the model
        
        Args:
            model_type (str): Type of model to use (mobilenetv2, etc.)
        """
        self.model_type = model_type
        self.model = None
        self.loaded = False
        
    def load_model(self):
        """
        Load pre-trained MobileNetV2 model with custom top layers
        Returns: bool - Success status
        """
        try:
            from tensorflow.keras.applications import MobileNetV2
            from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
            from tensorflow.keras.models import Model
            
            # Load base model
            base_model = MobileNetV2(
                input_shape=(224, 224, 3),
                include_top=False,
                weights='imagenet'
            )
            
            # Freeze base model weights
            base_model.trainable = False
            
            # Add custom layers
            x = GlobalAveragePooling2D()(base_model.output)
            predictions = Dense(7, activation='softmax')(x)
            
            # Create model
            self.model = Model(inputs=base_model.input, outputs=predictions)
            self.loaded = True
            
            print("✅ Model loaded successfully")
            return True
            
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            return False
    
    def preprocess_image(self, image_path, image_size=(224, 224)):
        """
        Preprocess image for model inference
        
        Args:
            image_path (str): Path to image file
            image_size (tuple): Target image size
            
        Returns:
            np.array - Preprocessed image
        """
        try:
            from tensorflow.keras.preprocessing import image as keras_image
            from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
            
            # Load image
            img = keras_image.load_img(image_path, target_size=image_size)
            img_array = keras_image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            
            # Preprocess using MobileNetV2 preprocessing
            img_array = preprocess_input(img_array)
            
            return img_array
            
        except Exception as e:
            print(f"❌ Error preprocessing image: {e}")
            return None
    
    def predict(self, image_path):
        """
        Make prediction on image
        
        Args:
            image_path (str): Path to image file
            
        Returns:
            tuple - (predicted_class, confidence_score)
        """
        if not self.loaded:
            print("❌ Model not loaded. Call load_model() first.")
            return None, None
        
        try:
            # Preprocess image
            img_array = self.preprocess_image(image_path)
            if img_array is None:
                return None, None
            
            # Make prediction
            predictions = self.model.predict(img_array, verbose=0)
            predicted_class = np.argmax(predictions[0])
            confidence = float(predictions[0][predicted_class])
            
            return predicted_class, confidence
            
        except Exception as e:
            print(f"❌ Error during prediction: {e}")
            return None, None


# Quick test function
if __name__ == '__main__':
    print("🌱 Plant Disease Detection Model")
    print("=" * 50)
    
    # Initialize model
    model = PlantDiseaseModel()
    
    # Load model (requires TensorFlow installed)
    print("\nLoading model...")
    model.load_model()
