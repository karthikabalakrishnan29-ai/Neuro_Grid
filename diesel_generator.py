class DieselGenerator:
    def __init__(self, max_output=20.0, fuel_efficiency=0.3):
        self.max_output = max_output
        self.fuel_efficiency = fuel_efficiency # Liters per kWh (Approx)

    def get_generation(self, required_power):
        generation = min(required_power, self.max_output)
        fuel_consumed = generation * self.fuel_efficiency
        return round(generation, 4), round(fuel_consumed, 4)