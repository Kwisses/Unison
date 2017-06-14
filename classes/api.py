"""Api class is an interface class for all apis to inherit.

The inheritance of this class ensures that each api will work with the core
program's classes.

For more information on how to create an api for this program, visit the 
projects GitHub repository. https://github.com/Kwistech/Unison
"""

# Handles activity log
import logging


class Api:

    def __init__(self):
        """Initialize Api variables."""
        # Set required variables

        # Set additional variables
        self.path = None
        self.process = None
        self.exc_format = "[API] {}: {}"

    def log(self, exc, msg):
        """Log exception (exc) and message (msg) in formatted error.

        Note: If an API throws an exception, call this method to log
        the error.

        Example:
            try:
                with open(filename) as f:
                    text = f.readlines()
            except FileNotFoundError as e:
                self.log(FileNotFoundError, e)  <--
            else:
                return text

        Args:
            exc (type): Name of exception.
            msg (Exception): Error message.
        """
        err = self.exc_format.format(exc.__name__, msg)
        logging.error(err)
