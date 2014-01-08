from embedded.utils.ticker import DummyTicker

def tokenizer(code, allowed, ticker=None):
    '''
    Generator, which
    '''
    if ticker is None:
        ticker = DummyTicker()
    for char in code:
        ticker.tick()
        if char in allowed:
            yield char
