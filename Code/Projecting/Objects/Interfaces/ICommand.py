from abc import ABC, abstractmethod


class ICommand(ABC):

    @abstractmethod
    def action(self) -> None:
        pass
