"""app1."""

import requests
import rich

# from app2 import main as m2  # NOT ALLOWED!
from lib1 import lib1_m


def something():
    """something."""
    data = requests.get("http://google.com")
    print(data.content)
    lib1_m.util_1()
    print("something")


def mmain():
    """mmain."""
    something()
    rich.print("app1 [red]app1[/red]!")
    # m2.mmain()


if __name__ == "__main__":
    mmain()
