from .Interfaces.ICommand import ICommand


class JsonDeepSearcherCommand(ICommand):

    def __init__(self, json: dict, f: callable) -> None:
        super().__init__()
        self.json = json
        self.f = f

    def action(self) -> None:
        for i in self.json:
            if not (type(self.json[i]) is dict):
                self.f(i, self.json[i])
            else:
                JsonDeepSearcherCommand(self.json[i], self.f).action()

