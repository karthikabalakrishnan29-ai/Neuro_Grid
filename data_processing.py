import sys
import os

# 1. First PATH-a set pannanum (Ithu thaan top-la irukkanum)
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))

# 2. Athukku apparam thaan unga local utils-a import pannanum
try:
    from utils.logger import logger
except ImportError:
    # Oru velai logger illana simulation stop aagama irukka ithu:
    print("⚠️ Logger not found, using standard print.")
    class DummyLogger:
        info = print
        error = print
    logger = DummyLogger()

import pandas as pd
import numpy as np

def preprocess_microgrid_data():
    # 1. Path Setup
    # Path-a dynamic-ah mathikkalam for safety
    base_dir = os.path.abspath(os.path.dirname(__file__) + '/..')
    raw_path = os.path.join(base_dir, "data/raw/microgrid/microgrid_dataset_1000_rows.csv")
    processed_dir = os.path.join(base_dir, "data/processed/")
    
    if not os.path.exists(raw_path):
        logger.error(f"❌ Raw dataset missing at: {raw_path}")
        return

    # 2. Load Data
    df = pd.read_csv(raw_path)
    logger.info(f"📊 Loaded {len(df)} rows from raw data.")

    # 3. Data Cleaning
    df.ffill(inplace=True)

    # 4. Feature Engineering
    if 'irradiance' in df.columns:
        df['P_solar_calc'] = df['irradiance'] * 0.18 * 20 
    
    if 'wind_speed' in df.columns:
        df['P_wind_calc'] = 0.5 * 1.225 * 50 * 0.4 * (df['wind_speed']**3)

    # 5. Adding Time Features
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['hour'] = df['timestamp'].dt.hour
        df['day_of_week'] = df['timestamp'].dt.dayofweek

    # 6. Save Processed Data
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)
        
    output_file = os.path.join(processed_dir, "final_training_data.csv")
    df.to_csv(output_file, index=False)
    logger.info(f"✅ Processed data saved to: {output_file}")

if __name__ == "__main__":
    preprocess_microgrid_data()