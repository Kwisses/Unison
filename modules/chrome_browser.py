"""Chrome module handles the implementation of the Unison's Chrome API."""

# Import the projects Chrome api
from apis.chrome_api import ChromeApi

# Import default Module class
from classes.module import Module


class ChromeBrowser(Module, ChromeApi):

    def __init__(self):
        """Set inherited parameters."""
        Module.__init__(self, name=ChromeBrowser.__name__,
                        verbs=["chrome", "google", "browse"])
        ChromeApi.__init__(self)

    def run(self, **kwargs):
        """Run module."""
        verb = kwargs["verb"]
        noun = kwargs["noun"]

        if verb == "chrome":
            self.handle()
        elif verb == "google":
            self.search_chrome(noun)
        elif verb == "browse":
            self.browse_site(noun)
