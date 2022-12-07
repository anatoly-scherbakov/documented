---
title: Philosophy
---

## Making your exceptions sane

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

## Links

* About naming and abstracting things: [Kevlin Henney. Seven Ineffective Coding Habits of Many Programmers](https://www.youtube.com/watch?v=ZsHMHukIlJY)
* [Python: Better Typed Than You Think](https://beepb00p.xyz/mypy-error-handling.html) summarizes a number of ways to handle errors in Python programs
* [dry-python/returns](http://github.com/dry-python/returns) proposes to replace exceptions with monadic [`Result` container](https://returns.readthedocs.io/en/latest/pages/result.html), which works great in [Scala](https://www.scala-lang.org/api/2.9.3/scala/Either.html), [Haskell](https://www.schoolofhaskell.com/school/starting-with-haskell/basics-of-haskell/10_Error_Handling#the-either-monad), and [Rust](https://doc.rust-lang.org/stable/rust-by-example/error/result.html), — but arguably not everyone would want to adopt this approach in their Python codebase.
* [Exceptions as control flow](https://blog.cerebralab.com/Exceptions_as_control_flow), to the contrast, describes advantages of using exceptions to control your application.

Which actually explains the meaning of this little helper: if we're stuck with exceptions in Python, why not at least make them friendlier?
