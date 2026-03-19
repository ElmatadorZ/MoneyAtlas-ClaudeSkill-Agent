# memory/memory_store.py

import json
from typing import Dict, Any

class MemoryStore:

    def __init__(self, path="memory.json"):
        self.path = path
        self.memory = self._load()

    def _load(self):
        try:
            with open(self.path, "r") as f:
                return json.load(f)
        except:
            return {}

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.memory, f, indent=2)

    def log_decision(self, decision: Dict[str, Any]):
        if "history" not in self.memory:
            self.memory["history"] = []
        self.memory["history"].append(decision)
        self.save()

    def get_history(self):
        return self.memory.get("history", [])
