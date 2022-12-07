---
title: 🟡 pydantic
---

!!! warning "Partially compatible"
    Pydantic models will raise an error if to try to inherit them from `Exception`, but we can use Pydantic `dataclasses` instead. Idea:  [:simple-github: pydantic/pydantic#1875](https://github.com/pydantic/pydantic/issues/1875)

{{ run_python_script("examples/pydantic_exception.py") }}
