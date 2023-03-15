from abc import ABC, abstractmethod

class IExtendAble(ABC):
    
    @abstractmethod
    def extend(self, data) -> None:
        pass