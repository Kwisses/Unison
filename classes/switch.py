
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
        # This is almost generic. Need to transfer specific info to the
        # module and keep the run() method simple with only noun required
        # I will need to implement more verbs (maybe a list of verbs) inside
        # each module to check for.
        for mod in self.mods:
            if verb == mod.verb:
                path = self.settings["desktop_path"] + noun + ".txt"
                mod.run(noun=noun, filename=path, tts=self.tts)

        # if verb == "open":
        #     self.obj = TxtFile()
        #     path = self.settings["desktop_path"] + noun + ".txt"
        #     self.obj.run(path, self.tts)
        #
        # if verb == "read":
        #     self.obj.read_text()
        #
        # if verb == "close":
        #     self.obj.close_file()

    def run(self, msg):
        for verb in self.verbs:
            if verb in msg:
                noun = msg.split(verb + " ")[-1]
                self.cases(verb, noun)
