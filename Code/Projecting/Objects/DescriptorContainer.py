from .Interfaces.IContainer import IContainer

class DescriptorContainer(IContainer):

    def __init__(self, list_of_descriptors: iter=[]) -> None:
        super().__init__()
        self._discriptors = dict(map(lambda a: (a, 0), list_of_descriptors))


    def add(self, data: dict) -> None:
        for i in data:
            self._discriptors += self.discriptors.setdefault(i, 0) + data[i]

    def get(self):
        return self._discriptors
