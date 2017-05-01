"""Speech-To-Text tools are stored here."""

from speech_recognition import Microphone, Recognizer, UnknownValueError


class SpeechToText(object):

    def __init__(self):
        self.rec = Recognizer()
        self.mic = Microphone()

    def listen(self):
        with self.mic as mic:
            self.rec.adjust_for_ambient_noise(mic)
            audio = self.rec.listen(mic)

            try:
                msg = self.rec.recognize_google(audio, language='en-US')
            except UnknownValueError:
                print("I couldn't understand you, try again!")
            else:
                return msg

    def switch(self, msg):
        print(msg)
