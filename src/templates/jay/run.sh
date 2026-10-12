#!/usr/bin/env bash

PROJECT="$HOME/projects/project"
CURRENT_BUILD="$PROJECT/build/project"
RUNTIME="runtime"

"$RUNTIME" "$CURRENT_BUILD/thing" "$@"
