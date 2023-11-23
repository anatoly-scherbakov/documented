from documented import DocumentedError


class NotRenderable(DocumentedError):
    """
    This exception is not renderable.

    {self.no_hope}
    """

    @property
    def no_hope(self):
        return str(1 / 0)


raise NotRenderable()
