# strategy/asymmetric_engine.py

class AsymmetricEngine:

    def find(self, alpha, macro, geo):

        opportunities = []

        for a in alpha:

            if a["type"] == "SMART_MONEY_ENTRY":
                if macro["risk_asset_bias"] == "bearish":
                    opportunities.append({
                        "type": "CONTRARIAN_SETUP",
                        "logic": "smart money vs macro fear",
                        "conviction": "high"
                    })

        return opportunities
