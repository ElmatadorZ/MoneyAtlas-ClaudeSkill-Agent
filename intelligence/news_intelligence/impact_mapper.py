class ImpactMapper:

    def map(self, bias):

        impact = []

        if bias["risk_off"] > 0:
            impact.append({
                "asset": "gold",
                "direction": "bullish"
            })

        if bias["bearish"] > 0:
            impact.append({
                "asset": "equities",
                "direction": "bearish"
            })

        return impact
