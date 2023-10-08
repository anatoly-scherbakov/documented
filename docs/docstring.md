---
title: 📝 """Docstring"""
hide:
  - toc
---

# 📝 `"""Docstring"""`

Having installed `documented`, you can use `DocumentedError` as base for your custom exception classes. The immediate
effect of that is that raising these exceptions will print their docstrings in the stack trace.

{{ run_python_script("examples/docstring.py") }}

## Styling Recommendations

* Create your own exception classes in terms of your domain, to play a part in your business logic, instead of using built-in `Exception` or `ValueError`.
* Refrain from using the word `Exception` or `Error` in their names.
  * A good IDE can convey the information that something is an exception;
  * Even discarding that, seeing `raise FooBarBaz` is sufficient to understand what kind of guy `FooBarBaz` is.

### :slight_smile: Good

* :white_check_mark: `BalanceInsufficient`
* :white_check_mark: `PlanetNotFound`
* :white_check_mark: `TetOffline`
* :white_check_mark: `OrderDeclined`

### :slight_frown: Not so good

* :no_entry_sign: `BalanceInsufficientError`
* :no_entry_sign: `PlanetNotFoundException`
* :no_entry_sign: `CatastrophicalError`
* :no_entry_sign: `UnknownError`
