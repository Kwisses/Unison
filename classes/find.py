"""Find class searches for project's api's and modules.

This class loads all of the projects modules and apis into lists to be 
used in core project files (brain.py, switch.py, etc.).
"""

# Verify objects
import inspect

# Handles activity log
import logging as log

# Used for finding local modules
import pkgutil

# Local project packages
import apis
import modules


class Find:

    def __init__(self):
        """Set api and mod instance containers."""
        self.api_lib = []
        self.mod_lib = []

    @staticmethod
    def apis():
        """Find all project-defined apis."""
        api_lib = []

        for finder, name, _ in pkgutil.iter_modules(apis.__path__):
            try:
                file = finder.find_module(name).load_module(name)
                for member in dir(file):
                    obj = getattr(file, member)
                    if inspect.isclass(obj):
                        for parent in obj.__bases__:
                            if 'Api' is parent.__name__:
                                api_lib.append(obj())
            except Exception as e:
                log.error(e)
        return api_lib

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
                log.error(e)
        return mod_lib
