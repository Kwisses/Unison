
from modules.txt_file import TxtFile


class Switch:

    def __init__(self, stt, tts, settings, mods):
        # Set SpeechToText and TextToSpeech objects
        self.stt = stt
        self.tts = tts
        self.settings = settings
        self.mods = mods

        # Initialize object reference variable
        self.obj = None

        # Set Instance variables
        self.verbs = self.get_verbs()

    def get_verbs(self):
        with open(self.settings["verbs_path"]) as f:
            f = f.readlines()
            verbs = [verb.strip("\n") for verb in f]
        return verbs

    def cases(self, verb, noun):
        for mod in self.mods:
            if verb in mod.verbs:
                # add any additional kwargs below.
                # will need to update this to be more generic
                mod.run(stt=self.stt, tts=self.tts,
                        settings=self.settings,
                        noun=noun, verb=verb)

    def run(self, msg):
        for verb in self.verbs:
            if verb in msg:
                noun = msg.split(verb + " ")[-1]
                self.cases(verb, noun)
