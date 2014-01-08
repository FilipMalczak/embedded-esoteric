# For more examples see: http://www.hevanet.com/cristofd/brainfuck/
# I don't guarantee that examples won't be repeated
import traceback
import sys
from embedded.brainf__k.interpreters import BrainfuckInterpreter
from embedded.utils.ticker import Ticker


hello_world = '''++++++++++
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
#source: polish wikipedia

fibbonacci = '''+++++++++++
>+>>>>++++++++++++++++++++++++++++++++++++++++++++
>++++++++++++++++++++++++++++++++<<<<<<[>[>>>>>>+>
+<<<<<<<-]>>>>>>>[<<<<<<<+>>>>>>>-]<[>++++++++++[-
<-[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<[>>>+<<<
-]>>[-]]<<]>>>[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]
>[<<+>>[-]]<<<<<<<]>>>>>[+++++++++++++++++++++++++
+++++++++++++++++++++++.[-]]++++++++++<[->-<]>++++
++++++++++++++++++++++++++++++++++++++++++++.[-]<<
<<<<<<<<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<-[>>.>.<<<
[-]]<<[>>+>+<<<-]>>>[<<<+>>>-]<<[<+>-]>[<+>-]<<<-]'''
#source: http://esoteric.sange.fi/brainfuck/bf-source/prog/fibonacci.txt

examples = [
    ("Hello world", hello_world),
    ("Fibbonacci sequence", fibbonacci)
]

def execute_example(interpreter, name, code):
    try:
        ticker = Ticker()
        print(name, "in Brainfuck")
        print("-"*80)
        interpreter.execute(code, ticker=ticker)
        print("<EOF>")
        print("-"*80)
    except BaseException:
        traceback.print_exc(file=sys.stdout)
        ticks = ticker.get_ticks()
        start = ticks-10
        if start<0:
            start=0
        end = ticks+10
        print("Error at character #"+str(ticks))
        print("\t"+(code[start:end].replace("\n", "\\n")))
        print("\t"+(" "*start)+"^")
        raise


interpreter = BrainfuckInterpreter()
for example in examples:
    execute_example(interpreter, *example)