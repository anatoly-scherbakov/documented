import logging
import textwrap

logger = logging.getLogger(__name__)


class Documented:
    """Class with a templated docstring."""

    def __str__(self) -> str:
        """Format and return the docstring."""
        template = self.__docstring_template()

        # This call can access properties of `self` and, therefore, execute
        # user's arbitrary code. We have to catch any exceptions that
        # may ensue, and log them.
        # If we do not do so, the user will only see something like this:
        #
        #     <unprintable Documented object>
        try:
            return template.format(self=self)

        except Exception:
            logger.exception(
                f'Could not print a {self.__class__.__name__} object.',
            )
            raise

    def __docstring_template(self) -> str:  # noqa: WPS112
        """Preformat the message template."""
        return textwrap.dedent(
            self.__doc__ or repr(self),
        ).strip('\n')
