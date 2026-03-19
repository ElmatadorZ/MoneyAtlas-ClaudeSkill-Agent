# agents/portfolio_agent.py

from .base_agent import BaseAgent, AgentOutput

class PortfolioAgent(BaseAgent):
    name = "portfolio"

    async def run(self, context):

        macro = context["macro"]["macro_bias"]
        risk = context["risk"]["risk_level"]

        if macro == "bearish" and risk == "high":
            decision = "Reduce exposure"
        else:
            decision = "Hold / Accumulate"

        return AgentOutput(
            name=self.name,
            data={"decision": decision},
            confidence=0.8,
            reasoning=f"Macro={macro}, Risk={risk}"
        )
