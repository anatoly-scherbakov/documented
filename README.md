# documented-error

[![Build Status](https://travis-ci.com/python-platonic/documented-error.svg?branch=master)](https://travis-ci.com/python-platonic/documented-error)
[![Coverage](https://coveralls.io/repos/github/python-platonic/documented-error/badge.svg?branch=master)](https://coveralls.io/github/python-platonic/documented-error?branch=master)
[![Python Version](https://img.shields.io/pypi/pyversions/documented-error.svg)](https://pypi.org/project/documented-error/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Human readable Python exceptions.


## Features

- Fully typed with annotations and checked with mypy, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)
- Add yours!


## Installation

```bash
pip install documented-error
```


## Example

Showcase how your project can be used:

```python
from documented_error.example import some_function

print(some_function(3, 4))
# => 7
```

## License

[MIT](https://github.com/python-platonic/documented-error/blob/master/LICENSE)


## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [5840464a31423422d7523897d854e92408eee6b8](https://github.com/wemake-services/wemake-python-package/tree/5840464a31423422d7523897d854e92408eee6b8). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/5840464a31423422d7523897d854e92408eee6b8...master) since then.
