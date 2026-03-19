from .base_agent import BaseAgent, AgentOutput
from smc.smc_wrapper import SMCWrapper


class SMCAgent(BaseAgent):
    name = "smc"

    def __init__(self):
        self.wrapper = SMCWrapper()

    async def run(self, context):

        smc_data = await self.wrapper.analyze(context)

        return AgentOutput(
            name=self.name,
            data=smc_data,
            confidence=0.85,
            reasoning=smc_data["summary"]
        )
