---
title: "🔴 python -OO"
---

As [the reference](https://docs.python.org/3/using/cmdline.html#cmdoption-OO) states, `-OO` mode will discard the docstrings.

```bash
python -OO script.py
```

{{
  run_python_script("examples/wizardry.py",
  annotations=[
    "Usage of `dataclasses` is not required but helps alleviate boilerplate.",
    "Docstring is used to render the exception. More than that, you can render fields of the exception instance in it using `{self.something}` placeholders.",
    "You cannot call methods of the exception instance. But you can refer to properties to help generate dynamic content."
  ],
  args=['-OO']
) }}

As you can see, the [Fallback `__repr__` mode](/repr/) is used in this case.
