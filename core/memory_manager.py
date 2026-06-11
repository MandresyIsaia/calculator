# core/memory_manager.py

class MemoryManager:
    def __init__(self):
        self._memory_value = 0.0
        self._history = []

    def clear(self):
        self._memory_value = 0.0
        self._history.append("MC : Mémoire réinitialisée à 0")

    def recall(self):
        return self._memory_value

    def add(self, value):
        self._memory_value += value
        self._history.append(f"M+ : +{value} (Total: {self._memory_value})")

    def subtract(self, value):
        self._memory_value -= value
        self._history.append(f"M- : -{value} (Total: {self._memory_value})")

    def store(self, value):
        self._memory_value = value
        self._history.append(f"MS : Stocké {value}")

    def get_history(self):
        return self._history