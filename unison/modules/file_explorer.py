"""Explorer module handles launch and exit of the File Explorer."""

# Used to get path to desktop directory
from os import path
# Opens File Explorer as a process
from subprocess import Popen

# Inherited by class Explorer
from unison.classes.module import Module


class FileExplorer(Module):

    def __init__(self):
        """Set required inherited parameters."""
        super().__init__(name=FileExplorer.__name__,
                         verbs=["explorer"])

    def launch_explorer(self, filepath):
        """Launch an instance of File Explorer with Popen.
        
        Args:
            filepath (str): Path to file to be opened.
        """
        self.process = Popen([r'explorer', "{}".format(filepath)])

    def exit_explorer(self):
        """Terminates self.process."""
        # Not working!
        # Each time an instance of File Explorer is called, it is
        # replaced by another instance of File Explorer by the OS.
        self.process.kill()

    def run(self, **kwargs):
        """Run module by set kwargs and verb switch statement.

        Set using the instructions outlined in the inherited Module class.

        Args:
            **kwargs: 
                settings (dict): All program settings.
                verb (str): Action word to match with module.
                noun (str): Item to be acted upon.
        """
        settings = kwargs["settings"]
        verb = kwargs["verb"]
        noun = kwargs["noun"]

        filepath = path.join(settings["desktop"],
                             settings["desktop_dir"])

        if self.process:
            self.exit_explorer()
        else:
            self.launch_explorer(filepath)
