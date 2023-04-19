from abc import ABC, abstractmethod


class IScope(ABC):

    @abstractmethod
    def resolve(self, key, **args) -> any:
        pass
