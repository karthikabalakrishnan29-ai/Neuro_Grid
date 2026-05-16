import pandas as pd

class FeatureEngineer:
    def __init__(self):
        pass

    def add_time_features(self, df, time_col='Time'):
        """Time-a vechu Peak hours-a kandupidikka help pannum"""
        df[time_col] = pd.to_datetime(df[time_col])
        df['hour'] = df[time_col].dt.hour
        df['day_of_week'] = df[time_col].dt.dayofweek
        df['is_weekend'] = df['day_of_week'].apply(lambda x: 1 if x >= 5 else 0)
        return df

    def create_rolling_features(self, df, column, window=4):
        """Moving average features for forecasting"""
        df[f'{column}_rolling_avg'] = df[column].rolling(window=window).mean()
        return df.fillna(0)