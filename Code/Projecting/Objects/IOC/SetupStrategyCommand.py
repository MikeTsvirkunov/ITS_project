from Interfaces.ICommand import ICommand
from IOCContainer import IOCContainer


class SetupStrategyCommand(ICommand):
    def __init__(self, new_strategy: callable) -> None:
        super().__init__()
        self.__new_strategy = new_strategy

    def action(self) -> None:
        IOCContainer().strategy = self.__new_strategy
