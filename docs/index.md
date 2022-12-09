---
title: documented
---

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

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package).
