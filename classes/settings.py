import os


class Settings:

    def __init__(self):
        self.settings_path = "./data/settings/global_settings.yml"
        self.global_settings = self.get_global_settings()
        self.instance_settings = self.get_instance_settings()
        self.settings = {}

    def get_global_settings(self):
        with open(self.settings_path) as f:
            f = [setting.strip("\n") for setting in f.readlines()]
        return f

    def get_instance_settings(self):
        desktop_path = os.path.join(os.environ["HOMEPATH"], "Desktop")
        desktop_path = "C:\\" + desktop_path + "\\"
        return [desktop_path]

    def get_verbs(self):
        with open(self.settings["verbs_path"]) as f:
            f = f.readlines()
            verbs = [verb.strip("\n") for verb in f]
        return verbs

    def set_global_settings(self):
        for setting in self.global_settings:
            key, value = setting.split(": ")
            self.settings[key] = value

    def set_instance_settings(self):
        for setting in self.instance_settings:
            self.settings["desktop_path"] = setting

    def set_verbs(self):
        self.settings["verbs"] = self.get_verbs()

    def set(self):
        self.set_global_settings()
        self.set_instance_settings()
        self.set_verbs()
        return self.settings
