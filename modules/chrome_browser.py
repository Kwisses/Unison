"""Chrome module handles the launch and exit of the Chrome browser."""

# Import the projects Chrome api
from apis.chrome_api import ChromeApi

# Import default Module class
from classes.module import Module


class ChromeBrowser(Module, ChromeApi):

    def __init__(self):
        """Set inherited parameters."""
        Module.__init__(self, name=ChromeBrowser.__name__,
                        verbs=["chrome"])
        ChromeApi.__init__(self)

    def run(self, **kwargs):
        """Run module."""
        self.handle()
