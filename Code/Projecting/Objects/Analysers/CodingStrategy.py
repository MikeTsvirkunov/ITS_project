from Interfaces.IStrategy import IStrategy
from keras.models import Sequential


class ExtractWordsStrategy(IStrategy):
    def __init__(self, codding_model: Sequential) -> None:
        self.codding_model = codding_model

    def execute(self, *args) -> any:
        return self.codding_model(args[0]).predict()
