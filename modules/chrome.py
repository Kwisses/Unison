from apis.google_api import GoogleApi
from classes.module import Module


class Chrome(Module, GoogleApi):

    def __init__(self):
        Module.__init__(self, name=Chrome.__name__,
                        verbs=["chrome"])
        GoogleApi.__init__(self)

    def run(self, **kwargs):
        self.open_chrome()
