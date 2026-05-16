import joblib
import os
from utils.logger import logger

class ForecastingLoader:
    def __init__(self):
        # Model files irukkura path
        self.model_path = "models/forecasting/load_model_v1.pkl"

    def load_trained_model(self):
        """Pickle file-a load panni return pannum"""
        if os.path.exists(self.model_path):
            model = joblib.load(self.model_path)
            logger.info("Forecasting model loaded successfully.")
            return model
        else:
            logger.error("Model file not found! Run training script first.")
            return None