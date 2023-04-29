from IScope import IScope


class Scope(IScope):
    def __init__(self, parent_scope: IScope, storage: dict=dict()) -> None:
        self.__parent_scope = parent_scope
        self.__storage = storage
    
    def resolve(self, key, *args) -> any:
        return self.__storage[key](args) if key in self.__storage else self.__parent_scope.resolve(key, args)
