---
title: 🟡 rich
---

## 🟢 `Documented`

```python
import rich
from documented import Documented


class MyMessage(Documented):
    """
    This is a Markdown formatted message.
    
    * _One_,
    * *Two*,
    * `Three`
    
    and **more** features of Markdown
    
    > are supported.
    """

rich.print(MyMessage())
```

This will render the docstring as Markdown in the console.

## 🟡 `DocumentedError`

It's easy to write an exception with console markup or Markdown formatted text, catch that exception and `rich.print()` it for user's information.

I haven't found a way to integrate [:simple-github: rich](https://github.com/textualize/rich/) with `documented` directly, to render beautiful exceptions with console markup or Markdown text in them right in the traceback.

Related thread: [:simple-github: textualize/rich#2619](https://github.com/Textualize/rich/issues/2619).
