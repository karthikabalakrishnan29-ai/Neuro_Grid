class EnsembleForecaster:
    def __init__(self, models):
        self.models = models

    def get_weighted_forecast(self, data):
        """Ellaa model predictions-aiyum weightage vechu combine pannum"""
        predictions = [m.predict(data) for m in self.models]
        return sum(predictions) / len(predictions)