
from subprocess import Popen

from classes.api import Api


class GoogleApi(Api):

    def __init__(self):
        super().__init__()

    def open_chrome(self):
        Popen(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])
