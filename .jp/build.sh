#!/usr/bin/env bash

PROJECT="$HOME/projects/joyproj"
PROJECT_NAME="joyproj"
SRC="$PROJECT/src"
TARGET_BUILD="$PROJECT/build/joyproj"
VERSION="$PROJECT/VERSION"

if [[ "$1" == "install" ]]; then
  TARGET_BUILD="$HOME/.jaythings/joyproj"
fi

echo "joyproj building: Building '$PROJECT' in '$TARGET_BUILD' ..."

rm -r "$TARGET_BUILD/"*
cp -r "$SRC/"* "$TARGET_BUILD/"
cp "$VERSION" "$TARGET_BUILD/"

echo "  done"
