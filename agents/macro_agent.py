# agents/macro_agent.py

from .base_agent import BaseAgent, AgentOutput

class MacroAgent(BaseAgent):
    name = "macro"

    async def run(self, context):
        macro = context.get("macro_data", {})

        insight = "Liquidity tightening → risk assets under pressure"

        return AgentOutput(
            name=self.name,
            data={"macro_bias": "bearish"},
            confidence=0.7,
            reasoning=insight
        )
