import xgboost as xgb
import pandas as pd
import numpy as np
from utils.logger import logger

class LoadForecasterXGB:
    def __init__(self):
        self.model = xgb.XGBRegressor(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=5
        )
        logger.info("XGBoost Load Forecaster initialized.")

    def train(self, X_train, y_train):
        """Historical load data-va vechu model-a train panna"""
        logger.info("Training XGBoost model...")
        self.model.fit(X_train, y_train)

    def predict(self, current_features):
        """
        Features like Voltage, Global_intensity-a input-ah kudutha 
        Load (kW) predict pannum.
        """
        # Dataframe or array-va input-ah ethukkum
        prediction = self.model.predict(current_features)
        return np.round(prediction, 4)