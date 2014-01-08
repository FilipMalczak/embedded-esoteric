from array import array
import sys
from embedded.brainf__k.interfaces import TickerInterface


class ElasticArray(array):
    '''
    Almost exactly the same as array.
    Only difference is that it will never raise IndexError, because calls with
    index greater/equal than length of array causes array to be filled with 0.
    '''

    def _ensure_index(self, idx):
        if len(self)<=idx:
            self.extend(0 for i in range(idx-len(self)+1))

    def __getitem__(self, item):
        self._ensure_index(item)
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        self._ensure_index(key)
        return super().__setitem__(key, value)

    def insert(self, i, x):
        if i>=0:
            self._ensure_index(i)
        return super().insert(i, x)

class Brainf__kRuntime:
    def __init__(self, size=30000, stdout=sys.stdout, stdin=sys.stdin):
        self.buffer = ElasticArray("B")
        self.maxsize = size
        self.stdout = stdout
        self.stdin = stdin
        self._pointer = 0

    @property
    def pointer(self):
        return self._pointer

    @pointer.setter
    def pointer(self, x):
        if self.maxsize>0:
            self._pointer = x % self.maxsize
        else:
            self._pointer = x

class DummyTicker(TickerInterface):
    '''
    Used when debugging is turned off. tick() doesnt do anything, and get_ticks()
    always returns 0.
    '''
    def get_ticks(self):
        return 0

class Ticker(TickerInterface):
    def __init__(self):
        self._ticks = 0

    def tick(self):
        self._ticks += 1

    def get_ticks(self):
        return self._ticks