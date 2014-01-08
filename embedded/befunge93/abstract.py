from embedded.befunge93.interfaces import GrammarInterface
from embedded.befunge93.runtime import Runtime
from embedded.exceptions import AbstractMethodException


class AbstractBefungeInterpreter:
    def grammar(self) -> GrammarInterface:
        raise AbstractMethodException()

    #hook is executed right after defining active cell
    def execute(self, code: str, runtime: Runtime=None, hook = lambda runtime: None):
        if runtime is None:
            runtime = Runtime()
        runtime.space.inject_code(code)
        grammar = self.grammar()
        string_mode = False
        active = runtime.space.active_cell()
        hook(runtime)
        while not active == grammar.stop_char:
            if active == grammar.string_char:
                string_mode = not string_mode
            elif active in grammar.digits:
                number = grammar.digit_to_number(active)
                runtime.stack.append(number)
            else:
                if string_mode:
                    runtime.stack.append(ord(active))
                else:
                    instruction = grammar.instruction_for_char(active)
                    instruction(runtime)
            runtime.space.move()
            active = runtime.space.active_cell()
            hook(runtime)
        return  runtime

class AbstractGrammar(GrammarInterface):
    def digit_to_number(self, digit_char: str) -> int:
        return int(digit_char)

    def instruction_for_char(self, char: str) -> callable:
        return type(self).char_to_instruction_dict[char]