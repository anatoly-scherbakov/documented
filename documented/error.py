from documented.documented import Documented


class DocumentedError(Documented, Exception):
    """Exception with a templated error message provided as the docstring."""
