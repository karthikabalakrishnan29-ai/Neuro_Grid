import numpy as np
import pandas as pd
from utils.logger import logger

class LoadForecasterLSTM:
    def __init__(self, window_size=10):
        self.window_size = window_size
        self.model = None # Ippo dummy, neenga Keras/TF model inga load pannalam

    def prepare_data(self, series):
        """Data-va rolling window format-ku mathum"""
        X, y = [], []
        for i in range(len(series) - self.window_size):
            X.append(series[i:i + self.window_size])
            y.append(series[i + self.window_size])
        return np.array(X), np.array(y)

    def predict(self, recent_data):
        """Adutha time step load-a predict pannum"""
        logger.info("Running LSTM Load Forecast...")
        # Simple moving average for simulation if model not trained
        return np.mean(recent_data) * 1.05