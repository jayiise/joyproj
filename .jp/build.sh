#!/usr/bin/env bash

PROJECT="$HOME/projects/joyproj"
PROJECT_NAME="joyproj"
SRC="$PROJECT/src"
TARGET_BUILD="$PROJECT/build/joyproj"
VERSION="$PROJECT/VERSION"

if [[ "$1" == "install" ]]; then
  TARGET_BUILD="$HOME/.jaythings/joyproj"
  mv "$TARGET_BUILD/projects.json" "/tmp/joyproj-projects.json.bak"
fi

echo "joyproj building: Building '$PROJECT' in '$TARGET_BUILD' ..."

rm -r "$TARGET_BUILD/"*
cp -r "$SRC/"* "$TARGET_BUILD/"
cp "$VERSION" "$TARGET_BUILD/"
if [[ "$1" == "install" ]]; then
  mv "/tmp/joyproj-projects.json.bak" "$TARGET_BUILD/projects.json"
fi

echo "  done"
