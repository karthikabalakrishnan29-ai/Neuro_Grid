from utils.logger import logger

class EnergyScheduler:
    def __init__(self):
        self.schedule = []

    def create_24h_schedule(self, hourly_forecasts):
        """Adutha 24 hours-ku enna pannanum-nu oru plan create pannum"""
        logger.info("Generating 24-hour dispatch schedule...")
        for hour, data in enumerate(hourly_forecasts):
            # Simulation logic to fill schedule
            self.schedule.append({
                "hour": hour,
                "mode": "ECONOMY" if 10 <= hour <= 16 else "PEAK_SHAVING"
            })
        return self.schedule