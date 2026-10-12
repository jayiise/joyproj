#!/usr/bin/env bash

PROJECT="$HOME/projects/project"
PROJECT_NAME="project"
SRC="$PROJECT/src"
TARGET_BUILD="$PROJECT/build/project"
VERSION="$PROJECT/VERSION"

if [[ "$1" == "install" ]]; then
  TARGET_BUILD="whereeveritgoes"
fi

echo "joyproj building: Building '$PROJECT_NAME' in '$TARGET_BUILD' ..."

rm -r "$TARGET_BUILD/"*
cp -r "$SRC/"* "$TARGET_BUILD/"
cp "$VERSION" "$TARGET_BUILD/"

echo "  done"
