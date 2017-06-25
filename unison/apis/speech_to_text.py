"""Speech-To-Text class converts audio to text.

This class uses the speech_recognition package which uses Google Speech 
Recognition to recognize the speech. The package connects to the user's 
computer microphone and uses its' input for the conversion.
"""

# Handles activity log
import logging as log

# Speech recognizer
from speech_recognition import Microphone, Recognizer, \
    UnknownValueError, RequestError


class SpeechToText:

    def __init__(self, settings):
        """Convert audio to text using the speech_recognition package."""
        # Initialize parameters
        self.settings = settings

        # Initialize speech_recognition objects
        self.rec = Recognizer()
        self.mic = Microphone()

        # Set instance variables
        self.lang = self.settings["lang"]
        self.error = False

    def listen(self):
        """Open dynamic microphone input and try audio to text conversion.
        
        A microphone is initialized and then set to the appropriate ambient
        noise threshold. This improves the accuracy of the audio. 

        The method then 'listens' for user input. Once there is user input, 
        the method then tries to convert the audio to text.
        """
        with self.mic as mic:
            # Set noise floor and start listening
            self.rec.adjust_for_ambient_noise(mic)
            audio = self.rec.listen(mic)

            # Attempt audio transcription
            try:
                msg = self.rec.recognize_google(audio, language=self.lang)
            except UnknownValueError:
                # Passed as to not log msg of 'None'
                pass
            except RequestError as e:
                # Handle multiple log entries
                print("Can't connect to the internet!")
                if not self.error:
                    log.error(e)
                    self.error = True
            else:
                self.error = False
                return msg
