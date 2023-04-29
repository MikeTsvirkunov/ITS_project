from Interfaces.ICommand import ICommand
from ScopeBasedResolveDependencyStrategy import ScopeBasedResolveDependencyStrategy

class RegisterIoCDependencyCommand(ICommand):
    def __init__(self, key: str, f: callable) -> None:
        self.__key = key
        self.__f = f
    
    def action(self) -> None:
        try:
            ScopeBasedResolveDependencyStrategy().curent_scopes.value.storage[self.__key] = self.__f
        except:
            raise Exception('Не удалось зарегистрировать зависимость')
        