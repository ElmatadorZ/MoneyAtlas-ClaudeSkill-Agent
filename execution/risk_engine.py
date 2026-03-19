class RiskEngine:

    def __init__(self, capital: float, risk_per_trade: float = 0.01):
        self.capital = capital
        self.risk_per_trade = risk_per_trade

    def calculate_position_size(self, entry, stop_loss):

        risk_amount = self.capital * self.risk_per_trade
        risk_per_unit = abs(entry - stop_loss)

        if risk_per_unit == 0:
            return 0

        position_size = risk_amount / risk_per_unit
        return position_size
