import os


class Settings:

    def __init__(self, mods):
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
        with open(settings_path) as f:
            ps = [setting.strip("\n") for setting in f.readlines()]
        return ps

    @staticmethod
    def get_instance():
        desktop_path = os.path.join(os.environ["HOMEPATH"], "Desktop")
        desktop_path = "C:\\" + desktop_path + "\\"
        return [desktop_path]

    def get_verbs(self):
        verbs = []

        for mod in self.mods:
            for verb in mod.verbs:
                verbs.append(verb)

        # Checks if there is more than 1 of the same verb
        if len(verbs) != len(set(verbs)):
            raise KeyError

        return verbs

    def set_main(self, settings):
        for setting in settings:
            key, value = setting.split(": ")
            self.settings[key] = value

    def set_instance(self):
        for setting in self.instance_settings:
            self.settings["desktop_path"] = setting

    def set_verbs(self):
        self.settings["verbs"] = self.get_verbs()

    def set(self):
        # Set main settings
        self.set_main(self.project_settings)
        self.set_main(self.module_settings)
        self.set_instance()

        # Set additional settings
        self.set_verbs()
        return self.settings
