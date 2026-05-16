import pandas as pd
import numpy as np
from utils.logger import logger

class ModelExplainer:
    def __init__(self, model, feature_names):
        """
        model: Trained XGBoost or LSTM model
        feature_names: List of columns (e.g., ['Voltage', 'Global_intensity', 'Sub_metering_1'])
        """
        self.model = model
        self.feature_names = feature_names

    def explain_prediction(self, input_data):
        """
        Oru specific prediction-ku entha feature evlo contribution 
        pannuchu-nu explain pannum.
        """
        try:
            # XGBoost model-na direct-ah feature importance edukalam
            if hasattr(self.model, 'feature_importances_'):
                importances = self.model.feature_importances_
                explanation = dict(zip(self.feature_names, importances))
                
                # Sort panni top features-a edukkurom
                sorted_explanation = dict(sorted(explanation.items(), key=lambda item: item[1], reverse=True))
                
                top_feature = list(sorted_explanation.keys())[0]
                impact = round(sorted_explanation[top_feature] * 100, 2)
                
                msg = f"Prediction driven mainly by '{top_feature}' ({impact}% impact)."
                logger.info(f"Model Explainer: {msg}")
                return sorted_explanation, msg
            
            else:
                return None, "Model type not supported for direct explanation."
        
        except Exception as e:
            logger.error(f"Error in ModelExplainer: {e}")
            return None, "Error generating explanation."

    def get_global_insight(self):
        """Full dataset-la overall-ah entha feature mukkiyam-nu sollum"""
        if hasattr(self.model, 'get_booster'):
            # XGBoost specific global importance
            scores = self.model.get_booster().get_score(importance_type='weight')
            return scores
        return {"status": "Global insights only available for Tree-based models."}

    def generate_narrative(self, prediction_value, explanation_dict):
        """Dashboard-la kaatta oru chinna paragraph generate pannum"""
        top_3 = list(explanation_dict.keys())[:3]
        narrative = (f"The predicted load is {round(prediction_value, 2)} kW. "
                     f"This is primarily influenced by {top_3[0]}, followed by {top_3[1]} and {top_3[2]}.")
        return narrative