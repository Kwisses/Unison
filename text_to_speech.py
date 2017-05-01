"""Text-To-Speech tools are stored here."""

from tempfile import NamedTemporaryFile
import os

from requests.exceptions import HTTPError
from gtts import gTTS
from pygame import mixer


class TextToSpeech:

    def __init__(self):
        pass

    def play_mp3(self, filepath):
        mixer.init()

        mixer.music.load(filepath)
        mixer.music.play()

        while mixer.music.get_busy():
            pass

        mixer.quit()

    def speak(self, msg):
        try:
            tts = gTTS(text=msg, lang="en-us")
        except HTTPError as e:
            print("Google TTS might not be updated: " + str(e))
        except Exception as e:
            print("Unknown Google TTS issue: " + str(e))
        else:
            with NamedTemporaryFile(mode='wb', suffix='.mp3',
                                    delete=False) as f:
                tts.write_to_fp(f)

            self.play_mp3(f.name)
            os.remove(f.name)
