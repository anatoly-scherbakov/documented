---
title: documented
hide:
  - navigation
  - toc
---

[![Python Version](https://img.shields.io/pypi/pyversions/documented.svg)](https://pypi.org/project/documented/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
![PyPI - License](https://img.shields.io/pypi/l/documented)

Templated docstrings for Python classes.

## Example

{{ run_python_script("examples/open-the-pod-bay-doors.py") }}

## Process

```mermaid
graph LR
    A("Class docstring<br>with <code>{self.placeholders}</code>") --> B(dedent)
    B --> C("interpolate")
    C --> D("<code>__str__()</code>")
    D --> raise("raise")
    D --> F("print")
    F --> rich("even as Markdown with <code>rich</code>")
    
    style raise stroke:#CC0000
```

## Features

!!! info inline "In your docstrings"
    Describe an object, or an exception, in your docstring, and use `{self.placeholders}` to include its fields & properties

!!! info inline "Print or raise the object"
    The docstring with resolved `{self.placeholders}` will be its string representation

!!! info inline "Result"
    Human readable text as the output, or log, of your application.

!!! info inline "More"
    [See docs](formatting/){ .md-button }

<br clear="both">

## Installation

```bash
pip install documented
```

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package).
