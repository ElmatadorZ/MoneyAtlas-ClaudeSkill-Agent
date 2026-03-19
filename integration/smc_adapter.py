# integration/smc_adapter.py

class SMCAdapter:

    def integrate(self, smc_output, cognitive_output):
        return {
            "market_structure": smc_output,
            "decision_layer": cognitive_output
        }
