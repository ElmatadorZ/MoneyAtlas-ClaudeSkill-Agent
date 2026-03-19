# cli/run_analysis.py

from core.genesis_protocol import GenesisProtocol
from core.first_principle_codex import FirstPrincipleCodex
from core.ai_fluency_4d import AIFluency4D
from core.discernment_engine import DiscernmentEngine
from core.decision_engine import DecisionEngine
from core.meta_cognition import MetaCognition
from orchestrator.multi_agent_orchestrator import MultiAgentOrchestrator


def main():

    problem = "Should we invest in gold now?"
    context = {}

    gp = GenesisProtocol()
    state = gp.initialize(problem, context)

    fp = FirstPrincipleCodex()
    decomposition = fp.deconstruct(problem)

    af = AIFluency4D()
    structured = af.apply(decomposition)

    orchestrator = MultiAgentOrchestrator()
    analysis = orchestrator.run(structured)

    de = DiscernmentEngine()
    verified = de.evaluate(analysis)

    decider = DecisionEngine()
    decision = decider.decide([
        {"name": "buy", "reward": 8, "risk": 5},
        {"name": "wait", "reward": 5, "risk": 2}
    ])

    meta = MetaCognition()
    audit = meta.audit(decision)

    print({
        "analysis": analysis,
        "verified": verified,
        "decision": decision,
        "audit": audit
    })


if __name__ == "__main__":
    main()
