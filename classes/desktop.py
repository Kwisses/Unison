"""Creates desktop directory for all files and programs to be stored.

In order for the program work as intended, all of the files, folders,
and programs that are to be used with said program MUST be in this
directory! This is because the program and its modules only searches 
this directory for running local processes. By searching in this way, 
it lowers the processing run-time and therefore speeds up return time.
"""

# For creating the program's desktop directory
from os import mkdir, path


class Desktop:

    def __init__(self):
        pass

    @staticmethod
    def create(settings):
        """Make new directory on users desktop if it doesn't exist.
        
        Args:
            settings (dict): All program settings.
            
        Raises:
            FileExistsError: If directory is found.
                             Handle gracefully.
        """
        directory = path.join(settings["desktop"],
                              settings["desktop_dir"])
        try:
            mkdir(directory)
        except FileExistsError as e:
            # Passed as to not log error upon each startup
            pass
        else:
            pass
            # self.set(settings)

    # --- This code copies all .exe files found in C:/program Files
    # --- and copies them to Unison Desktop.

    # --- USE THE BELOW CODE WITH CAUTION!!! ---

    # def set(self, settings):
    #     from os import path, walk, chmod
    #     from shutil import copy
    #     from stat import S_IWRITE
    #     directory = path.join(settings["desktop"],
    #                           settings["desktop_dir"])
    #
    #     root = "C:\\Program Files"
    #     for dirpath, subdirs, files in walk(root):
    #         for name in files:
    #             if name.endswith(".exe"):
    #                 root = path.join(dirpath, name)
    #                 print(root)
    #                 try:
    #                     copy(src=root, dst=directory)
    #                 except PermissionError:
    #                     chmod(name, S_IWRITE)
    #                     copy(src=root, dst=directory)
