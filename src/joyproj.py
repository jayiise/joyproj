# joyproj - jayiise@github.com

# Init
from pathlib import Path
from types import ModuleType
import subprocess, json, sys, importlib.util, shutil

PROJECT_DIRECTORY = Path(__file__).parent
VERSION = (PROJECT_DIRECTORY / "VERSION").read_text().strip("\n")
PROJECTS_FILE = PROJECT_DIRECTORY / "projects.json"
TEMPLATES = PROJECT_DIRECTORY / "templates"
CWD = Path.cwd()

# Functions
def show_header():
  print(f"joyproj v{VERSION} - jayiise@github.com")

def show_help():
  show_header()
  print('''A joyful project task runner. [BUGS WILL BE EXPECTED]

Run user-defined tasks for projects using the CLI.''')

def get_projects():
  with open(PROJECTS_FILE, "r") as f:
    return json.load(f)

def write_projects(new_projects: dict[str, str]):
  with open(PROJECTS_FILE, "w") as f:
    json.dump(new_projects, f, indent=4)

def append_project(name: str, path: str):
  if not name or not path:
    return

  projects = get_projects()
  projects[name] = path
  write_projects(projects)

  print(f"joyproj: Added '{name}' to projects!")

def remove_project(name: str):
  projects = get_projects()

  if not name in projects:
    print(f"joyproj: {name} is an invalid project!")
    return

  del projects[name]

  write_projects(projects)
  print(f"joyproj: Removed '{name}' in projects!")

def list_projects():
  print("Joyful projects:")

  for name, path in get_projects().items():
    print(f"  {name}: {path}")

def create_project(name: str, template: str):
  append_project(name, str(CWD))

  TEMPLATE_DIRECTORY = TEMPLATES / template

  if not TEMPLATE_DIRECTORY.is_dir():
    print(f"joyproj: '{template}' is an invalid template! Defaulting to 'minimal'")
    TEMPLATE_DIRECTORY = TEMPLATES / "minimal"

  if (CWD / ".jp").is_dir():
    answer = input("joyproj: Aye! There already exists '.jp' directory. Overwrite it? [y/N]: ")

    if not answer in ("y", "yes"):
      return

    shutil.rmtree(CWD / ".jp")

  shutil.copytree(TEMPLATE_DIRECTORY, CWD / ".jp")

  # Support for any editor desirable? Idk!
  subprocess.run(["nvim", "./.jp/"])

  print("joyproj: Your joyful project (MAYBE) is ready to be used by the CLI!")

def load_jp_project(project_directory: Path) -> tuple[Path, ModuleType] | None:
  JP_DIR = project_directory / ".jp"

  if not JP_DIR.is_dir():
    return None

  JP_CONFIG = JP_DIR / "jp.py"

  if not JP_CONFIG.is_file():
    print("joyproj: This joyful project does not have a configuration file!")
    return None

  spec = importlib.util.spec_from_file_location("jpmodule", JP_CONFIG)
  jpmodule = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(jpmodule)
  return JP_DIR, jpmodule

def handle_jpmodule(JP_DIR: Path, jpmodule: ModuleType, args: tuple[str, ...]):
  commands = jpmodule.commands

  if not args[0] in commands:
    print(f"joyproj [{str(CWD)}]: '{args[0]}' is not a valid command in this project!")
    return

  commands[args[0]](args)
  return

# Interfaces
def cli(args: tuple[str, ...]):
  JP_RESULT = load_jp_project(CWD)

  if JP_RESULT != None:
    JP_DIR, jpmodule = JP_RESULT

  if len(args) < 2:
    if JP_RESULT != None:
      print(f"joyproj [{str(JP_DIR)}]: No commands in project specified!")
    else:
      print("joyproj: No commands specified! Use 'help' for more information.")
    return

  if args[1] in ("h", "help"):
    show_help()
    return
  elif args[1] in ("v", "version"):
    show_header()
    return
  elif args[1] in ("l", "ls", "list"):
    list_projects()
    return
  elif args[1] in ("n", "new"):
    if len(args) < 3:
      print("joyproj: No name argument specified!")
      return

    if len(args) > 3:
      template = args[3]
    else:
      print("joyproj: Automatically using 'minimal' template.")
      template = "minimal"

    create_project(args[2], template) 
    return
  elif args[1] in ("r", "remove"):
    if len(args) < 3:
      print("joyproj: No name argument specified!")
      return

    remove_project(args[2])
    return

  if JP_RESULT != None:
    handle_jpmodule(JP_DIR, jpmodule, args[1:])
    return

  projects = get_projects()

  if not args[1] in projects:
    print(f"joyproj: '{args[1]}' is not a valid command!")
    return

  JS_RESULT = load_jp_project(Path(projects[args[1]]))

  if JP_RESULT != None:
    JS_DIR, jpmodule = JS_RESULT
    handle_jpmodule(JP_DIR, jpmodule, args[2:])

# Main
def main(args: tuple[str, ...]):
  cli(args)

main(sys.argv)
