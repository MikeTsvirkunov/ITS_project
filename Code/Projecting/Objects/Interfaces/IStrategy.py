from abc import ABC, abstractmethod


class IStrategy(ABC):
    @abstractmethod
    def execute(self, *args) -> any:
        pass
