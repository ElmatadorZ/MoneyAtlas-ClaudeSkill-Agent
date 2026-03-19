class RiskEngine:

    def evaluate(self, smc_layers):

        risks = []

        for layer in smc_layers:

            if layer.confidence < 0.5:
                risks.append(
                    f"Layer {layer.layer}: ความไม่แน่นอนสูง"
                )

            if layer.state == "distributing":
                risks.append(
                    f"Layer {layer.layer}: เสี่ยงต่อการปรับฐาน"
                )

        return risks
