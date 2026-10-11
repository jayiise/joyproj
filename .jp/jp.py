# joyproj v0.1 - jayiise@github.com
# jp template - change as you wish!

from pathlib import Path
import subprocess, sys

def test(args):
  print(f"Hello joyproj! Extra args: {" ".join(args)}")

def bash_test(args):
  subprocess.run([Path(__file__).parent / "bash-testy.sh", *args[1:]])

def run(args):
  subprocess.run([Path(__file__).parent / "run.sh", *args[1:]])

def build(args):
  subprocess.run([Path(__file__).parent / "build.sh", *args[1:]])

def dev(args):
  subprocess.run([Path(__file__).parent / "dev.sh", *args[1:]])

commands = {
  "testy": test,
  "bash-testy": bash_test,
  "run": run,
  "build": build,
  "dev": dev
}
