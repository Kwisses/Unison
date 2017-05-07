from os import mkdir, path


class Desktop:

    def __init__(self):
        pass

    @staticmethod
    def create(settings):
        try:
            directory = path.join(settings["desktop"],
                                  settings["desktop_dir"])
            mkdir(directory)
        except FileExistsError:
            pass
