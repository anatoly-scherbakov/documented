from rich.traceback import install

from documented import DocumentedError

install(show_locals=True)


class RedError(DocumentedError):
    """This [bold]error[/bold] *is* [red]red[/red]."""


def main():
    """Test `rich` formatting for exception text."""
    raise RedError()


if __name__ == '__main__':
    main()
