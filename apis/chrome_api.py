"""ChromeAPI connects to the Chrome browser."""

# Open a Chrome process
from subprocess import Popen

# Import default Api class
from classes.api import Api

# For using Google search
from webbrowser import open_new_tab


class ChromeApi(Api):

    def __init__(self):
        """Set required inherited parameters."""
        super().__init__()
        self.path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        self.google_str = "www.google.ca/#q={}"
        self.browse_str = "www."

    def launch_chrome(self):
        """Launch a process of the Chrome browser."""
        self.process = Popen(self.path)

    def exit_chrome(self):
        """Exit an existing process of the Chrome browser."""
        self.process = self.process.terminate()

    def search_chrome(self, query):
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

    def handle(self):
        """Handle processing of Api."""
        # Switch statement
        if self.process:
            self.exit_chrome()
        else:
            self.launch_chrome()
