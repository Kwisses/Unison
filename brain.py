"""The "Brain" class handles most of Unison's processing."""

# Import Settings class
from settings import Settings

# Import Audio I/O classes
from speech_to_text import SpeechToText
from text_to_speech import TextToSpeech

# Import Switch class for Audio In
from switch import Switch

# Import misc classes
from classes.find import Find
from classes.login import Login


class Brain:

    def __init__(self):
        # Get and set all settings
        self.settings_obj = Settings()
        self.settings = self.settings_obj.set()

        # Initialize Audio I/O objects
        self.stt = SpeechToText()
        self.tts = TextToSpeech()

        # Initialize Switch object
        self.switch = Switch(self.stt, self.tts, self.settings)

        # Initialize misc objects
        Find.apis()
        Find.mods()

        # Login
        Login(greet=False)

    def run(self):
        # Main program loop
        while True:
            # Listen for keyword
            print("Listening...")
            msg = self.stt.listen()

            if not msg:
                continue
            elif self.settings["keyword"] in msg.lower():
                self.switch.run(msg)

            # For debugging...
            # else:
            #     print(msg)
            #     self.tts.speak(msg)
