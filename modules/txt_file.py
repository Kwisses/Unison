from subprocess import Popen

from classes.module import Module


class TxtFile(Module):

    def __init__(self):
        super().__init__(name=TxtFile.__name__,
                         verbs=["open", "read", "close"])

    @staticmethod
    def get_text(filename):
        with open(filename) as f:
            text = f.readlines()[0]
        return text

    def read_text(self, filename, tts):
        text = self.get_text(filename)
        tts.speak(text)

    def launch_file(self, filename):
        program_name = "notepad.exe"
        self.process = Popen([program_name, filename])

    def close_file(self):
        self.process.terminate()

    def run(self, **kwargs):
        # Set variables from kwargs
        tts = kwargs["tts"]
        noun = kwargs["noun"]
        settings = kwargs["settings"]
        verb = kwargs["verb"]

        # Set additional variables
        desktop_path = settings["desktop_path"]
        filename = desktop_path + noun + ".txt"

        # Switch statement
        if verb == "open":
            self.launch_file(filename)
        elif verb == "read":
            self.read_text(filename, tts)
        elif verb == "close":
            self.close_file()
