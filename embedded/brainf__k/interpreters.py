from embedded.brainf__k.instructions import *
from embedded.brainf__k.internals import AbstractBrainf__kInterpreter


class BrainfuckInterpreter(AbstractBrainf__kInterpreter):
    def get_instruction_classes(self):
        return [
            IncPointer,
            DecPointer,
            IncValue,
            DecValue,
            GetChar,
            PutChar,
            Loop
        ]

if __name__=="__main__":
    code = '''++++++++++
[
>+++++++>++++++++++>+++>+<<<<-
] Na początek ustawiamy kilka przydatnych później wartości
>++.               drukuje 'H'
>+.                drukuje 'e'
+++++++.           drukuje 'l'
.                  drukuje 'l'
+++.               drukuje 'o'
>++.               spacja
<<+++++++++++++++. drukuje 'W'
>.                 drukuje 'o'
+++.               drukuje 'r'
------.            drukuje 'l'
--------.          drukuje 'd'
>+.                drukuje '!'
>.                 nowa linia'''
    interpreter = BrainfuckInterpreter()
    interpreter.execute(code)