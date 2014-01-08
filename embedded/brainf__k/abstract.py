from embedded.brainf__k.interfaces import GrammarInterface
from embedded.brainf__k.jit import JITCompiler
from embedded.brainf__k.runtime import Brainf__kRuntime
from embedded.exceptions import AbstractMethodException


class AbstractBrainf__kInterpreter:
    def grammar(self):
        raise AbstractMethodException()

    def execute(self, code, runtime=None, ticker=None):
        '''
        code is string with brainf__k code
        runtime may be passed, for code to run in predefined environment
        ticker is TickerInterface implementation passed to used tokenizer. It may
            be useful while debugging. It will count ALL characters, not only
            those recognized as brainf__k instructions.
        '''
        if runtime is None:
            runtime = Brainf__kRuntime()
        jit = JITCompiler(self.grammar())
        instruction_gen = jit.compile(code, ticker)
        try:
            while 1:
                instr = next(instruction_gen)
                instr.execute(runtime)
        except StopIteration:
            pass
        return runtime

class AbstractGrammar(GrammarInterface):
    def valid_characters(self):
        return "".join(
            type(self).char_to_instruction_dict.keys()
        )+type(self).loop_end_char

    def instruction_class_for_char(self, char):
        if char == type(self).loop_end_char:
            char = type(self).loop_start_char
        return type(self).char_to_instruction_dict[char]


