"""app1."""

import lib1_m
import requests
import rich
from app2 import main as m2  # NOT ALLOWED!


def something():
    """something."""
    data = requests.get("http://google.com")
    print(data.content)
    lib1_m.util_1()
    print("something")


if __name__ == "__main__":
    rich.print("app1 [red]app1")
