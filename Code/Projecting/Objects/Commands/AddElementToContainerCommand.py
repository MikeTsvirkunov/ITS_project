from Interfaces.ICommand import ICommand
from Interfaces.IExtendAble import IExtendAble


class AddElementToContainerCommand(ICommand):
    def __init__(self, container: IExtendAble, key: any, value: any) -> None:
        self.__container = container
        self.__key = key
        self.__value = value
    
    def action(self) -> None:
        self.__container.extend(self.__key, self.__value)
