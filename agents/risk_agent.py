# agents/risk_agent.py

from .base_agent import BaseAgent, AgentOutput

class RiskAgent(BaseAgent):
    name = "risk"

    async def run(self, context):
        return AgentOutput(
            name=self.name,
            data={"risk_level": "high"},
            confidence=0.75,
            reasoning="Volatility expansion likely"
        )
