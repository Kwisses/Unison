"""Program module launches and exits a local program."""

# To get and set desktop path and dir
from os import path

# Opens a program process
from subprocess import Popen

# # Inherited by class Program
from classes.module import Module


class Program(Module):

    def __init__(self):
        """Set required inherited parameters."""
        super().__init__(name=Program.__name__,
                         verbs=["launch", "exit"])
        self.ext = ".exe"

    def launch_program(self, filepath):
        """Open a process of filepath.
        
        Args:
            filepath (str): Path to program's launcher.
        """
        self.process = Popen([filepath])

    def exit_program(self):
        """Terminate self.process (launched program)."""
        self.process.terminate()

    def run(self, **kwargs):
        """Run module by set kwargs and verb switch statement.

        Set using the instructions outlined in the inherited Module class.

        Args:
            **kwargs: 
                settings (dict): All program settings.
                verb (str): Action word to match with module.
                noun (str): Item to be acted upon.
        """
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
        elif verb == "quit":
            self.exit_program()
