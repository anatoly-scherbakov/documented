---
title: 🟡 rich
hide:
  - toc
---

## 🟢 `Documented`

{{ run_python_script("examples/rich-markdown.py") }}

This will render the docstring as Markdown in the console.

## 🟡 `DocumentedError`

!!! info inline end "See related thread"
    [:simple-github: textualize/rich#2619](https://github.com/Textualize/rich/issues/2619)

* :slight_frown: I haven't found a way to integrate [:simple-github: rich](https://github.com/textualize/rich/) with `documented` directly, to render beautiful exceptions with console markup or Markdown text in them right in the traceback.

* :slight_smile: However, this can always be done manually:
    * `except` the error,
    * and `rich.print()` it.
