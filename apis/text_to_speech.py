"""Text-To-Speech class converts text to audio using gTTs.

The Google Text-To-Speech API is used to do this conversion. Once converted,
a temporary .mp3 file is created which stores this information and is played 
and then automatically deleted.

Note:
    On occasion, a PermissionError might occur during the deletion process.
    This happens because the audio file is still loaded into this program
    while the system tries to delete it.
    
    If a user's computer runs the program on an SSD (Solid-State Drive), 
    this creation/deletion process will cause wear on the drive over an 
    extended period of time!
"""

# Google Text-To-Speech API
from gtts import gTTS

# Handles activity log
import logging as log

# To remove .mp3 files
from os import remove

# To play .mp3 files
from pygame import mixer

# If the gTTS fails
from requests.exceptions import HTTPError

# To create a temp .mp3 file
from tempfile import NamedTemporaryFile


class TextToSpeech:

    def __init__(self, settings):
        """Convert text to audio using the gTTS api."""
        # Initialize parameters
        self.settings = settings

        # Set instance variables
        self.lang = self.settings["lang"]

    @staticmethod
    def create_mp3(tts):
        """Creates a temporary .mp3 file in the default temp dir.
        
        Args:
            tts (gtts.tts.gTTS): Google Text-To_Speech object.
        
        Returns:
            tempfile._TemporaryFileWrapper: Temp .mp3 file.
        """
        with NamedTemporaryFile(mode='wb', suffix='.mp3',
                                delete=False) as f:
            tts.write_to_fp(f)
        return f

    @staticmethod
    def play_mp3(filepath, clear=True):
        """Handles the play functionality of the pygame.mixer object.
        
        The mixer.init() has the potential to be a memory leak if the 
        program is used for either an extended period of time or
        is scaled to include a substantial amount of calls to it.
        
        Args:
            filepath (str): Path of file to be played.
            clear (bool): If True, call mixer.quit().
        """
        # Start, load, and play pygame.mixer object.
        mixer.init()
        mixer.music.load(filepath)
        mixer.music.play()

        # While the audio is playing, do nothing...
        while mixer.music.get_busy():
            pass

        # Quits mixer object - for gTTS
        if clear:
            mixer.quit()

    @staticmethod
    def delete_mp3(f):
        """Try to delete a temporary .mp3 file.
        
        Args:
            f (tempfile._TemporaryFileWrapper): Temp .mp3 file.
            
        Raises:
            PermissionError: If file is open in another program.
        """
        try:
            remove(f.name)
        except PermissionError as e:
            log.error(e)

    def speak(self, msg):
        """Convert msg to gTTS object to be played as audio.
        
        Args:
            msg (str): Text to be converted to audio.
            
        Raises:
            HTTPError: If program can't connect to gTTS api.
            Exception: Catch-all for additional errors.
        """
        # Get Google TTS object and write it to .mp3 file.
        try:
            tts = gTTS(text=msg, lang=self.lang)
        except HTTPError as e:
            log.error(e.strerror)
        except Exception as e:
            log.error(e)
        else:
            # Create, play, and delete .mp3 file
            f = self.create_mp3(tts)
            self.play_mp3(f.name, clear=True)
            self.delete_mp3(f)
