# joyproj - jayiise@github.com

# Init
from pathlib import Path
import subprocess, json, sys, importlib.util

PROJECT_DIRECTORY = Path(__file__).parent
VERSION = (PROJECT_DIRECTORY / "VERSION").read_text().strip("\n")
CWD = Path.cwd()

# Functions
def show_header():
  print(f"joyproj v{VERSION} - jayiise@github.com")

def show_help():
  show_header()
  print('''Run project-specific user-defined tasks with the CLI.''')

def get_jp() -> tuple[Path, Path] | None:
  JP_DIR = CWD / ".jp"

  if not JP_DIR.is_dir():
    return None

  JP_CONFIG = JP_DIR / "jp.py"

  if not JP_CONFIG.is_file():
    print("This joyful project is not configured!")
    return None

  return JP_DIR, JP_CONFIG

def handle_jpmodule(JP_DIR, jpmodule, args):
  commands = jpmodule.commands

  if not args[0] in commands:
    print(f"joyproj [{str(JP_DIR)}]: '{args[0]}' is not a valid command in this project!")
    return 0

  commands[args[0]](args)

  return 0

# Interfaces
def cli(args):
  JP_RESULT = get_jp()

  # Probably have this section go to the get_jp() function to just return the jpmodule, for now this works.
  if JP_RESULT != None:
    JP_DIR, JP_CONFIG = JP_RESULT
    spec = importlib.util.spec_from_file_location("jpmodule", JP_CONFIG)
    jpmodule = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(jpmodule)

  if len(args) < 2:
    if JP_RESULT != None:
      print(f"joyproj [{str(JP_DIR)}]: No commands specified!")
    else:
      print("joyproj: No commands specified! Use 'help' for more information.")

    return 0

  if JP_RESULT != None:
    handle_jpmodule(JP_DIR, jpmodule, args[1:])
    return 0

  if args[1] in ("h", "help"):
    show_help()
  elif args[1] in ("v", "version"):
    show_header()
  else:
    print(f"joyproj: '{args[1]}' is not a valid command!")

  return 0

# Main
def main(args):
  cli(args)

main(sys.argv)
