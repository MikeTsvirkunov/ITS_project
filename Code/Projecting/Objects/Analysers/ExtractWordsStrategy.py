from Interfaces.IStrategy import IStrategy


class ExtractWordsStrategy(IStrategy):
    def __init__(self, nlp) -> None:
        self.nlp = nlp
    
    def execute(self, *args) -> any:
        return self.nlp(args[0]).ents
