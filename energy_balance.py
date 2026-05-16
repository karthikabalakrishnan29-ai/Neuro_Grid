from utils.logger import logger

class EnergyBalancer:
    def __init__(self):
        pass

    def calculate_balance(self, solar_pw, wind_pw, load_demand):
        """
        Net Power = (Solar + Wind) - Load
        Positive result: Excess power (Charge battery)
        Negative result: Deficit (Discharge battery or use Grid/Gen)
        """
        total_gen = solar_pw + wind_pw
        net_power = total_gen - load_demand
        
        logger.info(f"Balance Calc: Gen={round(total_gen, 2)}kW, Load={round(load_demand, 2)}kW, Net={round(net_power, 2)}kW")
        return round(net_power, 4)