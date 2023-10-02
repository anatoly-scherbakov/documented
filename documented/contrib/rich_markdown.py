from documented.untouchable import Untouchable

try:
    from rich.markdown import Markdown
except ImportError:  # pragma: nocover
    from documented import DocumentedError

    class RichNotInstalled(DocumentedError):
        """
        The `rich` library is not installed.

        There was an attempt to visualize a `Documented` object as Markdown via
        `rich` library, but that one is not installed. Perhaps you would want
        to do:

        ```
        pip install rich
        ```
        """

    Markdown = Untouchable(  # type: ignore
        exception=RichNotInstalled(),
    )
