---
title: ✏️ Templating
hide:
  - toc
---

# :octicons-project-template-24: Templating

`{self.something}` templating pieces will be interpolated when rendering the exception value. 

{{ run_python_script("examples/open-the-pod-bay-doors.py") }}

* [`textwrap.dedent()`](https://docs.python.org/3/library/textwrap.html#textwrap.dedent) is applied to the result, thus Python indentation rules do not corrupt the resulting message.
* Template rendering is done using [`str.format()`](https://docs.python.org/3/library/string.html#formatspec). That function receives the object instance as `self` keyword argument.

    You can also access elements of lists and dicts by index, for example: `{self.countries[US]}`, but I wouldn't recommend that. Use a property instead (see below).

## Dynamic content

From template, you can't call methods of the object, but you can access its fields and properties. You might find useful:
 
* [`@property`](https://docs.python.org/3/library/functions.html#property)
* or, [`@cached_property`](https://docs.python.org/3/library/functools.html#functools.cached_property) for performance
    * This function is only available since Python 3.8,
    * There is a [backport](https://pypi.org/project/cached-property) available though.

## Dataclasses

Dataclasses are used in this example in order to provide the astronaut's name to the exception in the most convenient way. You can

* opt out of using them if you wish,
* or use [`attrs`](../compatibility/attrs/) instead,
* or maybe substitute them with [pydantic dataclasses](../compatibility/pydantic/).

## Error while rendering

If there is an error while rendering the exception then you will see something like this:

{{ run_python_script("examples/not_renderable.py") }}
