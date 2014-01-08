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

#TODO: IO operations and below on english wiki
