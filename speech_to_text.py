"""Speech-To-Text class converts audio to text.

This class uses the speech_recognition package which uses Google Speech 
Recognition to recognize the speech. The package connects to the user's 
computer microphone and uses its' input for the conversion.
"""

from speech_recognition import Microphone, Recognizer, \
    UnknownValueError, RequestError


class SpeechToText(object):

    def __init__(self):
        """Convert audio to text using the speech_recognition package."""
        # Initialize speech_recognition objects
        self.rec = Recognizer()
        self.mic = Microphone()

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
                msg = self.rec.recognize_google(audio, language='en-US')
            except UnknownValueError:
                # Add response code here if user wants error responses
                pass
            except RequestError:
                print("Error: Cannot connect to the Google Api!")
            else:
                return msg
