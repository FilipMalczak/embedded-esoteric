class TickerInterface:
    '''
    Little class, useful while debugging brainf__k code.
    It counts "ticks", which are calls to "tick" method.
    '''

    def tick(self):
        '''
        Increase internal counter
        '''

    def get_ticks(self):
        '''
        Return internal counter value
        '''

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
