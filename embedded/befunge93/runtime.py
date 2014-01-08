#TODO: add acyclic space
from array import array
from collections import defaultdict
import sys


def def_cell():
    return " "

def def_row():
    return defaultdict(def_cell)

class Directions:
    RIGHT = 1, 0
    LEFT = -1, 0
    DOWN = 0, 1
    UP = 0, -1

class CyclicSpace:
    def __init__(self, columns: int=80, rows: int=25,
                 position: (int, int)=(0, 0),
                 direction: (int, int)=Directions.RIGHT,
                 code: str=""):
        self.columns = columns
        self.rows = rows
        self.position = position
        self.direction = direction
        self._data = defaultdict(def_row)
        self.inject_code(code)

    def __getitem__(self, item: (int, int)):
        x, y = item
        return self._data[y][x]

    def __setitem__(self, key: (int, int), value: int):
        x, y = key
        self._data[y][x] = value

    def inject_code(self, code: str):
        y = 0
        for line in code.splitlines():
            x = 0
            for char in line:
                self[x, y] = char
                x += 1
            y += 1


    def move(self, direction=None):
        if direction is None:
            direction = self.direction
        x, y = self.position
        dx, dy = direction
        self.position = x+dx, y+dy

    def active_cell(self):
        return self[self.position]

    def __str__(self):
        return "-"+ ("".join("|" if self.position[0]==x else "-" for x in range(self.columns))) + "-\n" + \
               "\n".join(
                   ("=" if y==self.position[1] else "|") +\
                    "".join( self[x, y]
                             if x in self._data[y]
                             else " "
                             for x in range(self.columns)
                    ) + \
                    ("=" if y==self.position[1] else "|")
                    for y in range(self.rows)
                ) + \
                "\n"+ "-"+ ("".join("|" if self.position[0]==x else "-" for x in range(self.columns))) + "-"

    def __repr__(self):
        return "< %s: data: %r >" % (
            type(self).__name__,
            {
                k: dict(v)
                for k,v in self._data.items()
            }
        )


class Runtime:
    def __init__(self, space=None, stack=None,
                 stdout: 'ascii writing stream'=sys.stdout,
                 stdin: 'ascii reading stream'=sys.stdin):
        if space is None:
            space = CyclicSpace()
        if stack is None:
            stack = array("B")
        self.space = space
        self.stack = stack
        self.stdout = stdout
        self.stdin = stdin
