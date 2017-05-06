"""TxtFile module opens, reads, and closes a .txt file."""

from os import path

# For opening .txt program
from subprocess import Popen

# Inherited by class TxtFile
from classes.module import Module


class TxtFile(Module):

    def __init__(self):
        """Set required inherited parameters."""
        super().__init__(name=TxtFile.__name__,
                         verbs=["open", "read", "close"])
        self.ext = ".txt"

    @staticmethod
    def get_text(filename):
        """Get text from filename.
        
        Args:
            filename (str): Name of file to get text from.
        
        Returns:
            list: Contains lines from filename.
        """
        with open(filename) as f:
            text = f.readlines()
        return text

    def read_text(self, filename, tts):
        """Read text from filename using tts.
        
        Args:
            filename (str): Name of file to be read.
            tts (text_to_speech.TextToSpeech): tts object.
        """
        text = self.get_text(filename)
        for line in text:
            tts.speak(line)

    def open_file(self, filename, settings):
        """Open filename with given settings.
        
        Args:
            filename (str): Name of file to be opened.
            settings (dict): All program settings.
        """
        program_name = settings["text_program"]
        self.process = Popen([program_name, filename])

    def close_file(self):
        """Terminate self.process (opened file)."""
        self.process.terminate()

    def run(self, **kwargs):
        """Run module by set kwargs and verb switch statement.
        
        Set using the instructions outlined in the inherited Module class.
        
        Args:
            **kwargs: 
                settings (dict): All program settings.
                stt (speech_to_text.SpeechToText): Handles speech-to-text
                tts (text_to_speech.TextToSpeech): Handles text-to-speech
                apis (list): Contains all found apis.
                verb (str): Action word to match with module.
                noun (str): Item to be acted upon.
        """
        # Set variables from kwargs
        tts = kwargs["tts"]
        noun = kwargs["noun"]
        settings = kwargs["settings"]
        verb = kwargs["verb"]

        # Set additional variables
        desktop = path.join(settings["desktop"], settings["desktop_dir"])
        filename = path.join(desktop, noun + self.ext)

        # Switch statement
        if verb == "open":
            self.open_file(filename, settings)
        elif verb == "read":
            self.read_text(filename, tts)
        elif verb == "close":
            self.close_file()
