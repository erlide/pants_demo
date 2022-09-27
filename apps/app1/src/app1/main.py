"""app1."""

import requests
import rich
import yaml

# from app2 import main as m2  # NOT ALLOWED!
from lib1 import lib1_m


def something():
    """something."""
    data = requests.get("http://google.com")
    print(f"GOOGLE <- {len(data.content)} bytes")
    print(yaml.safe_dump({}))
    lib1_m.util_1()
    print("something")


def mmain():
    """mmain."""
    something()
    rich.print("app1 [red]app1[/red]!")
    # m2.mmain()


if __name__ == "__main__":
    mmain()
