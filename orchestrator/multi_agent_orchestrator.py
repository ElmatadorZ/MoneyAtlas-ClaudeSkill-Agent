# orchestrator/multi_agent_orchestrator.py

from agents.analyst_agent import AnalystAgent
from agents.strategist_agent import StrategistAgent
from agents.skeptic_agent import SkepticAgent
from agents.macro_agent import MacroAgent

class MultiAgentOrchestrator:

    def __init__(self):
        self.analyst = AnalystAgent()
        self.strategist = StrategistAgent()
        self.skeptic = SkepticAgent()
        self.macro = MacroAgent()

    def run(self, data):
        a = self.analyst.run(data)
        s = self.strategist.run(a)
        sk = self.skeptic.run(a)
        m = self.macro.run(data)

        return {
            "analysis": a,
            "strategy": s,
            "critique": sk,
            "macro": m
        }
