---
title: Philosophy
hide:
  - toc
---

* Create your own exception classes in terms of your domain, to play a part in your business logic, instead of using built-in `Exception` or `ValueError`.
* Refrain from using the word `Exception` or `Error` in their names,
    * For instance:
        * `BalanceInsufficient`
        * `PlanetNotFound`
        * `TetOffline`
        * `OrderDeclined`
    * Instead of:
        * `ValueError`
        * `Exception`
        * `CatastrophicalError`.

* Store meaningful properties of your errors in fields of the exception classes.
* Use [`dataclasses`](https://docs.python.org/3/library/dataclasses.html), [`attrs`](https://github.com/python-attrs/attrs) or [`pydantic`](https://github.com/samuelcolvin/pydantic) to save yourself from boilerplate in `__init__()` — and to get IDE support.
* Maintain docstrings of your exceptions to contain up-to-date, human readable descriptions of what they mean.
* You will be stimulated to do this by [`documented`](https://github.com/anatoly-scherbakov/documented): when an exception happens, the docstring becomes actually useful.
