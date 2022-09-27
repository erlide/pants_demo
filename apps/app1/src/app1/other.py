"""other."""

from dataclasses import dataclass

from . import main


@dataclass
class Board:
    """board."""

    xyz: int


def enter():
    """enter."""
    main.mmain()
    print("HELLO HELLO HELLO")
