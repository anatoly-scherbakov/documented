---
title: documented
---

[![Coverage](https://coveralls.io/repos/github/python-platonic/documented/badge.svg?branch=master)](https://coveralls.io/github/python-platonic/documented?branch=master)
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

```python
from dataclasses import dataclass
from documented import DocumentedError


@dataclass
class InsufficientWizardryLevel(DocumentedError):
    """
    🧙 Your level of wizardry is insufficient ☹

        Spell: {self.spell}
        Minimum level required: {self.required_level}
        Actual level: {self.actual_level} {self.comment}

    Unseen University will be happy to assist in your training! 🎓
    """

    spell: str
    required_level: int
    actual_level: int

    @property
    def comment(self) -> str:
        if self.actual_level <= 0:
            return '(You are Rincewind, right? Hi!)'
        else:
            return ''


raise InsufficientWizardryLevel(
    spell='Animal transformation',
    required_level=8,
    actual_level=0,
)
```

which prints:

```
---------------------------------------------------------------------
InsufficientWizardryLevel           Traceback (most recent call last)
<ipython-input-1-d8ccdb953cf6> in <module>
     27 
     28 
---> 29 raise InsufficientWizardryLevel(
     30     spell='Animal transformation',
     31     required_level=8,

InsufficientWizardryLevel: 
🧙 Your level of wizardry is insufficient ☹

    Spell: Animal transformation
    Minimum level required: 8
    Actual level: 0 (You are Rincewind, right? Hi!)

Unseen University will be happy to assist in your training! 🎓
```

## Usage

* Template rendering is done using [`str.format()`](https://docs.python.org/3.6/library/string.html#formatspec).
* That function receives the object instance as `self` keyword argument.
* From template, you can't call methods of the object, but you can access its fields and properties.
* [`textwrap.dedent()`](https://docs.python.org/3/library/textwrap.html#textwrap.dedent) is applied to the result, thus Python indentation rules do not corrupt the resulting message.

Dynamically computed pieces of content may be introduced using:
 
* [`@property`](https://docs.python.org/3/library/functions.html#property)
* or, [`@cached_property`](https://docs.python.org/3/library/functools.html#functools.cached_property) for performance.

You can also access elements of lists and dicts by index, for example: `{self.countries[US]}`.

## Making your exceptions sane

* Create your own exception classes in terms of your domain, to play a part in your business logic.
* Do not use the word `Exception` or `Error` in their names. Your code should `raise` things like:
    * `BalanceInsufficient`
    * `PlanetNotFound`
    * `TetOffline`
    * `OrderDeclined`

  And should not:

    * `ValueError`
    * `Exception`
    * `CatastrophicalError`

* Store meaningful properties of your errors in fields of the exception classes.
* Use [`dataclasses`](https://docs.python.org/3/library/dataclasses.html), [`attrs`](https://github.com/python-attrs/attrs) or [`pydantic`](https://github.com/samuelcolvin/pydantic) to save yourself from boilerplate in `__init__()` — and to get IDE support.
* Maintain docstrings of your exceptions to contain up-to-date, human readable descriptions of what they mean.
* You will be stimulated to do this by [`documented`](https://github.com/python-platonic/documented): when an exception happens, the docstring becomes actually useful.

## Links

* About naming and abstracting things: [Kevlin Henney. Seven Ineffective Coding Habits of Many Programmers](https://www.youtube.com/watch?v=ZsHMHukIlJY)
* [Python: Better Typed Than You Think](https://beepb00p.xyz/mypy-error-handling.html) summarizes a number of ways to handle errors in Python programs
* [dry-python/returns](http://github.com/dry-python/returns) proposes to replace exceptions with monadic [`Result` container](https://returns.readthedocs.io/en/latest/pages/result.html), which works great in [Scala](https://www.scala-lang.org/api/2.9.3/scala/Either.html), [Haskell](https://www.schoolofhaskell.com/school/starting-with-haskell/basics-of-haskell/10_Error_Handling#the-either-monad), and [Rust](https://doc.rust-lang.org/stable/rust-by-example/error/result.html), — but arguably not everyone would want to adopt this approach in their Python codebase.
* [Exceptions as control flow](https://blog.cerebralab.com/Exceptions_as_control_flow), to the contrast, describes advantages of using exceptions to control your application.

Which actually explains the meaning of this little helper: if we're stuck with exceptions in Python, why not at least make them friendlier?

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [5840464a31423422d7523897d854e92408eee6b8](https://github.com/wemake-services/wemake-python-package/tree/5840464a31423422d7523897d854e92408eee6b8). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/5840464a31423422d7523897d854e92408eee6b8...master) since then.
