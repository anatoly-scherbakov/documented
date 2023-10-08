---
title: 🟡 pydantic
hide:
  - toc
---

!!! info inline end "Idea"
    [:simple-github: pydantic/pydantic#1875](https://github.com/pydantic/pydantic/issues/1875)

* :slight_frown: Pydantic models will raise an error if to try to inherit them from `Exception` and then `raise`,
* :slight_smile: but we can use Pydantic `dataclasses` instead.

{{ run_python_script("examples/pydantic_exception.py") }}
