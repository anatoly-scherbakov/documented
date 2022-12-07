from pydantic.dataclasses import dataclass as pydantic_dataclass

from documented import DocumentedError


@pydantic_dataclass
class PydanticError(DocumentedError):
    """
    Incorrect answer to the Question of Life, Universe, and Everything.

        - Answer given: {self.answer}
        - Correct answer: indubitably 42.
    """

    answer: str


raise PydanticError(answer='bazinga')
