from Scope import Scope
from threading import local

class ScopeBasedResolveDependencyStrategy:
    root: Scope = None
    default_scope = lambda: ScopeBasedResolveDependencyStrategy.Root
    curent_scopes: local = local()
    
    @staticmethod
    def resolve(self, key: str, **args):
        if key != 'Scope.Root':
            if ScopeBasedResolveDependencyStrategy.curent_scope == None:
                return ScopeBasedResolveDependencyStrategy.default_scope().resolve(key, args)
            else:
                return ScopeBasedResolveDependencyStrategy.curent_scope.value.resolve(key, args)
        return ScopeBasedResolveDependencyStrategy.Root
