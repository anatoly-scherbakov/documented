---
title: documented
---

[![Coverage](https://coveralls.io/repos/github/anatoly-scherbakov/documented/badge.svg?branch=master)](https://coveralls.io/github/anatoly-scherbakov/documented?branch=master)
[![Python Version](https://img.shields.io/pypi/pyversions/documented.svg)](https://pypi.org/project/documented/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
![PyPI - License](https://img.shields.io/pypi/l/documented)

Templated docstrings for Python classes.

## Features

- Describe your business logic in docstrings of your classes and exceptions;
- When printing an object or an exception, the library will substitute the placeholders in the docstring text with runtime values,
- And you (or your user) will see a human readable text.

## Installation

```bash
pip install documented
```


## Example

{{
  run_python_script("examples/wizardry.py",
  annotations=[
    "Usage of `dataclasses` is not required but helps alleviate boilerplate.",
    "Docstring is used to render the exception. More than that, you can render fields of the exception instance in it using `{self.something}` placeholders.",
    "You cannot call methods of the exception instance. But you can refer to properties to help generate dynamic content."
  ]
) }}

## Usage

* Template rendering is done using [`str.format()`](https://docs.python.org/3/library/string.html#formatspec).
* That function receives the object instance as `self` keyword argument.
* From template, you can't call methods of the object, but you can access its fields and properties.
* [`textwrap.dedent()`](https://docs.python.org/3/library/textwrap.html#textwrap.dedent) is applied to the result, thus Python indentation rules do not corrupt the resulting message.

Dynamically computed pieces of content may be introduced using:
 
* [`@property`](https://docs.python.org/3/library/functions.html#property)
* or, [`@cached_property`](https://docs.python.org/3/library/functools.html#functools.cached_property) for performance.

You can also access elements of lists and dicts by index, for example: `{self.countries[US]}`.

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

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package).
