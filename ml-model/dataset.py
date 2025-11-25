"""
Plant disease datasets and training utilities
This module provides utilities for training and evaluating models
"""

import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

class PlantDatasetManager:
    """
    Manages plant disease datasets for training
    """
    
    PLANT_CLASSES = [
        'healthy',
        'fungal_disease', 
        'bacterial_disease',
        'viral_disease',
        'pest_damage',
        'nutrient_deficiency',
        'water_stress'
    ]
    
    @staticmethod
    def get_data_generators(batch_size=32, image_size=(224, 224)):
        """
        Create data generators for training and validation
        
        Args:
            batch_size (int): Batch size for training
            image_size (tuple): Size of images
            
        Returns:
            tuple - (train_generator, validation_generator)
        """
        
        # Training data augmentation
        train_datagen = ImageDataGenerator(
            rescale=1./255,
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest'
        )
        
        # Validation data (only rescaling)
        val_datagen = ImageDataGenerator(rescale=1./255)
        
        return train_datagen, val_datagen
    
    @staticmethod
    def download_datasets():
        """
        Download available plant disease datasets
        
        Recommended datasets:
        - PlantVillage Dataset (40K+ images)
        - Plant-Leaf-Dataset
        - Crop Disease Detection datasets from Kaggle
        """
        print("Recommended datasets to download:")
        print("1. PlantVillage: https://github.com/spMohanty/PlantVillage-Dataset")
        print("2. Kaggle Plant Pathology: https://www.kaggle.com/datasets")
        print("3. Leaf Disease: https://www.kaggle.com/vipoooool/new-plant-diseases-dataset")


# Training configuration
TRAINING_CONFIG = {
    'epochs': 50,
    'batch_size': 32,
    'learning_rate': 0.001,
    'image_size': (224, 224),
    'validation_split': 0.2,
    'early_stopping': True,
    'patience': 10
}

print("✅ Dataset manager initialized")
print(f"Available classes: {PlantDatasetManager.PLANT_CLASSES}")
