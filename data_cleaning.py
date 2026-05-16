import pandas as pd
import numpy as np
from utils.logger import logger

class DataCleaner:
    @staticmethod
    def clean_household_data(df):
        """Handle missing values and numeric conversions for household data"""
        logger.info("Cleaning Household Dataset...")
        # Missing values-a '?' iruntha NaN-ah mathuvom
        df = df.replace('?', np.nan)
        
        # Numeric columns-a convert pannuvom
        cols_to_fix = ['Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity']
        for col in cols_to_fix:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Null values-a median vechu fill pannuvom (Data loss kuraikka)
        return df.fillna(df.median(numeric_only=True))

    @staticmethod
    def clean_microgrid_data(df):
        """Handle timestamps and basic cleaning for microgrid data"""
        logger.info("Cleaning Microgrid Dataset...")
        df['Time'] = pd.to_datetime(df['Time'])
        return df.dropna()