"""Login handles the user login.

The program implements a login feature as to keep track of custom settings.
Note that all of the settings defined in a user's profile WILL OVERWRITE
THE DEFAULT SETTINGS!
"""

# Used to get number of user profiles
from os import listdir


class Login:

    def __init__(self, settings):
        """Handle login components.
        
        Args:
            settings (dict): Contains all settings.
        """
        # Initialize parameters and instance variables
        self.settings = settings
        self.users_path = self.settings["users_path"]

        # Get all user profiles
        self.users = self.get_users()

        # Select one user for login and init settings
        self.user = self.select_user()
        self.user_settings = self.get_user_settings()
        self.set_user_settings()

    def get_users(self):
        """Get all user profiles."""
        users = [user for user in listdir(self.users_path)]
        return users

    def select_user(self):
        """Select one user for login."""
        if len(self.users) == 1:
            user = self.users[0].split(".")[0]
        else:
            print("Which user? ")
            user = input("> ").lower()
        return user

    def get_user_settings(self):
        """Get all user-defined program settings."""
        with open(self.users_path + "/" + self.user + ".yml") as f:
            us = [setting.strip("\n") for setting in f.readlines()]
        return us

    def set_user_settings(self):
        """Set all user-defined program settings.
        
        Note: This will overwrite some default settings!
        """
        for setting in self.user_settings:
            key, value = setting.split(": ")
            self.settings[key] = value
