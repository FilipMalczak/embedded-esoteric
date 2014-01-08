from array import array

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
