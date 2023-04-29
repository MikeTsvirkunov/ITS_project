from IScope import IScope


class LeafScope(IScope):
    def __init__(self, f: callable) -> None:
        self.__f = f
    
    def resolve(self, key, **args) -> any:
        return self.__f(key, args)