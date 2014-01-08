import sys
import traceback
from embedded.befunge93.interpreters import Befunge93Interpreter
from embedded.befunge93.runtime import Runtime

#both "hello world"s come from english wiki
simple_hello_world = '''>              v
v  ,,,,,"Hello"<
>48*,          v
v,,,,,,"World!"<
>25*,@
'''

#am I wrong, or commented example shouldn't work?
#complicated_hello_world = '''>25*"!dlrow ,olleH":v
#                 v:,_@
#                 >  ^'''

less_or_more = '''vv  <      <
    2
    ^  v<
 v1<?>3v4
    ^   ^
>  >?>  ?>5^
    v   v
 v9<?>7v6
    v  v<
    8
    >  >   ^
 vv  <      <
     2
     ^  v<
  v1<?>3v4
     ^   ^
 >  >?>  ?>5^
     v   v      v          ,*25         <<
  v9<?>7v6                              ,,
     v  v<                              ""
     8                                  ><
     >  >   ^                           ""v
  >*:.>0"!rebmun tupnI">:#,_$25*,:&:99p`|^<       _0"!niw uoY">:#,_$25*,@
      ^         <                       >:99g01-*+^'''

factorial = '''0&>:1-:v v *_$.@
  ^    _$>\:^'''

erastotenes = '''2>:3g" "-!v\  g30          <
 |!`"O":+1_:.:03p>03g+:"O"`|
 @               ^  p3\" ":<
2 234567890123456789012345678901234567890123456789012345678901234567890123456789'''

examples = [
    ("Simple 'Hello world'", simple_hello_world),
    #("Complicated 'Hello world'", complicated_hello_world)
    #("'Less or more' game", less_or_more) # some troubles with input here and below
    #("Factorial", factorial)
    ("Erastotenes sieve", erastotenes)
]

def execute_example(interpreter, name, code, hook=lambda r: None):
    try:
        print(name, "in Befunge93")
        print("-"*80)
        runtime = Runtime()
        interpreter.execute(code, runtime)
        print("<EOF>")
        print("-"*80)
    except BaseException:
        traceback.print_exc(file=sys.stdout)
        print("Program space:")
        print(runtime.space)
        print("Active cell:", runtime.space.active_cell())
        print("Position:", runtime.space.position, "; Direction:", runtime.space.direction)
        print("Program stack:")
        print("\n".join(str(x) for x in reversed(runtime.stack)))
        raise

interpreter = Befunge93Interpreter()
for example in examples:
    execute_example(interpreter, *example)
