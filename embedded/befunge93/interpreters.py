from embedded.befunge93.abstract import AbstractBefungeInterpreter
from embedded.befunge93.grammars import Befunge93Grammar


class CustomBefungeInterpreter(AbstractBefungeInterpreter):
    def __init__(self, grammar):
        self._grammar = grammar

    def grammar(self):
        return self._grammar

class Befunge93Interpreter(AbstractBefungeInterpreter):
    def grammar(self):
        return Befunge93Grammar()
