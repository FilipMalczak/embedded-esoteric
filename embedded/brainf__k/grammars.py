from embedded.brainf__k.abstract import AbstractGrammar
from embedded.brainf__k.instructions import *


class BrainfuckGrammar(AbstractGrammar):
    char_to_instruction_dict = {
        ">": IncPointer,
        "<": DecPointer,
        "+": IncValue,
        "-": DecValue,
        ",": GetChar,
        ".": PutChar,
        "[": Loop
    }

    loop_start_char = "["
    loop_end_char = "]"
