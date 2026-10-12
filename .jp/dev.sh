#!/usr/bin/env bash

PROJECT="$HOME/projects/joyproj"
PROJECT_NAME="joyproj"
OLD_WD="$PWD"

enter_session() {
  if [ -n "$TMUX" ]; then
    tmux switch-client -t "$PROJECT_NAME"
  else
    tmux attach-session -t "$PROJECT_NAME"
  fi
}

if tmux has-session -t "$PROJECT_NAME" 2>/dev/null; then
  enter_session
  exit 0
fi

cd "$PROJECT"
tmux new-session -d -s "$PROJECT_NAME" -n editor
tmux send-keys -t "$PROJECT_NAME":editor 'nvim src/joyproj.py' Enter

tmux new-window -t "$PROJECT_NAME" -n test

tmux select-window -t "$PROJECT_NAME":editor

enter_session

cd "$OLD_WD"
