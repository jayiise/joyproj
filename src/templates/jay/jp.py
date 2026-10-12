# joyproj - jayiise@github.com
# jp template - change as you wish!

from pathlib import Path
import subprocess

JP_DIR = Path(__file__).parent

def dev(args):
  subprocess.run([JP_DIR / "dev.sh", *args[1:]])  

def build(args):
  subprocess.run([JP_DIR / "build.sh", *args[1:]])  

def run(args):
  subprocess.run([JP_DIR / "run.sh", *args[1:]])  

commands = {
  "dev": dev,
  "build": build,
  "run": run
}
