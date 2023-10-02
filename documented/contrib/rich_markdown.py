from documented.untouchable import Untouchable

try:
    from rich.markdown import Markdown   # noqa: WPS433
except ImportError:  # pragma: nocover
    from documented import DocumentedError  # noqa: WPS433

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

    Markdown = Untouchable(  # type: ignore   # noqa: WPS440
        exception=RichNotInstalled(),
    )
