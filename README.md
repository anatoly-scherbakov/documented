# documented

[![Build Status](https://travis-ci.com/python-platonic/documented.svg?branch=master)](https://travis-ci.com/python-platonic/documented)
[![Coverage](https://coveralls.io/repos/github/python-platonic/documented/badge.svg?branch=master)](https://coveralls.io/github/python-platonic/documented?branch=master)
[![Python Version](https://img.shields.io/pypi/pyversions/documented.svg)](https://pypi.org/project/documented/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Templated docstrings for Python classes.

## Features

- Describe your business logic in docstrings of your classes and exceptions;
- When printing an object or an exception, your code will explain to you what is going on.

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

## License

[MIT](https://github.com/python-platonic/documented/blob/master/LICENSE)


## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [5840464a31423422d7523897d854e92408eee6b8](https://github.com/wemake-services/wemake-python-package/tree/5840464a31423422d7523897d854e92408eee6b8). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/5840464a31423422d7523897d854e92408eee6b8...master) since then.
