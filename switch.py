from modules.txt_file import TxtFile


class Switch:

    def __init__(self, stt, tts):
        # Set SpeechToText and TextToSpeech objects
        self.stt = stt
        self.tts = tts

        # Initialize object reference variable
        self.obj = None

        # Get all verbs
        self.verbs = self.get_verbs()

    def get_verbs(self):
        with open("./data/settings/verbs.txt") as f:
            f = f.readlines()
            verbs = [verb.strip("\n") for verb in f]
        return verbs

    def cases(self, verb, noun):
        if verb == "open":
            self.obj = TxtFile()

            path = "C:\\Users\Johnathon Kwisses\Desktop\\" + noun + ".txt"
            self.obj.run(path, self.tts)

        if verb == "read":
            self.obj.read_text()

        if verb == "close":
            self.obj.close_file()

    def run(self, msg):
        for verb in self.verbs:
            if verb in msg:
                noun = msg.split(verb + " ")[-1]
                self.cases(verb, noun)
