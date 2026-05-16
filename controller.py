from .setpoint_manager import SetpointManager
from .load_shedding import LoadSheddingManager
from .actuator_interface import ActuatorInterface
from utils.logger import logger

class MainController:
    def __init__(self):
        self.setpoints = SetpointManager()
        self.shedding = LoadSheddingManager()
        self.actuator = ActuatorInterface()

    def process_control_loop(self, current_metrics):
        """
        Input: {'net_power': -15.0, 'voltage': 228.0, ...}
        """
        net_p = current_metrics.get('net_power', 0)
        
        # 1. Check if Load Shedding is needed
        if net_p < -5.0:
            shed_actions = self.shedding.execute_shedding(abs(net_p))
            for action in shed_actions:
                self.actuator.send_signal(action['device'], action['action'])

        # 2. Maintain Voltage Stability
        if current_metrics.get('voltage', 230) < 220:
            logger.info("Voltage Low: Triggering Inverter Boost.")
            self.actuator.send_signal("Main_Inverter", "BOOST_MODE")

        return {"status": "Control Loop Executed"}