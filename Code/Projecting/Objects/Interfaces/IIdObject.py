from abc import ABC, abstractmethod


class IIdObject(ABC):

    @abstractmethod
    def getId(self) -> str:
        pass
