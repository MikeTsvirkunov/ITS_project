from abc import ABC, abstractmethod


class IContainer(ABC):
    
    @abstractmethod
    def getAll(self) -> dict:
        pass

    @abstractmethod
    def isIn(self, key) -> bool:
        pass

    @abstractmethod
    def getValue(self, key) -> any:
        pass
