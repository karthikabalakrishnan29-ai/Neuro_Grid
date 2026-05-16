from utils.logger import logger

class DemandResponseManager:
    def __init__(self, price_threshold=8.0):
        self.price_threshold = price_threshold

    def evaluate_response(self, current_price):
        """
        Price threshold-a thaanduna, non-critical loads-a shift panna order anupum.
        """
        if current_price > self.price_threshold:
            logger.warning(f"High Price Alert (₹{current_price}). Triggering Demand Response.")
            return {
                "action": "SHIFT_LOAD",
                "target_devices": ["EV_Charger", "HVAC_System"],
                "status": "ACTIVE"
            }
        return {"action": "NONE", "status": "STABLE"}