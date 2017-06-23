"""WindowsMediaPlayer enables a user to play a song in Windows Media Player."""

# To get and set desktop path and dir
from os import path

# Opens a program process
from subprocess import Popen

# Inherited by class LocalProgram
from classes.module import Module


class WindowsMediaPlayer(Module):

    def __init__(self):
        """Set required inherited parameters."""
        super().__init__(name=WindowsMediaPlayer.__name__,
                         verbs=["play", "stop"])
        self.ext = ".mp3"

    def play(self, music_player, music):
        """Open a process of music_player with music.
        
        Args:
            music_player (str): Path to music player .exe file.
            music (str): Music to play.
        """
        if not self.process:
            self.process = Popen([music_player, music])

    def stop(self):
        """Terminate instance of music_player."""
        if self.process:
            self.process.terminate()
            self.process = None

    def run(self, **kwargs):
        """Run module by set kwargs and verb switch statement.

        Set using the instructions outlined in the inherited Module class.

        Args:
            **kwargs: 
                settings (dict): All program settings.
                verb (str): Action word to match with module.
                noun (str): Item to be acted upon.
        """
        settings = kwargs["settings"]
        verb = kwargs["verb"]
        noun = kwargs["noun"]

        music_player = settings["music_player"]

        desktop = path.join(settings["desktop"],
                            settings["desktop_dir"])
        music = path.join(desktop, noun + self.ext)

        if verb == "play":
            self.play(music_player, music)
        elif verb == "stop":
            self.stop()
