from dataclasses import dataclass


@dataclass
class Untouchable:
    """Object that cannot be accessed."""

    exception: Exception = Exception('Untouchable object has been touched!')

    def __call__(self, *args, **kwargs):
        """Call the object and fail."""
        raise self.exception

    def __getattr__(self, item):
        """Ask for an attribute and fail."""
        raise self.exception

    def __getitem__(self, item):
        """Ask for an item and fail."""
        raise self.exception

    def __str__(self):
        """Ask for string representation and fail."""
        raise self.exception

    def __repr__(self):
        """Ask for  native representation and fail."""
        raise self.exception
