"""Explorer module handles launch and exit of the File Explorer."""

from os import path
from subprocess import Popen

from classes.module import Module


class Explorer(Module):

    def __init__(self):
        super().__init__(name=Explorer.__name__,
                         verbs=["explorer"])

    def launch_explorer(self, filepath):
        self.process = Popen([r'explorer', "{}".format(filepath)])

    def exit_explorer(self):
        # Not working!
        self.process.kill()

    def run(self, **kwargs):
        settings = kwargs["settings"]
        verb = kwargs["verb"]
        noun = kwargs["noun"]

        filepath = path.join(settings["desktop"],
                             settings["desktop_dir"])

        if self.process:
            self.exit_explorer()
        else:
            self.launch_explorer(filepath)
