import pandas as pd
from utils.logger import logger
from utils.config import PROCESSED_DATA_DIR

class FeatureStore:
    def __init__(self):
        self.features = {}
        self.store_path = PROCESSED_DATA_DIR / "feature_registry.csv"

    def register_features(self, df, source_name):
        """Cleaned data-va feature store-la register panna"""
        try:
            self.features[source_name] = df
            logger.info(f"Features from '{source_name}' registered successfully.")
        except Exception as e:
            logger.error(f"Error registering features: {e}")

    def get_features_for_model(self, source_name, columns=None):
        """ML models-ku thevaiyana specific columns-a mattum edukka"""
        if source_name in self.features:
            df = self.features[source_name]
            if columns:
                return df[columns]
            return df
        logger.warning(f"Source '{source_name}' not found in Feature Store.")
        return None

    def save_to_disk(self):
        """Future use-ku features-a save panni vekka"""
        if self.features:
            # Ellaa features-aiyum combine panni save pannuvom
            combined_df = pd.concat(self.features.values(), axis=1)
            combined_df.to_csv(self.store_path, index=False)
            logger.info(f"Feature store saved to disk: {self.store_path}")

    def load_from_disk(self):
        """Saved features-a thirumba load panna"""
        if self.store_path.exists():
            df = pd.read_csv(self.store_path)
            logger.info("Feature store loaded from disk.")
            return df
        return None

# Global Instance
feature_store = FeatureStore()