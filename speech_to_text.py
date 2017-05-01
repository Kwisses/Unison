"""Speech-To-Text tools are stored here."""

from speech_recognition import Microphone, Recognizer, UnknownValueError


class SpeechToText(object):

    def __init__(self):
        self.recognizer = Recognizer()
        self.mic = Microphone()

    def listen(self):
        with self.mic as mic:
            self.recognizer.adjust_for_ambient_noise(mic)
            audio = self.recognizer.listen(mic)

            try:
                msg = self.recognizer.recognize_google(audio, language='en-US')
            except UnknownValueError:
                print("I couldn't understand you, try again!")
            else:
                return msg

    def switch(self, msg):
        print(msg)
