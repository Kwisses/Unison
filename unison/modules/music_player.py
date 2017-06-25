"""MusicPlayer enables a user to play a song in their defined music player."""

# To get and set desktop path and dir
from os import path
# Opens a program process
from subprocess import Popen

# Inherited by class MusicPlayer
from unison.classes.module import Module


class MusicPlayer(Module):

    def __init__(self):
        """Set required inherited parameters."""
        super().__init__(name=MusicPlayer.__name__,
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
        # Set variables from kwargs
        settings = kwargs["settings"]
        verb = kwargs["verb"]
        noun = kwargs["noun"]

        # Get path to user's music player .exe file
        music_player = settings["music_player"]

        # Set path to project's desktop directory
        desktop = path.join(settings["desktop"],
                            settings["desktop_dir"])
        music = path.join(desktop, noun + self.ext)

        # Switch statement
        if verb == "play":
            self.play(music_player, music)
        elif verb == "stop":
            self.stop()
