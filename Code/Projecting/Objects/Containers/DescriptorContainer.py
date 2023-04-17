from ...Objects.Interfaces.IContainer import IContainer
from ...Objects.Interfaces.INamedObject import INamedObject
from ...Objects.Interfaces.IExtendAble import IExtendAble


class DescriptorContainer(IContainer, INamedObject, IExtendAble):
    def __init__(self, name: str, subjects: iter = []) -> None:
        self.__name = name
        self.__subjects = dict([(subject, []) for subject in subjects])

    def getAll(self) -> dict:
        return self.__subjects

    def getValue(self, key) -> any:
        return self.__subjects[key]

    def isIn(self, key) -> bool:
        return key in self.__subjects

    def extend(self, key, value) -> None:
        self.__subjects[key] = value

    def getName(self) -> str:
        return self.__name
