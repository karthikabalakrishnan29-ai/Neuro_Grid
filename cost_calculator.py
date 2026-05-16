class CostCalculator:
    def __init__(self):
        self.total_savings = 0.0
        self.total_expenditure = 0.0

    def update_costs(self, energy_kwh, price_per_unit, source):
        """
        source: 'RENEWABLE', 'GRID', 'BATTERY'
        """
        cost = energy_kwh * price_per_unit
        
        if source == 'RENEWABLE':
            # Renewables use panrathaala evlo kaasu save aaguthu
            self.total_savings += cost
        elif source == 'GRID':
            self.total_expenditure += cost
            
        return cost

    def get_roi_report(self):
        return {
            "Total Savings (₹)": round(self.total_savings, 2),
            "Operational Cost (₹)": round(self.total_expenditure, 2),
            "Net Benefit (₹)": round(self.total_savings - self.total_expenditure, 2)
        }