"""Speech-To-Text tools are stored here."""

from speech_recognition import Microphone, Recognizer, UnknownValueError


class SpeechToText(object):

    def __init__(self):
        # Initialize speech_recognition objects
        self.rec = Recognizer()
        self.mic = Microphone()

    def listen(self):
        with self.mic as mic:
            # Set noise floor and start listening
            self.rec.adjust_for_ambient_noise(mic)
            audio = self.rec.listen(mic)

            # Attempt audio transcription
            try:
                msg = self.rec.recognize_google(audio, language='en-US')
            except UnknownValueError:
                pass
                # print("I couldn't understand you, try again!")
            else:
                return msg
