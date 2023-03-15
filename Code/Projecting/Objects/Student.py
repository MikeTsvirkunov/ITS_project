from .Interfaces.IExtendAble import IExtendAble
from .Interfaces.IContainer import IContainer


class Student(IContainer):
    
    def __init__(self, 
                 container_of_know_discriptors: IContainer, 
                 container_of_can_discriptors: IContainer, 
                 container_of_master_discriptors: IContainer
                 ) -> None:
        super().__init__()

        self._container_of_know_discriptors = container_of_know_discriptors

        self._container_of_can_discriptors = container_of_can_discriptors

        self._container_of_master_discriptors = container_of_master_discriptors

        self._common_container = {'know': self._container_of_know_discriptors, 
                                  'can': self._container_of_can_discriptors, 
                                  'master': self._container_of_master_discriptors}
    
    
    def add(self, data: dict) -> None:
        for i in data:
            self._common_container[i].add(data[i].get())
    
    def get(self) -> None:
        return self._common_container
