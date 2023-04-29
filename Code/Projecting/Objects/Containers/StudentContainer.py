from ...Objects.Interfaces.IContainer import IContainer
from ...Objects.Interfaces.IIdObject import IIdObject
from ...Objects.Interfaces.IExtendAble import IExtendAble


class StudentContainer(IContainer, IIdObject, IExtendAble):
    def __init__(self, id: str, subjects: iter=[]) -> None:
        self.__id = id
        self.__subjects = dict([(subject, []) for subject in subjects])
    
    def getAll(self) -> dict:
        return self.__subjects
    
    def getValue(self, key) -> any:
        return self.__subjects[key]

    def isIn(self, key) -> bool:
        return key in self.__subjects

    def extend(self, key, value) -> None:
        self.__subjects[key] = value
    
    def getId(self) -> str:
        return self.__id
    
    