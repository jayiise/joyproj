#!/usr/bin/env bash

PROJECT="$HOME/projects/joyproj"
SRC="$PROJECT/src"
CURRENT_BUILD="$PROJECT/build/joyproj"
VERSION="$PROJECT/VERSION"

rm -r "$CURRENT_BUILD/"*
cp -r "$SRC/"* "$CURRENT_BUILD/"
cp "$VERSION" "$CURRENT_BUILD/"
