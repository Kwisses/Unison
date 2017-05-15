"""Login handles the user login.

The program implements a login feature as to keep track of custom settings.
Note that all of the settings defined in a user's profile WILL OVERWRITE
THE DEFAULT SETTINGS!
"""

# Handles activity log
import logging as log

# Used to get number of user profiles
from os import listdir


class Login:

    def __init__(self, settings, ext=".yml"):
        """Handle login components.
        
        Args:
            settings (dict): Contains all settings.
        """
        # Initialize parameters
        self.settings = settings
        self.ext = ext

        # Set instance variables
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

    def create_user(self):
        """Create a user profile .yml file."""
        # User enters required info below
        print("Please provide your name and email below.")
        name = input("Name: ").lower()
        email = input("Email: ").lower()

        # Set variables for new file
        lines = ["name: {}\n".format(name), "email: {}\n".format(email)]
        filepath = self.users_path + "/" + name + self.ext

        # Write new file to filepath
        try:
            with open(filepath, "w+") as f:
                f.writelines(lines)
        except Exception as e:
            log.error(e)

    def select_user(self):
        """Select one user for login."""
        # Call create_user if no user exists
        if not self.users:
            self.create_user()
            self.users = self.get_users()

        # Select user
        if len(self.users) == 1:
            user = self.users[0].split(".")[0]
        else:
            print("Which user? ")
            user = input("> ").lower()

        return user

    def get_user_settings(self):
        """Get all user-defined program settings."""
        filepath = self.users_path + "/" + self.user + self.ext
        with open(filepath) as f:
            us = [setting.strip("\n") for setting in f.readlines()]
        return us

    def set_user_settings(self):
        """Set all user-defined program settings.
        
        Note: This will overwrite some default settings!
        """
        for setting in self.user_settings:
            key, value = setting.split(": ")
            self.settings[key] = value
