"""
Crop Prediction Model using Decision Tree Classifier
This module provides crop recommendation based on soil parameters.
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pickle
import os
import sys


class CropPredictionModel:
    """
    A machine learning model for crop prediction based on soil parameters.
    
    Attributes:
        model: The trained decision tree classifier
        feature_names: List of feature names
        label_encoder: Encoder for crop labels
    """

    def __init__(self, data_path="../data/crop_dataset_sample.csv"):
        """
        Initialize the model and load data.
        
        Args:
            data_path: Path to the CSV file containing training data
        """
        self.model = None
        self.feature_names = ["nitrogen", "phosphorus", "potassium", "rainfall"]
        self.label_encoder = LabelEncoder()
        self.data = None
        
        try:
            self.load_data(data_path)
            self.train_model()
        except FileNotFoundError:
            print(f"Error: Data file not found at {data_path}")
            sys.exit(1)
        except Exception as e:
            print(f"Error during model initialization: {str(e)}")
            sys.exit(1)

    def load_data(self, data_path):
        """
        Load training data from CSV file.
        
        Args:
            data_path: Path to the CSV file
        """
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Data file not found: {data_path}")
        
        self.data = pd.read_csv(data_path)
        print(f"Data loaded successfully. Shape: {self.data.shape}")
        print(f"Columns: {list(self.data.columns)}")

    def train_model(self):
        """Train the decision tree classifier."""
        try:
            # Prepare features and labels
            X = self.data[self.feature_names]
            y = self.data["label"]
            
            # Validate data
            if X.isnull().any().any() or y.isnull().any():
                raise ValueError("Data contains null values")
            
            # Train model
            self.model = DecisionTreeClassifier(max_depth=5, random_state=42)
            self.model.fit(X, y)
            
            # Store encoder for future use
            self.label_encoder.fit(y)
            
            print(f"Model trained successfully!")
            print(f"Number of crops: {len(self.label_encoder.classes_)}")
            print(f"Crops: {list(self.label_encoder.classes_)}")
            
        except Exception as e:
            print(f"Error during model training: {str(e)}")
            raise

    def predict(self, nitrogen, phosphorus, potassium, rainfall):
        """
        Predict the best crop for given soil parameters.
        
        Args:
            nitrogen: Nitrogen level in mg/kg
            phosphorus: Phosphorus level in mg/kg
            potassium: Potassium level in mg/kg
            rainfall: Annual rainfall in mm
            
        Returns:
            Predicted crop name
            
        Raises:
            ValueError: If inputs are invalid
        """
        if self.model is None:
            raise RuntimeError("Model not trained. Please train the model first.")
        
        # Validate inputs
        inputs = [nitrogen, phosphorus, potassium, rainfall]
        if not all(isinstance(x, (int, float)) for x in inputs):
            raise ValueError("All inputs must be numeric")
        
        if any(x < 0 for x in inputs):
            raise ValueError("All inputs must be non-negative")
        
        try:
            # Create feature array
            X = np.array([[nitrogen, phosphorus, potassium, rainfall]])
            
            # Make prediction
            prediction = self.model.predict(X)[0]
            return prediction
            
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            raise

    def predict_probability(self, nitrogen, phosphorus, potassium, rainfall):
        """
        Get probability distribution for all crops.
        
        Args:
            nitrogen: Nitrogen level in mg/kg
            phosphorus: Phosphorus level in mg/kg
            potassium: Potassium level in mg/kg
            rainfall: Annual rainfall in mm
            
        Returns:
            Dictionary mapping crops to probability scores
        """
        if self.model is None:
            raise RuntimeError("Model not trained")
        
        try:
            X = np.array([[nitrogen, phosphorus, potassium, rainfall]])
            proba = self.model.predict_proba(X)[0]
            
            result = {}
            for crop, prob in zip(self.model.classes_, proba):
                result[crop] = round(prob * 100, 2)
            
            return result
            
        except Exception as e:
            print(f"Error during probability prediction: {str(e)}")
            raise

    def save_model(self, filepath="crop_model.pkl"):
        """
        Save the trained model to a file.
        
        Args:
            filepath: Path to save the model
        """
        try:
            with open(filepath, 'wb') as f:
                pickle.dump(self.model, f)
            print(f"Model saved successfully to {filepath}")
        except Exception as e:
            print(f"Error saving model: {str(e)}")

    def load_model(self, filepath="crop_model.pkl"):
        """
        Load a previously trained model.
        
        Args:
            filepath: Path to the saved model
        """
        try:
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"Model file not found: {filepath}")
            
            with open(filepath, 'rb') as f:
                self.model = pickle.load(f)
            print(f"Model loaded successfully from {filepath}")
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            raise


def main():
    """Main function to demonstrate model usage."""
    print("=" * 60)
    print("KRISHIMITRA - Crop Prediction System")
    print("=" * 60)
    
    # Initialize model
    model = CropPredictionModel("../data/crop_dataset_sample.csv")
    
    # Example predictions
    print("\n--- Testing Model Predictions ---")
    
    test_cases = [
        (90, 42, 43, 200, "Rice conditions"),
        (60, 55, 44, 150, "Maize conditions"),
        (20, 20, 20, 90, "Peas conditions"),
        (85, 40, 45, 180, "Rice conditions")
    ]
    
    for n, p, k, r, description in test_cases:
        try:
            prediction = model.predict(n, p, k, r)
            probabilities = model.predict_probability(n, p, k, r)
            
            print(f"\n{description}:")
            print(f"  Input: N={n}, P={p}, K={k}, Rainfall={r}mm")
            print(f"  Predicted Crop: {prediction}")
            print(f"  Confidence Scores: {probabilities}")
        except ValueError as e:
            print(f"  Prediction Error: {str(e)}")
    
    # Save model for production use
    model.save_model("crop_model.pkl")


if __name__ == "__main__":
    main()