"""InternetBrowser handles the interaction of the users internet browser."""

# Open an internet browser process
from subprocess import Popen
# For using Google search
from webbrowser import open_new_tab

# Import default Module class
from unison.classes.module import Module


class InternetBrowser(Module):
    def __init__(self):
        """Set required inherited parameters."""
        super().__init__(name=InternetBrowser.__name__,
                         verbs=["internet", "google", "browse"])
        self.google_str = "www.google.ca/#q={}"
        self.browse_str = "www.{}"

    def launch_browser(self, browser_path):
        """Launch a process of the users chosen browser."""
        self.process = Popen(browser_path)

    def exit_browser(self):
        """Exit an existing process of the users browser."""
        self.process = self.process.terminate()

    def search_internet(self, query):
        """Open a new tab with query.

        Args:
            query (str): Query for Google search.
        """
        if self.process:
            open_new_tab(self.google_str.format(query))

    def browse_site(self, query):
        """Open a new tab with query as the site.

        Args:
            query (str): Query for site search.
        """
        if self.process:
            open_new_tab(self.browse_str.format(query))

    def run(self, **kwargs):
        """Run module."""
        settings = kwargs["settings"]
        verb = kwargs["verb"]
        noun = kwargs["noun"]
        print(noun)

        browser_path = settings["internet_browser"]

        if verb == "internet":
            if not self.process:
                self.launch_browser(browser_path)
            else:
                self.exit_browser()
        elif verb == "google":
            self.search_internet(noun)
        elif verb == "browse":
            self.browse_site(noun)
