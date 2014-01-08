from array import array
import sys
from embedded.brainf__k.jit import JITCompiler
from embedded.brainf__k.tokenizer import tokenizer


class Brainf__kRuntime:
    def __init__(self, size=30000, stdout=sys.stdout, stdin=sys.stdin):
        self.buffer = array("B")
        self.maxsize = size
        self.stdout = stdout
        self.stdin = stdin
        self.pointer = 0

class AbstractBrainf__kInterpreter:
    def execute(self, code, runtime=None):
        if runtime is None:
            runtime = Brainf__kRuntime()
        jit = JITCompiler(self.get_instruction_classes())
        instruction_gen = jit.compile(code)
        try:
            while 1:
                instr = next(instruction_gen)
                instr.execute(runtime)
        except StopIteration:
            pass
