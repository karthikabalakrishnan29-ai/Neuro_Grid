import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_load_forecaster():
    # 1. Load Dataset
    data = pd.read_csv('data/processed/power_consumption.csv')
    X = data[['voltage', 'global_intensity', 'sub_metering_1']]
    y = data['active_power']

    # 2. Train Model
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X, y)

    # 3. Save as Pickle file
    joblib.dump(model, 'models/forecasting/load_model_v1.pkl')
    print("Model trained and saved to models/forecasting/")

if __name__ == "__main__":
    train_load_forecaster()