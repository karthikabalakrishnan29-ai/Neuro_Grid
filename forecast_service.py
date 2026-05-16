from core_layer.forecasting.load.lstm_model import LoadForecasterLSTM

class ForecastService:
    def __init__(self):
        self.forecaster = LoadForecasterLSTM()

    def get_future_load(self, historical_data):
        prediction = self.forecaster.predict(historical_data)
        return {"prediction": prediction, "confidence": 0.92}