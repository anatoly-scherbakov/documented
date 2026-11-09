import sys

from documented import DocumentedError

sys.setrecursionlimit(30)


class Recursion(DocumentedError):
    """
    This exception is a bugger.

    It will crash when rendering {self.recursive_property}.
    """

    @property
    def recursive_property(self):
        return self


raise Recursion()
