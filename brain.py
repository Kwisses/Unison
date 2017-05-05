"""The "Brain" class handles most of Unison's processing."""

# Import Audio I/O classes
from speech_to_text import SpeechToText
from text_to_speech import TextToSpeech

# Import main program classes
from classes.switch import Switch
from classes.find import Find
from classes.login import Login
from classes.settings import Settings


class Brain:

    def __init__(self):
        # Initialize Audio I/O objects
        self.tts = TextToSpeech()
        self.stt = SpeechToText()

        # Initialize misc objects
        self.apis = Find.apis()
        self.mods = Find.mods()

        # Get and set all settings
        self.settings_obj = Settings(self.mods)
        self.settings = self.settings_obj.set()

        # Initialize Switch object
        self.switch = Switch(self.settings,
                             self.stt, self.tts,
                             self.apis, self.mods)

        # Login
        Login(greet=False)

    def run(self):
        # Main program loop
        while True:
            # User feedback
            self.tts.play_mp3(self.settings["feedback"],
                              cleanup=False)
            print("Listening...")

            # Listen for keyword
            msg = self.stt.listen()

            if not msg:
                continue
            elif self.settings["keyword"] in msg.lower():
                self.switch.run(msg)

            # For debugging...
            # print(msg)
            # self.tts.speak(msg)
