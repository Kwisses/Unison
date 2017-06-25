"""Finder class searches for project's api's and modules.

This class loads all of the projects modules and apis into lists to be 
used in core project files (brain.py, switch.py, etc.).
"""

# Handles activity log
import logging as log
# Verify objects
from inspect import isclass
# Used for finding local modules
from pkgutil import iter_modules

# Local project packages
from unison import apis
from unison import modules


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

    @staticmethod
    def get_lib_obj(loaded_file, pkg_name, lib):
        """Get all lib objects.
        
        Args:
            loaded_file (module): File to be parsed.
            pkg_name (str): Name of package to be parsed.
            lib (list): Container for all lib objects.
            
        Returns:
            list: Contains all lib objects.
        """
        # Append all apis and/or modules to lib
        for member in dir(loaded_file):
            obj = getattr(loaded_file, member)
            if isclass(obj):
                for parent in obj.__bases__:
                    if pkg_name is parent.__name__:
                        lib.append(obj())

    def run(self, pkg, pkg_name):
        """Run generic package finder.

        Args:
            pkg (__init__): Module to search.
            pkg_name (str): Name of package.
        """
        # List object to be returned
        lib = []

        # Search pkg and get all relevant package files
        for finder, name, _ in iter_modules(pkg.__path__):
            try:
                file = finder.find_module(name)
                loaded_file = file.load_module(name)
            except Exception as e:
                log.error(e)
            else:
                self.get_lib_obj(loaded_file, pkg_name, lib)
        return lib
