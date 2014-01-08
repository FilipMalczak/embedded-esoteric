from embedded.brainf__k.tokenizer import tokenizer

class JITCompiler:
    def __init__(self, grammar):
        self.grammar = grammar

    def compile_next_char(self, token_gen):
        char = next(token_gen)
        instr_class = self.grammar.instruction_class_for_char(char)
        instruction = instr_class(char, self, token_gen)
        return instruction

    def compile(self, code, ticker=None):
        token_gen = tokenizer(code, self.grammar.valid_characters(), ticker)
        try:
            while 1:
                yield self.compile_next_char(token_gen)
        except StopIteration:
            pass