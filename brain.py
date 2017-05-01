"""The "Brain" class handles most of Unison's processing."""

from speech_to_text import SpeechToText
from text_to_speech import TextToSpeech

from classes.find import Find
from classes.execute import Execute
from classes.login import Login


class Brain:

    def __init__(self):
        self.stt = SpeechToText()
        self.tts = TextToSpeech()

        Find.apis()
        Find.mods()

        Login(greet=False)

    def run(self):

        while True:
            print("Listening...")
            msg = self.stt.listen()

            if msg == "unison":
                print("yes?")
                msg = self.stt.listen()
                self.stt.switch(msg)
            else:
                print(msg)
                self.tts.speak(msg)
