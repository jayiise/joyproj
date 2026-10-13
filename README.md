# joyproj (wip)
A joyful project task runner. (BUGS WILL BE EXPECTED)

Run projects user-defined tasks in the `.jp` directory in the project directory using the CLI.

Practically a throw-away project, don't expect anything useful here.



## Command-line Interface
Outside of a joyful project you can add (only adds current working directory to projects (Like if your project already has a `.jp` directory.) create, remove, list projects. You can also put the project name and the command after to run tasks from there, `joyproj silly-games run` In a joyful project you can directly run tasks with the CLI.

### Commands:
  - h, help | Tells you to redirect to the README.md.
  - v, version | Shows the version.
  - n, new | Creates a new joyful project, adds the current working directory to joyproj's projects, copies a user-specified `.jp` template to your project and boots you into nvim to configure your `.jp` directory.
  - a, add | Only adds the current working directory to joyproj's projects. Use this if your project already has a `.jp` directory.
  - r, remove | Only removes your project from joyproj's projects. It does not delete the projects `.jp` directory.



## `.jp` configuration
In the `.jp` directory you'll usually find a `jp.py` file which contains your declared tasks. The `commands` variable is a table dictionary of indexes, the names of your tasks, and the values, the literal task as a function. Here is a example of a `jp.py` file:

```python
def test(args):
  print("Testing purposes for the audience.")

commands = {
  "test": test
}
```

If you want you can link the function to a bash script in your directory. I don't think that how I did it would be the greatest though.
