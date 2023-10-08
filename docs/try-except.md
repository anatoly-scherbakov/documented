---
title: 🏀 try…except
---

# :basketball: `try`…`except`

```mermaid
graph TD
    catch("Why to catch an exception<br>you have thrown elsewhere?") -- "Catching<br>any exception" --> any("Log the error, maybe")
    catch -- "Catch specific<br>exception(s) only" --> flow("<font color=white>Use the exception<br>to change how the system behaves</font>")
    
    style flow fill:#526cfe
```

!!! info inline end "Read more on this"
    [:paperclip: Exceptions as Control Flow](https://blog.cerebralab.com/Exceptions_as_control_flow){ .md-button .md-button--primary }

Python `except` construct allows to manage how the application behaves depending on which exception has been raised. `documented` stimulates to add fields and properties to your exception classes, which you can neatly use in `except` clauses:

```python
try:
    hal.do_stuff()
except HALHasGoneCrazy as err:
    if err.is_moebius_cycle:
        hal.turn_off()
    else:
        hal.self_check()
```
