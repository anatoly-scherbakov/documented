"""MkDocs macros for the documentation site."""
import functools
import textwrap
from pathlib import Path
from plumbum.cmd import python

from mkdocs_macros.plugin import MacrosPlugin


TEMPLATE = '''
```python title="{path}"
{code}
```

{annotations}

⇒
```python title="stderr"
{stderr}
```
'''


def format_annotations(annotations: list[str]) -> str:
    enumerated_annotations = enumerate(annotations, start=1)

    return '\n\n'.join(
        f'{number}. {annotation}'
        for number, annotation in enumerated_annotations
    )


def run_python_script(
    path: str,
    docs_dir: Path,
    annotations: list[str] | None = None,
):
    if annotations is None:
        annotations = []

    code_path = docs_dir / path
    code = code_path.read_text()

    _, stdout, stderr = python[code_path].run(retcode=None)

    return TEMPLATE.format(
        path=path,
        code=code,
        stdout=stdout,
        stderr=stderr,
        annotations=format_annotations(annotations),
    )


def define_env(env: MacrosPlugin):
    """Hook function."""
    env.macro(
        functools.partial(
            run_python_script,
            docs_dir=Path(env.conf['docs_dir']),
        ),
        name='run_python_script',
    )
