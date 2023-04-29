from Interfaces.ICommand import ICommand
from ScopeBasedResolveDependencyStrategy import ScopeBasedResolveDependencyStrategy
from Scope import Scope


class SetScopeInCurrentThreadCommand(ICommand):
    def __init__(self, scope: Scope) -> None:
        super().__init__()
        self.__scope: Scope = scope
    
    def action(self) -> None:
        ScopeBasedResolveDependencyStrategy().curent_scopes.value = self.__scope

