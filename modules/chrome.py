from apis.chrome_api import ChromeApi
from classes.module import Module


class Chrome(Module, ChromeApi):

    def __init__(self):
        Module.__init__(self, name=Chrome.__name__,
                        verbs=["chrome"])
        ChromeApi.__init__(self)

    def run(self, **kwargs):
        self.open_chrome()
