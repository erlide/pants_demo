#! /usr/bin/python3
"""Check that top-level applications don't depend on each other."""


import subprocess
import sys
from typing import List

import rich


def get_bad_dependencies(app, apps) -> List[str]:
    """Return illegal dependencies for this app."""
    result = []
    deps = (
        subprocess.run(
            f"./pants dependencies --transitive {app}",
            shell=True,
            check=True,
            capture_output=True,
        )
        .stdout.decode("utf-8")
        .split("\n")[:-1]
    )
    for dep in deps:
        for other in apps:
            if other == app:
                continue
            othername = other.split(":")[1]
            if othername in dep:
                result.append(dep)
    return result


def main():
    """Get all aps and verify each of them."""
    apps = (
        subprocess.run(
            "./pants --filter-target-type=pex_binary list ::",
            shell=True,
            check=True,
            capture_output=True,
        )
        .stdout.decode("utf-8")
        .split("\n")[:-1]
    )

    result = {}
    for app in apps:
        bad_deps = get_bad_dependencies(app, apps)
        if bad_deps:
            result[app] = bad_deps

    if result:
        print("Illegal dependencies detected:")
    for app, deps in result.items():
        for dep in deps:
            rich.print(f"    [red]{app}[/] on [blue]{dep}[/]")

    return result


if __name__ == "__main__":
    if main():
        sys.exit(1)
