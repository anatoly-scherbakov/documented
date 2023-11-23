from pydantic.dataclasses import dataclass as pydantic_dataclass

from documented import DocumentedError


@pydantic_dataclass
class PydanticError(DocumentedError):
    """
    Incorrect answer!

    (To the Question of Life, Universe, and Everything.)

        - Answer given: {self.answer}
        - Correct answer: indubitably 42.
    """

    answer: str


raise PydanticError(answer='bebebe')
