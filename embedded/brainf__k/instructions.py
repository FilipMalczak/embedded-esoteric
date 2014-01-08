from embedded.brainf__k.exceptions import Brainf__kSyntaxError


class AbstractInstruction:
    chars = ""

    def execute(self, runtime):
        pass

    def __init__(cls, char, jit_compiler, token_gen):
        pass

def ensure_valid_address(array, address):
    if len(array)<=address:
        array.extend(0 for i in range(address-len(array)+1))

class IncPointer(AbstractInstruction):
    chars = ">"

    def execute(self, runtime):
        runtime.pointer+=1

class DecPointer(AbstractInstruction):
    chars = "<"

    def execute(self, runtime):
        runtime.pointer-=1

class IncValue(AbstractInstruction):
    chars = "+"

    def execute(self, runtime):
        ensure_valid_address(runtime.buffer, runtime.pointer)
        runtime.buffer[runtime.pointer] += 1

class DecValue(AbstractInstruction):
    chars = "-"

    def execute(self, runtime):
        ensure_valid_address(runtime.buffer, runtime.pointer)
        runtime.buffer[runtime.pointer] -= 1

class GetChar(AbstractInstruction):
    chars = ","

    def execute(self, runtime):
        #todo: ensure thread safety
        #TODO: ensure that stdin reads chars
        byte_ = ord(runtime.stdin.read(1)) % 256
        ensure_valid_address(runtime.buffer, runtime.pointer)
        runtime.buffer[runtime.pointer] = byte_

class PutChar(AbstractInstruction):
    chars = "."

    def execute(self, runtime):
        ensure_valid_address(runtime.buffer, runtime.pointer)
        runtime.stdout.write(chr(runtime.buffer[runtime.pointer]))

class LoopEnd(Exception):
    pass

class Loop(AbstractInstruction):
    start_char = "["
    stop_char = "]"
    chars = start_char+stop_char


    def __init__(self, char, jit_compiler, token_gen):
        if char == type(self).stop_char:
            raise LoopEnd()
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
        ensure_valid_address(runtime.buffer, runtime.pointer)
        while runtime.buffer[runtime.pointer]:
            for instruction in self.instructions:
                instruction.execute(runtime)
