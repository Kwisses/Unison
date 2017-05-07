"""The "Brain" class handles most of Unison's processing.

This class sets up all instances of all the necessary classes for the program.
It then runs the main loop of the program which handles the calls for the 
program feedback, SpeechToText, Switch and TextToSpeech methods. 
"""

# Import Audio I/O classes
from speech_to_text import SpeechToText
from text_to_speech import TextToSpeech

# Import main program classes
from classes.desktop import Desktop
from classes.find import Find
from classes.login import Login
from classes.settings import Settings
from classes.switch import Switch


class Brain:

    def __init__(self):
        """Handle core components of Unison.
        
        Note:
            Any changes made to this class should be made with caution.
        """
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

        # Create directory for local file and program access
        Desktop.create(self.settings)

        # User login
        Login(greet=False)

    def feedback(self):
        """Generate audio and visual feedback for the user."""
        # Audio feedback
        self.tts.play_mp3(self.settings["feedback"], clear=False)

        # Visual feedback
        print("Listening...")

    def run(self):
        """Run main program loop."""
        # Controls call to program feedback()
        feedback = True

        # Main program loop
        while True:

            # Program feedback
            if feedback:
                self.feedback()

            # Listen to audio from mic
            msg = self.stt.listen()

            # Verify audio msg
            if not msg:
                feedback = False
                continue
            else:
                feedback = True
                msg = msg.lower()

            # Process audio message (msg)
            if self.settings["keyword"] in msg:
                self.switch.run(msg)
            elif self.settings["quit"] in msg:
                quit()

            # --For debugging--
            # else:
            #     self.tts.speak(msg)
