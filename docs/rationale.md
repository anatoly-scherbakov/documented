---
hide:
  - toc
---

During my time in writing Python code, I have gone through a certain evolution; one of the aspects of it is how I create and manage exceptions.

## Level 0

```python
raise ValueError("I'm sorry Dave. I'm afraid I can't do that.")
```

Here, to signify an error, we just use a standard built-in error class (such as `Exception` or `ValueError`). The exception message will be printed to the log and/or provided to the user.

If we would like to catch the exception and to base our future behavior on the particular error that we had caught then we will be in trouble; likely we'll have to manually parse the exception message. That's dirty.

## Level 1

```python
class PodBayDoorsStillClosed(ValueError):
    pass

# …

raise PodBayDoorsStillClosed("I'm sorry Dave. I'm afraid I can't do that.")
```

Now, I can catch `PodBayDoorsStillClosed` in some other place of the application, and modify my behavior based on that. For instance, I can

```python
try:
    ...
except PodBayDoorsStillClosed:
    retry()
```

It is unlikely that HAL complies but at least the code will be arguably a bit more expressive.

## Level 2

At some point, I realize that the text of HAL's message belongs to the class of the exception; there is no reason to keep them apart.

```python
class PodBayDoorsStillClosed(ValueError):
    def __str__(self):
        return "I'm sorry Dave. I'm afraid I can't do that."

# …

raise PodBayDoorsStillClosed()
```

This is better, but… is it cool to write `__str__` all the time, for each exception message, separately? — No, decidedly not.

## Level ∞

Some time ago I wrote a very small Python library by the name of [`documented`](https://anatoly-scherbakov.github.io/documented/). Which makes it look like this:

```python
@dataclass
class PodBayDoorsStillClosed(DocumentedError):
    """
    I’m sorry, {self.user_name}.

    I’m afraid I can’t do that.
    """

    user_name: str

# …

raise PodBayDoorsStillClosed('Dave')
```

That will print:

```
PodBayDoorsStillClosed: I’m sorry, Dave.

I’m afraid I can’t do that.
```

I am now using it to format both internal and external exceptions for web and console applications. Flight condition nominal, so far. Perhaps this library will be useful for you too; you can easily grab it via

```shell
pip install documented
```
