from dataclasses import dataclass
from documented import DocumentedError


@dataclass   # (1)!
class InsufficientWizardryLevel(DocumentedError):
    """
    🧙 Your level of wizardry is insufficient ☹

        Spell: {self.spell}
        Minimum level required: {self.required_level}
        Actual level: {self.actual_level} {self.comment}

    Unseen University will be happy to assist in your training! 🎓
    """   # (2)!

    spell: str
    required_level: int
    actual_level: int

    @property   # (3)!
    def comment(self) -> str:
        if self.actual_level <= 0:
            return '(You are Rincewind, right? Hi!)'
        else:
            return ''


raise InsufficientWizardryLevel(
    spell='Animal transformation',
    required_level=8,
    actual_level=0,
)
