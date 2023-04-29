from Interfaces.ICommand import ICommand
from Interfaces.IExtendAble import IExtendAble
from Containers.KCMContainer import KCMContainer


class SumOfKCMContainersCommand(ICommand):
    def __init__(self, kcm_container_to_increas: KCMContainer, kcm_container_to_add: KCMContainer) -> None:
        self.__kcm_container_to_increas = kcm_container_to_increas
        self.__kcm_container_to_add = kcm_container_to_add
    
    def action(self) -> None:
        if self.__kcm_container_to_increas.getName() != self.__kcm_container_to_add.getName():
            raise Exception(
                f'Incorect names of KCMContainer\'s: {self.__kcm_container_to_increas.getName()} != {self.__kcm_container_to_add.getName()}')
        for i in self.__kcm_container_to_add.getAll():
            self.__kcm_container_to_increas.getAll()[i] += self.__kcm_container_to_add.getAll()[i]

            
        
