---
title: Documented
---

!!! note "Base class"
    You can inherit your classes from `Documented`, it won't be an exception like it is the case for `DocumentedError` but it will still render your docstring as `__str__`. I use this to catalogue messages in console applications, for example. 

::: documented.Documented
