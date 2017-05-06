"""Settings class gets and sets all project settings for the program.

There are three types of settings this program uses:
    1. project settings  (global settings)
    2. module settings   (scalable module settings)
    3. instance settings (local settings)
    
These settings are differentiated as to ease the scalability of the program.
    
Each type of setting has its own get and set methods. All of these set
methods are called via the set() method.
"""

# Used for getting local paths
import os


class Settings:

    def __init__(self, mods):
        """Get all data for settings.
        
        Args:
            mods (list): Contains all found modules.
        """
        # Set required parameters
        self.mods = mods

        # Main project setting paths
        project_settings_path = "./data/settings/project_settings.yml"
        module_settings_path = "./data/settings/module_settings.yml"

        # Get all settings
        self.project_settings = self.get_main(project_settings_path)
        self.module_settings = self.get_main(module_settings_path)
        self.instance_settings = self.get_instance()

        # Container for all settings
        self.settings = {}

    @staticmethod
    def get_main(settings_path):
        """Open and read settings_path file and return parsed data.
        
        Args:
            settings_path (str): Path to main settings file.
            
        Returns:
            list: Contains all project settings.
        """
        with open(settings_path) as f:
            ms = [setting.strip("\n") for setting in f.readlines()]
        return ms

    @staticmethod
    def get_instance():
        """Get and return all instance settings.
        
        For this project, instance (local) settings are defined as being 
        settings that correspond to the user's environment. For example, 
        paths to a user's desktop are found and set as they are unique to
        the run instance of the program.
        
        Returns:
            list: Contains all instance settings.
        """
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop\\")
        return [desktop_path]

    def get_verbs(self):
        """Get all verbs found in each mod.verbs list.
        
        Returns:
            list: Contains all verbs found in each mod.verbs list.
            
        Raises:
            KeyError: If there is more than 1 of the same verb found.
            This error will have to be implemented gracefully in future
            versions.
        """
        verbs = []

        for mod in self.mods:
            for verb in mod.verbs:
                verbs.append(verb)

        # Checks if there is more than 1 of the same verb
        if len(verbs) != len(set(verbs)):
            raise KeyError

        return verbs

    def set_main(self, settings):
        """Set settings to self.settings dict.

        Args:
            settings (list): Contains str list of settings.
        """
        for setting in settings:
            key, value = setting.split(": ")
            self.settings[key] = value

    def set_instance(self):
        """Set self.instance_settings to self.settings dict."""
        for setting in self.instance_settings:
            self.settings["desktop_path"] = setting

    def set_verbs(self):
        """Set self.get_verbs to self.settings dict."""
        self.settings["verbs"] = self.get_verbs()

    def set(self):
        """Call all setters for all types of settings; amalgamate data.
        
        Returns:
            dict: key=type of setting; value=value of setting.
        """
        # Set main settings
        self.set_main(self.project_settings)
        self.set_main(self.module_settings)
        self.set_instance()

        # Set additional settings
        self.set_verbs()

        # Return settings dict
        return self.settings
