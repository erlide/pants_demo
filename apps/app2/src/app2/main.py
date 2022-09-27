"""app2."""

import rich
from lib2 import lib2_m
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = "Jane Doe"


def mmain():
    """mmain."""
    rich.print("app2")
    lib2_m.util_2()
    print(User(id=3))


if __name__ == "__main__":
    mmain()
