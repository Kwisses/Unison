"""The "Brain" class handles most of Unison's processing.

This class sets up all instances of all the necessary classes for the program.
It then runs the main loop of the program which handles the calls for the 
program feedback, SpeechToText, Switch and TextToSpeech methods. 
"""

# Handles activity log
import logging as log

# Import Audio I/O classes
from speech_to_text import SpeechToText
from text_to_speech import TextToSpeech

# Import main program classes
from classes.desktop import Desktop
from classes.login import Login
from classes.settings import Settings
from classes.switch import Switch


class Brain:

    def __init__(self):
        """Handle core components of Unison.
        
        Note:
            Any changes made to this class should be made with caution.
        """
        # Get and set all settings, apis, and mods
        self.settings_obj = Settings()
        self.settings = self.settings_obj.set()

        # Initialize Audio I/O objects
        self.tts = TextToSpeech(self.settings)
        self.stt = SpeechToText(self.settings)

        # Initialize Switch object
        self.switch = Switch(self.settings, self.stt, self.tts)

        # Create directory for local file and program access
        Desktop.create(self.settings)

        # User login
        Login(greet=False)

        # Program control variables
        self.feedback = True

    def set_logger(self):
        """Set basic configuration for log."""
        log.basicConfig(filename=self.settings["log_path"],
                        format=self.settings["log_format"],
                        datefmt=self.settings["date_format"])

    def generate_feedback(self):
        """Generate audio and visual feedback for the user."""
        if self.feedback:
            # Audio feedback
            self.tts.play_mp3(self.settings["feedback"], clear=False)

            # Visual feedback
            print("Listening...")

    def process_msg(self, msg):
        """Process msg through if/else statements."""
        # For str consistency
        msg = msg.lower()

        # Select process to run
        if self.settings["keyword"] in msg:
            # Runs switch with msg
            executed = self.switch.run(msg)

            # Handles false positives
            if executed:
                self.feedback = True
            else:
                self.feedback = False

        elif self.settings["quit"] in msg:
            quit()
        else:
            self.feedback = False

    def run(self):
        """Run main program loop."""
        # Set log
        self.set_logger()

        while True:
            # Program feedback
            self.generate_feedback()

            # Listen to audio from mic
            msg = self.stt.listen()
            print(msg)

            # Verify and process audio msg
            if msg:
                self.process_msg(msg)
            else:
                self.feedback = False
                continue

            # --For debugging--
            # self.tts.speak(msg)
