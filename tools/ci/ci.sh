#!/bin/bash

./pants --version # Bootstrap Pants.

# run on everything
./pants tailor --check update-build-files --check lint check test ::

## or run only on what changed; this can miss things like adding a new linter
#./pants --changed-since=github/master tailor --check update-build-files --check lint
#./pants --changed-since=github/master --changed-dependees=transitive check test
