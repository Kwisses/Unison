from subprocess import Popen

from classes.module import Module


class TxtFile(Module):

    def __init__(self):
        super().__init__()

    def get_text(self):
        with open(self.filename) as f:
            text = f.readlines()[0]
        return text

    def read_text(self):
        text = self.get_text()
        self.tts.speak(text)

    def launch_file(self):
        program_name = "notepad.exe"
        self.process = Popen([program_name, self.filename])

    def close_file(self):
        self.process.terminate()

    def run(self, filename, tts):
        self.filename = filename
        self.tts = tts

        self.launch_file()
