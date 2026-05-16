import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from utils.logger import logger

class AnomalyDetector:
    def __init__(self, contamination=0.05):
        # contamination: dataset-la evlo percentage anomaly irukkum-nu guess
        self.model = IsolationForest(contamination=contamination, random_state=42)
        logger.info("Isolation Forest Anomaly Detector Initialized.")

    def train_model(self, data):
        """Historical data-va vechu normal behavior-a learn pannum"""
        # FFT features and Power Usage-a training-ku edukkurom
        features = data.filter(regex='FFT_|Power|Voltage|Frequency')
        self.model.fit(features)
        logger.info("Anomaly detection model training complete.")

    def detect(self, current_reading):
        """
        Current sensor reading-a check panni anomaly-ah illaiyanu sollum.
        Output: -1 (Anomaly), 1 (Normal)
        """
        prediction = self.model.predict(current_reading)
        is_anomaly = True if prediction[0] == -1 else False
        return is_anomaly