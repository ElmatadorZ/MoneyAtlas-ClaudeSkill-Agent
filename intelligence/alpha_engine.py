# intelligence/alpha_engine.py

class AlphaEngine:

    def detect(self, smc_layers):

        alpha = []

        for l in smc_layers:

            if l.state == "accumulating" and l.confidence > 0.75:
                alpha.append({
                    "type": "SMART_MONEY_ENTRY",
                    "layer": l.layer,
                    "price": l.cost_basis,
                    "edge": "institutional accumulation"
                })

            if l.state == "distributing":
                alpha.append({
                    "type": "EXIT_SIGNAL",
                    "layer": l.layer,
                    "risk": "distribution detected"
                })

        return alpha
