

class Module(object):

    def __init__(self, name, verb):
        # Essential instance parameters
        self.name = name
        self.verb = verb

        # Other instance parameters
        self.stt = None
        self.tts = None
        self.filename = None
        self.process = None
