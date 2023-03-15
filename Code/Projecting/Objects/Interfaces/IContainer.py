from abc import ABC, abstractmethod


class IContainer(ABC):

    @abstractmethod
    def add(self, data) -> None:
        pass
    
    @abstractmethod
    def get(self) -> dict:
        pass
