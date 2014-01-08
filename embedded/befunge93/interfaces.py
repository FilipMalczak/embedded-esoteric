class InstructionInterface:
    def __call__(self, runtime):
        '''
        Execute this instruction in given runtime
        '''

class GrammarInterface:
    # in Befunge93 these are (in order) " and @
    string_char = ""
    stop_char = ""

    #these should be string containing all characters treated as digits,
    # probably just 0123456789
    digits = ""

    #TODO: add configurable space as empty character
    # as for now space should be connected to lambda r: pass

    def digit_to_number(self, digit_char: str) -> int:
        '''
        This function should translate digit character to int
        '''

    def instruction_for_char(self, char: str) -> InstructionInterface:
        '''
        This function should return callable with __call__ signature matching
        this of InstructionInterface
        '''
