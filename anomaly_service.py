from intelligence_layer.anomaly_detection.anomaly_detector import AnomalyDetector

class AnomalyService:
    def __init__(self):
        self.detector = AnomalyDetector()

    def check_for_faults(self, current_data):
        is_anomaly = self.detector.detect(current_data)
        return {"is_anomaly": is_anomaly, "status": "Critical" if is_anomaly else "Healthy"}