

class Switch:

    def __init__(self, settings, stt, tts, apis, mods):
        # Set all main project data
        self.settings = settings
        self.stt = stt
        self.tts = tts
        self.apis = apis
        self.mods = mods

    def execute_mods(self, verb, noun):
        for mod in self.mods:
            if verb in mod.verbs:
                mod.run(settings=self.settings,
                        stt=self.stt, tts=self.tts,
                        apis=self.apis,
                        noun=noun, verb=verb)

    def run(self, msg):
        for verb in self.settings["verbs"]:
            if verb in msg:
                noun = msg.split(verb + " ")[-1]
                self.execute_mods(verb, noun)
