

class Module(object):

    def __init__(self, name, verbs):
        # Essential instance parameters
        self.name = name
        self.verbs = verbs

        # Other instance parameters
        self.process = None

    def run(self, **kwargs):
        pass
