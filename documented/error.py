import logging
import textwrap
from dataclasses import dataclass

from documented.documented import Documented

logger = logging.getLogger(__name__)


class DocumentedError(Documented, Exception):
    """Exception with a templated error message provided as the docstring."""
