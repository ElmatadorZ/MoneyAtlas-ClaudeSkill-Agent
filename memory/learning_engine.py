# memory/learning_engine.py

class LearningEngine:

    def evaluate_performance(self, history):
        wins = sum(1 for h in history if h.get("result") == "win")
        total = len(history)
        return wins / total if total > 0 else 0.0

    def adjust_strategy(self, performance):
        if performance < 0.5:
            return "reduce risk"
        elif performance > 0.7:
            return "increase position"
        return "maintain"
