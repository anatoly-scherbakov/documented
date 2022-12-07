---
title: Fallback mode
---

If either:

* the docstring for a `Documented` class is not provided,
* or it is stripped by the [`-OO`](/compatibility/-OO/) mode

then we will output the object's [`repr()`](https://docs.python.org/3/library/functions.html#repr) instead.
