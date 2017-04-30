import contextlib
import sys
import os


class ErrorHandler:

    def __init__(self):
        pass

    @contextlib.contextmanager
    def ignore_stderr(self):
        """Ignore unwanted 'error' output from pyglet/pyaudio """
        devnull = os.open(os.devnull, os.O_WRONLY)
        old_stderr = os.dup(2)
        sys.stderr.flush()
        os.dup2(devnull, 2)
        os.close(devnull)
        try:
            yield
        finally:
            os.dup2(old_stderr, 2)
            os.close(old_stderr)
