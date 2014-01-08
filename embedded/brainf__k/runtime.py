import sys
from embedded.utils.array import ElasticArray

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

