def tokenizer(code, allowed):
    for char in code:
        if char in allowed:
            yield char
