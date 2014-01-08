from embedded.brainf__k.tokenizer import tokenizer


class JITCompiler:
    def __init__(self, instruction_classes):
        self.chars_to_instr = {}
        for instr_class in instruction_classes:
            for c in instr_class.chars:
                self.chars_to_instr[c] = instr_class

    def compile_next_char(self, token_gen):
        char = next(token_gen)
        instr_class = self.chars_to_instr[char]
        instruction = instr_class(char, self, token_gen)
        return instruction

    def compile(self, code):
        token_gen = tokenizer(code, list(self.chars_to_instr.keys()))
        try:
            while 1:
                yield self.compile_next_char(token_gen)
        except StopIteration:
            pass