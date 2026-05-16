from utils.config import HOUSEHOLD_DATA_PATH, MICROGRID_DATA_PATH
from .data_cleaning import DataCleaner
from .feature_engineering import FeatureEngineer
import pandas as pd

class DataPipeline:
    def __init__(self):
        self.cleaner = DataCleaner()
        self.engineer = FeatureEngineer()

    def get_processed_microgrid_data(self):
        # 1. Load
        df = pd.read_csv(MICROGRID_DATA_PATH)
        # 2. Clean
        df = self.cleaner.clean_microgrid_data(df)
        # 3. Engineer
        df = self.engineer.add_time_features(df)
        return df

    def get_processed_household_data(self):
        # 1. Load (Semicolon check)
        df = pd.read_csv(HOUSEHOLD_DATA_PATH, sep=';', low_memory=False)
        # 2. Clean
        df = self.cleaner.clean_household_data(df)
        return df