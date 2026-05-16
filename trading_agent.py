class TradingAgent:
    def __init__(self):
        self.daily_revenue = 0.0

    def decide_trade(self, battery_soc, current_price, net_generation):
        """
        Logic:
        1. Battery full-ah irunthu, price-um nalla iruntha -> SELL.
        2. Battery low-ah irunthu, price kuraiva iruntha -> BUY.
        """
        decision = "HOLD"
        
        if net_generation > 0 and battery_soc > 90 and current_price > 7.0:
            decision = "SELL_TO_GRID"
        elif battery_soc < 20 and current_price < 5.0:
            decision = "BUY_FROM_GRID"
            
        return decision