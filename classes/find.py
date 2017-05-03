import pkgutil
import inspect
import traceback

import modules


class Find:

    def __init__(self):
        pass

    @staticmethod
    def apis():
        pass

    @staticmethod
    def mods():
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
