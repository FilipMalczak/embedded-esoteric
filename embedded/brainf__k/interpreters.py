from embedded.brainf__k.grammars import BrainfuckGrammar
from embedded.brainf__k.abstract import AbstractBrainf__kInterpreter

class BrainfuckInterpreter(AbstractBrainf__kInterpreter):
    def grammar(self):
        return BrainfuckGrammar()

#TODO: create Brainfork interpreter