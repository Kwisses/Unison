"""Find class searches for project's api's and modules.

This class loads all of the projects modules and apis into lists to be 
used in core project files (brain.py, switch.py, etc.).
"""


# Used for finding local modules
import pkgutil
import inspect
import traceback

# Local project package
import modules


class Find:

    def __init__(self):
        """Set api and mod instance containers."""
        self.api_lib = []
        self.mod_lib = []

    @staticmethod
    def apis():
        """Find all project-defined api's."""
        pass

    @staticmethod
    def mods():
        """Find all project-defined modules."""
        mod_lib = []

        for finder, name, _ in pkgutil.iter_modules(modules.__path__):
            try:
                mod = finder.find_module(name).load_module(name)
                for member in dir(mod):
                    obj = getattr(mod, member)
                    if inspect.isclass(obj):
                        for parent in obj.__bases__:
                            if 'Module' is parent.__name__:
                                mod_lib.append(obj())
            except Exception as e:
                print(traceback.format_exc())
        return mod_lib
