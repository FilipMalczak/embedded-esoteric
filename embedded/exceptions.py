class Brainf__kSyntaxError(SyntaxError):
    pass

class AbstractMethodException(Exception):
    def __str__(self):
        return "This method should be overriden!"
