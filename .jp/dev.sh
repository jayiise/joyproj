#!/usr/bin/env bash

PROJECT="$HOME/projects/joyproj"
SESSION="joyproj"
OLD_WD="$PWD"

enter_session() {
  if [ -n "$TMUX" ]; then
    tmux switch-client -t "$SESSION"
  else
    tmux attach-session -t "$SESSION"
  fi
}

if tmux has-session -t "$SESSION" 2>/dev/null; then
  enter_session
  exit 0
fi

cd "$PROJECT"
tmux new-session -d -s "$SESSION" -n editor
tmux send-keys -t "$SESSION":editor 'nvim src/joyproj.py' Enter

tmux new-window -t "$SESSION" -n test

tmux select-window -t "$SESSION":editor

enter_session

cd "$OLD_WD"
