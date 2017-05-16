"""Module class is an interface class for all modules to inherit.

Note:
    All modules need to inherit this class!
    
The inheritance of this class ensures that each module will work with the core
program's classes.

For more information on how to create a module for this program, visit the 
projects GitHub repository. https://github.com/Kwistech/Unison
"""

# Handles activity log
import logging


class Module:

    def __init__(self, name, verbs):
        """Set name of module and all verbs used to call it.
        
        Args:
            name (str): The name of the module can be implemented two ways:
                        1. String literal (Ex. 'module name')
                        2. Module.__name__ (Ex. TxtFile.__name__)
            verbs (list): Contains all verbs (as strings)that the developer 
                          wants to use to call the method. 
        """
        # Essential instance parameters
        self.name = name
        self.verbs = verbs

        # Other instance parameters
        self.process = None
        self.exc_format = "[Module] {}: {}"

    def log(self, exc, msg):
        """Log exception (exc) and message (msg) in formatted error.
        
        Note: If a module throws an exception, call this method to log
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

    def run(self, **kwargs):
        """Run the module given kwargs.
        
        Note:
            Each module MUST define a run() method for it to work! Each
            module also needs to manually set the variables inside the 
            kwargs parameter.
        
        Example:
            tts = kwargs["tts"]
            noun = kwargs["noun"]
            settings = kwargs["settings"]
            verb = kwargs["verb"]
        
        The run() method of each module might want to include a switch 
        statement as to what method each verb calls.
        
        Example:
            if verb == "open":
                self.launch_file(settings, filename)
            elif verb == "read":
                self.read_text(filename, tts)
            elif verb == "close":
                self.close_file()
        """
        pass
