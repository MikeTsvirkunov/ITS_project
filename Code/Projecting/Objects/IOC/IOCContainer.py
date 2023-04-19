# from SetupStrategyCommand import SetupStrategyCommand
from Interfaces.ICommand import ICommand


class IOCContainer:
    def __init__(self) -> None:
        self.strategy: callable = self.defaultStrategy

    def resolve(self, key: str, *args):
        return self.strategy(key, args)

    def defaultStrategy(self, key: str, *args):
        if (key == "IOC.SetupStrategy"):
            return SetupStrategyCommand(args[0])
        if (key == 'IOC.Default'):
            return IOCContainer.defaultStrategy     
        raise ValueError(f'Unknown IoC dependency key {key}. Make sure that {key} has been registered before try to resolve the dependnecy')


class SetupStrategyCommand(ICommand):
    def __init__(self, new_strategy: callable) -> None:
        super().__init__()
        self.__new_strategy = new_strategy

    def action(self) -> None:
        IOCContainer().strategy = self.__new_strategy
