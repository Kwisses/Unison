"""The "Brain" class handles most of Unison's processing."""

# Import Audio I/O classes
from speech_to_text import SpeechToText
from text_to_speech import TextToSpeech

# Import Switch class for Audio In
from switch import Switch

# Import misc classes
from classes.find import Find
from classes.execute import Execute
from classes.login import Login


class Brain:

    def __init__(self):
        # Initialize Audio I/O objects
        self.stt = SpeechToText()
        self.tts = TextToSpeech()

        # Initialize Switch object
        self.switch = Switch(self.stt, self.tts)

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
            elif "unison" in msg.lower():
                self.switch.run(msg)

            # For debugging...
            else:
                print(msg)
                self.tts.speak(msg)
