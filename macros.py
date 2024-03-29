"""MkDocs macros for the documentation site."""
import functools
import os
import re
from pathlib import Path

from mkdocs_macros.plugin import MacrosPlugin
from sh import python, ErrorReturnCode


TEMPLATE = """
<div class="side-by-side" style="max-width: 100%" markdown>
<div class="admonition info" markdown>
<p class="admonition-title" markdown>{path}</p>
```python
{code}
```

{annotations}
</div>

<div class="admonition {output_block_class}" markdown>
<p class="admonition-title">python</p>
```python
{output}
```
</div>
</div>
"""


def format_annotations(annotations: list[str]) -> str:
    """Format annotations for a piece of code."""
    enumerated_annotations = enumerate(annotations, start=1)

    return '\n\n'.join(
        f'{number}. {annotation}'
        for number, annotation in enumerated_annotations
    )


def replace_full_file_path(line: str, code_path: Path) -> str:
    """Replace full file path with its absolute path, for conciseness."""
    return line.replace(str(code_path.parent.absolute()), '📂')


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

    try:
        stdout, stderr = python(
            *args,
            code_path,
            _env={
                **os.environ,
                'TERM': 'dumb',
            },
        ), None
    except ErrorReturnCode as err:
        stdout = err.stdout.decode()
        stderr = err.stderr.decode()

    cmd = 'python'
    if args:
        formatted_args = ' '.join(args)
        cmd = f'{cmd} {formatted_args}'

    output = '\n'.join(filter(bool, [stdout, stderr]))

    output = '\n'.join(
        replace_full_file_path(line=line, code_path=code_path)
        for line in output.splitlines()
    )

    return TEMPLATE.format(
        path=path,
        code=code,
        output=output,
        annotations=format_annotations(annotations),
        cmd=cmd,
        output_block_class='failure' if stderr else 'success',
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
