"""Finder class searches for project's api's and modules.

This class loads all of the projects modules and apis into lists to be 
used in core project files (brain.py, switch.py, etc.).
"""

# Verify objects
from inspect import isclass

# Handles activity log
import logging as log

# Used for finding local modules
from pkgutil import iter_modules

# Local project packages
import apis
import modules


class Find:

    def __init__(self):
        """Set api and mod instance containers."""
        pass

    def apis(self):
        """Find all project-defined apis."""
        api_lib = self.run(apis, "Api")
        return api_lib

    def mods(self):
        """Find all project-defined modules."""
        mod_lib = self.run(modules, "Module")
        return mod_lib

    def run(self, pkg, pkg_name):
        """Run generic package finder.

        Args:
            pkg (__init__): Module to search.
            pkg_name (str): Name of package.
        """
        # List to return
        lib = []

        # Search pkg and get all relevant package files
        for finder, name, _ in iter_modules(pkg.__path__):
            try:
                file = finder.find_module(name)
                loaded_file = file.load_module(name)
            except Exception as e:
                log.error(e)
            else:
                for member in dir(loaded_file):
                    obj = getattr(loaded_file, member)
                    if isclass(obj):
                        for parent in obj.__bases__:
                            if pkg_name is parent.__name__:
                                lib.append(obj())
        return lib
