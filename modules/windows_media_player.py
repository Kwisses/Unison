

# Opens a program process
from subprocess import Popen

# Inherited by class LocalProgram
from classes.module import Module


class WindowsMediaPlayer(Module):

    def __init__(self):
        super().__init__(name=WindowsMediaPlayer.__name__,
                         verbs=["play", "stop"])

    def play(self, music_player, music):
        if not self.process:
            self.process = Popen([music_player, music])

    def stop(self):
        if self.process:
            self.process.terminate()

    def run(self, **kwargs):
        verb = kwargs["verb"]
        noun = kwargs["noun"]
        settings = kwargs["settings"]

        music_player = settings["music_player"]

        if verb == "play":
            self.play(music_player, noun)
        elif verb == "stop":
            self.stop()
