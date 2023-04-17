from Interfaces.IContainer import IContainer
from Interfaces.INamedObject import INamedObject


class KCMContainer(IContainer, INamedObject):
    def __init__(self, name: str, know: float = 0, can: float = 0, master: float = 0):
        self.__name = name
        self.__kcm = {'know': know, 'can': can, 'master': master}
    
    def getAll(self) -> dict:
        return self.__kcm

    def getValue(self, key) -> any:
        return self.__kcm[key]

    def isIn(self, key) -> bool:
        return key in self.__kcm

    def add(self, key, value) -> None:
        self.__kcm[key] = value
    
    def getName(self) -> str:
        return self.__name
