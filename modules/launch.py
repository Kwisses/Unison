"""Launch module launches a local program."""

from os import path
from subprocess import Popen

from classes.module import Module


class Launch(Module):

    def __init__(self):
        super().__init__(name=Launch.__name__,
                         verbs=["launch", "quit"])
        self.ext = ".exe"

    def launch_program(self, filepath):
        self.process = Popen([filepath])

    def quit_program(self):
        self.process.terminate()

    def run(self, **kwargs):
        # Set variables from kwargs
        settings = kwargs["settings"]
        verb = kwargs["verb"]
        noun = kwargs["noun"]

        # Set path to project's desktop directory
        desktop = path.join(settings["desktop"],
                            settings["desktop_dir"])
        filepath = path.join(desktop, noun + self.ext)

        # Switch statement
        if verb == "launch":
            self.launch_program(filepath)
        else:
            self.quit_program()
