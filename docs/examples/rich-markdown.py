import rich
from documented import Documented


class MyMessage(Documented):
    """
    # This is a Markdown formatted message.

    * _One_,
    * *Two*,
    * `Three`

    and **more** features of Markdown

    > are supported.
    """


rich.print(MyMessage())
