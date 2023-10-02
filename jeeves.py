import rich
from sh import mkdocs

from documented import Documented


class Example(Documented):
    """
    This is an example Markdown printout.

    * This _message_
    * is *printed*
    * from a **Python** `docstring`.

    ## It even supports code

    ```python
    def something():
        ...
    ```

    > Cool indeed!
    """


def example():
    """Print an example `Documented` object in Markdown."""
    rich.print(Example())


def serve():
    """Serve documentation."""
    mkdocs.serve('-a', 'localhost:6854', _fg=True)
