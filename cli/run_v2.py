# cli/run_v2.py

from memory.memory_store import MemoryStore
from memory.learning_engine import LearningEngine
from backtest.backtest_engine import BacktestEngine
from signals.signal_engine import SignalEngine
from evolution.reinforcement import ReinforcementEngine

def main():

    # Initialize systems
    memory = MemoryStore()
    learner = LearningEngine()
    backtest = BacktestEngine()
    signal_engine = SignalEngine()
    reinforce = ReinforcementEngine()

    # Mock SMC Layer Output
    smc_layers = [
        type("Layer", (), {
            "state": "accumulating",
            "confidence": 0.8,
            "cost_basis": 1900
        })()
    ]

    # Generate signals
    signals = signal_engine.generate(smc_layers)

    # Backtest
    results = backtest.run(signals)

    # Log results
    for r in results:
        memory.log_decision(r)

    # Learn
    history = memory.get_history()
    performance = learner.evaluate_performance(history)

    # Reinforce
    updated = reinforce.update(signals, performance)

    print({
        "signals": signals,
        "performance": performance,
        "updated": updated
    })


if __name__ == "__main__":
    main()
