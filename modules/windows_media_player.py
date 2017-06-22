# To get and set desktop path and dir
from os import path

# Opens a program process
from subprocess import Popen

# Inherited by class LocalProgram
from classes.module import Module


class WindowsMediaPlayer(Module):

    def __init__(self):
        super().__init__(name=WindowsMediaPlayer.__name__,
                         verbs=["play", "stop"])
        self.ext = ".mp3"

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

        desktop = path.join(settings["desktop"],
                            settings["desktop_dir"])
        music = path.join(desktop, noun + self.ext)

        if verb == "play":
            self.play(music_player, music)
        elif verb == "stop":
            self.stop()
