from embedded.exceptions import Brainf__kSyntaxError
from embedded.brainf__k.interfaces import InstructionInterface

class IncPointer(InstructionInterface):
    def execute(self, runtime):
        runtime.pointer+=1

class DecPointer(InstructionInterface):
    def execute(self, runtime):
        runtime.pointer-=1

class IncValue(InstructionInterface):
    def execute(self, runtime):
        runtime.buffer[runtime.pointer] += 1

class DecValue(InstructionInterface):
    def execute(self, runtime):
        runtime.buffer[runtime.pointer] -= 1

class GetChar(InstructionInterface):
    def execute(self, runtime):
        #todo: ensure thread safety
        #TODO: ensure that stdin reads chars
        byte_ = ord(runtime.stdin.read(1)) % 256
        runtime.buffer[runtime.pointer] = byte_

class PutChar(InstructionInterface):
    def execute(self, runtime):
        runtime.stdout.write(chr(runtime.buffer[runtime.pointer]))

class LoopEnd(Exception):
    pass

class Loop(InstructionInterface):

    def __init__(self, char, jit_compiler, token_gen):
        if char == jit_compiler.grammar.loop_end_char:
            raise LoopEnd() #TODO: can we do it nicer?
        self.instructions = []
        self.instructions.append(jit_compiler.compile_next_char(token_gen))
        try:
            while 1:
                self.instructions.append(jit_compiler.compile_next_char(token_gen))
        except LoopEnd:
            pass
        except StopIteration:
            raise Brainf__kSyntaxError("Cannot find matching %s" % type(self).stop_char)

    def execute(self, runtime):
        while runtime.buffer[runtime.pointer]:
            for instruction in self.instructions:
                instruction.execute(runtime)
