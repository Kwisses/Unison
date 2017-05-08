"""ChromeAPI connects to the Chrome browser."""

# Open a Chrome process
from subprocess import Popen

# Import default Api class
from classes.api import Api


class ChromeApi(Api):

    def __init__(self):
        """Set required inherited parameters."""
        super().__init__()
        self.path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

    def launch_chrome(self):
        """Launch a process of the Chrome browser."""
        self.process = Popen(self.path)

    def exit_chrome(self):
        """Exit an existing process of the Chrome browser."""
        self.process.terminate()

    def handle(self):
        """Handle processing of Api."""
        # Switch statement
        if self.process:
            self.exit_chrome()
        else:
            self.launch_chrome()
