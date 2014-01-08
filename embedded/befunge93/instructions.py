import random
from embedded.befunge93.runtime import Directions


def add(runtime):
    a = runtime.stack.pop()
    b = runtime.stack.pop()
    runtime.stack.append(a+b)

def substract(runtime):
    a = runtime.stack.pop()
    b = runtime.stack.pop()
    runtime.stack.append(a-b)

def multiply(runtime):
    a = runtime.stack.pop()
    b = runtime.stack.pop()
    runtime.stack.append(a*b)

def divide(runtime):
    a = runtime.stack.pop()
    b = runtime.stack.pop()
    runtime.stack.append(int(a/b))

def modulo(runtime):
    a = runtime.stack.pop()
    b = runtime.stack.pop()
    runtime.stack.append(a%b)

def negate(runtime):
    a = runtime.stack.pop()
    runtime.stack.append( 0 if a else 1 )

def greater(runtime):
    a = runtime.stack.pop()
    b = runtime.stack.pop()
    runtime.stack.append(1 if b>a else 0)

def left(runtime):
    runtime.space.direction = Directions.LEFT

def right(runtime):
    runtime.space.direction = Directions.RIGHT

def up(runtime):
    runtime.space.direction = Directions.UP

def down(runtime):
    runtime.space.direction = Directions.DOWN

def rand(runtime):
    runtime.space.direction = [
        Directions.LEFT,
        Directions.RIGHT,
        Directions.UP,
        Directions.DOWN
        ][random.randint(0, 3)]

def horizontal_cond(runtime):
    a = runtime.stack.pop()
    if a:
        left(runtime)
    else:
        right(runtime)

def vertical_cond(runtime):
    a = runtime.stack.pop()
    if a:
        up(runtime)
    else:
        down(runtime)

def duplicate(runtime):
    a = runtime.stack.pop()
    runtime.stack.append(a)
    runtime.stack.append(a)

def swap(runtime):
    a = runtime.stack.pop()
    b = runtime.stack.pop()
    runtime.stack.append(a)
    runtime.stack.append(b)

def pop(runtime):
    runtime.stack.pop()

def print_int(runtime):
    a = runtime.stack.pop()
    runtime.stdout.write(str(a))

def print_ascii(runtime):
    a = runtime.stack.pop()
    runtime.stdout.write(chr(a))

#seriously, who came up with that name? oO
def trampoline(runtime):
    runtime.space.move()

def put(runtime):
    y = runtime.stack.pop()
    x = runtime.stack.pop()
    v = runtime.stack.pop()
    runtime.space[x, y]=v

def get(runtime):
    y = runtime.stack.pop()
    x = runtime.stack.pop()
    v = runtime.space[x, y]
    runtime.stack.append(v)

def read_int(runtime):
    a = int(runtime.stdin.read(1))
    runtime.stack.append(a)

def read_ascii(runtime):
    a = ord(runtime.stdin.read(1))
    runtime.stack.append(a)

def nothing(runtime):
    pass


