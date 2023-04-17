from abc import ABC, abstractmethod


class INamedObject(ABC):
    @abstractmethod
    def getName(self) -> str:
        pass
