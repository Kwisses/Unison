"""Api class is an interface class for all apis to inherit.

The inheritance of this class ensures that each api will work with the core
program's classes.

For more information on how to create an api for this program, visit the 
projects GitHub repository. https://github.com/Kwistech/Unison
"""


class Api:

    def __init__(self):
        """Initialize Api variables."""
        # Set required variables

        # Set additional variables
        self.path = None
        self.process = None
