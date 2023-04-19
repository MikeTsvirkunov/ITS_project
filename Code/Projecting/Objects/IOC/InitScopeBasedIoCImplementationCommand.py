from Interfaces.ICommand import ICommand
from Scope import Scope
from LeafScope import LeafScope
from IScope import IScope
from IOCContainer import IOCContainer
from ScopeBasedResolveDependencyStrategy import ScopeBasedResolveDependencyStrategy
from SetScopeInCurrentThreadCommand import SetScopeInCurrentThreadCommand
from RegisterIoCDependencyCommand import RegisterIoCDependencyCommand


class InitScopeBasedIoCImplementationCommand(ICommand):
    def action(self) -> None:
        if (ScopeBasedResolveDependencyStrategy().root == None):
            storage = dict()
            scope = Scope(parent_scope=LeafScope(IOCContainer().resolve(key='IOC.Default')),
                        storage=storage)
            storage['Scopes.Storage'] = lambda *args: dict()
            storage['Scopes.New'] = lambda *args: Scope(storage=IOCContainer.resolve(key='Scopes.Storage'),
                                                        parent_scope=args[0])
            storage['Scopes.Current'] = lambda *args: max(ScopeBasedResolveDependencyStrategy().current_scopes.value, 
                                                          ScopeBasedResolveDependencyStrategy().default_scope, 
                                                          key=lambda a: a != None)
            storage['Scopes.Current.Set'] = lambda *args: SetScopeInCurrentThreadCommand(Scope(args[0]))
            storage['IOC.Register'] = lambda *args: RegisterIoCDependencyCommand(args[0], args[1])
            ScopeBasedResolveDependencyStrategy().root = scope
            IOCContainer.resolve('IOC.SetupStrategy', ScopeBasedResolveDependencyStrategy.resolve).action()
            SetScopeInCurrentThreadCommand(scope).action()
        

