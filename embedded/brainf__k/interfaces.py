class InstructionInterface:
    def execute(self, runtime):
        '''
        Execute given instruction in given runtime
        '''

    def __init__(self, char, jit_compiler, token_gen):
        '''
        Create given instruction.
        char is character that made compiler create this instance.
        jit_compiler is jit_compiler that is working at the moment.
        token_gen is generator with further tokens (without char).
        '''

class GrammarInterface:
    def valid_characters(self):
        '''
        Should return string containing valid characters for given dialect
        '''

    def instruction_class_for_char(self, char):
        '''
        Should return subclass of InstructionInterface for given character.
        We can assume that it won't be called with character that isn't in
        self.valid_characters()
        '''

    #fill it with equivalent of '[' and ']' from classic dialect (in that order)
    loop_start_char = ""
    loop_end_char = ""
