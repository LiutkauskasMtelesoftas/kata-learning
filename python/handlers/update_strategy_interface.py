from abc import ABC, abstractmethod

class UpdateStrategyInterface:
    def update(self, item) -> None:
        pass
