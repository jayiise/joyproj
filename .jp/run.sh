#!/usr/bin/env bash

PROJECT="$HOME/projects/joyproj"
CURRENT_BUILD="$PROJECT/build/joyproj"
RUNTIME="$HOME/.python/bin/python3"

"$RUNTIME" "$CURRENT_BUILD/joyproj.py" "$@"
