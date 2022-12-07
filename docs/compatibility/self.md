---
title: "🔴 {self}"
---

Using plain `{self}` in the docstring will cause a recursion. As well as something like this:

{{ run_python_script("examples/recursion.py") }}

!!! warning "So please do not do that"
    We could have filtered out the plain call to `{self}` but we're unable to do so for more involved cases as illustrated above, so for now we are keeping it as it is.
