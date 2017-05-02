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
        # Start pygame.mixer object.
        mixer.init()

        # Load and play file
        mixer.music.load(filepath)
        mixer.music.play()

        # While the audio is playing, do nothing...
        while mixer.music.get_busy():
            pass

        # Quits mixer object - for
        mixer.quit()

    def speak(self, msg):
        # Get Google TTS object and write it to .mp3 file.
        try:
            tts = gTTS(text=msg, lang="en-us")
        except HTTPError as e:
            print("Google TTS might not be updated: " + str(e))
        except Exception as e:
            print("Unknown Google TTS issue: " + str(e))
        else:
            # Creates a temporary file in the default temp dir
            with NamedTemporaryFile(mode='wb', suffix='.mp3',
                                    delete=False) as f:
                tts.write_to_fp(f)

            # Plays .mp3 file and deletes it after it has been played
            self.play_mp3(f.name)
            try:
                os.remove(f.name)
            except PermissionError as e:
                print(e)
