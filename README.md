# documented

[![Python Version](https://img.shields.io/pypi/pyversions/documented.svg)](https://pypi.org/project/documented/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
![PyPI - License](https://img.shields.io/pypi/l/documented)

Templated docstrings for Python classes.

## Features

- Describe your business logic in docstrings of your classes and exceptions;
- When printing an object or an exception, the library will substitute the placeholders in the docstring text with runtime values,
- And you (or your user) will see a human-readable text.

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

For more examples, see: https://anatoly-scherbakov.github.io/documented/

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package).
