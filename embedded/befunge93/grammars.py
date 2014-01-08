from embedded.befunge93.abstract import AbstractGrammar
from embedded.befunge93.instructions import *


class CaseSensitiveBefunge93Grammar(AbstractGrammar):
    string_char = '"'
    stop_char = "@"

    digits = "0123456789"

    char_to_instruction_dict = {
        "+": add,
        "-": substract,
        "*": multiply,
        "/": divide,
        "%": modulo,
        "!": negate,
        "`": greater,
        "<": left,
        ">": right,
        "^": up,
        "v": down,
        "?": rand,
        "_": horizontal_cond,
        "|": vertical_cond,
        ":": duplicate,
        "\\": swap,
        "$": pop,
        ".": print_int,
        ",": print_ascii,
        "#": trampoline,
        "p": put,
        "g": get,
        "&": read_int,
        "~": read_ascii,
        " ": nothing
    }

class CaseInsensitiveBefunge93Grammar(AbstractGrammar):
    string_char = CaseSensitiveBefunge93Grammar.string_char
    stop_char = CaseSensitiveBefunge93Grammar.stop_char
    digits = CaseSensitiveBefunge93Grammar.digits
    char_to_instruction_dict = dict(
        V=down,
        P=put,
        G=get,
        **CaseSensitiveBefunge93Grammar.char_to_instruction_dict
    )

Befunge93Grammar = CaseSensitiveBefunge93Grammar