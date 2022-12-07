"""MkDocs macros for the documentation site."""
import functools
from pathlib import Path

from mkdocs_macros.plugin import MacrosPlugin
from plumbum.cmd import python

TEMPLATE = '''
```python title="{path}"
{code}
```

{annotations}

⇒
```python title="{cmd} {path}"
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
    args: list[str] | None = None,
):
    if annotations is None:
        annotations = []

    if args is None:
        args = []

    code_path = docs_dir / path
    code = code_path.read_text()

    _, stdout, stderr = python[*args, code_path].run(retcode=None)

    cmd = 'python'
    if args:
        formatted_args = ' '.join(args)
        cmd = f'{cmd} {formatted_args}'

    return TEMPLATE.format(
        path=path,
        code=code,
        stdout=stdout,
        stderr=stderr,
        annotations=format_annotations(annotations),
        cmd=cmd,
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
