import configparser
import time
import os

full_path = os.path.dirname(__file__)
path, ldir = os.path.split(full_path)


class ReadINI(object):
    """
    Read ini file
    """
    def __init__(self, *dir_paths):
        self.config = configparser.ConfigParser()
        self.config.optionxform = str
        # section_names = []
        for d in dir_paths:
            f = os.path.join(d, 'config.ini')
            # print(f)
            if os.path.exists(f):
                self.config.read(f)

    def get(self, section_name, prop_name):
        if section_name not in self.config.sections():  # we don't want KeyError
            return None                                 # just return None if not found

        return self.config.get(section_name, prop_name)


# GENERAL
# =================

# library version
VERSION = 'unodit 0.5'

# creation time
NOW = time.strftime("%c")

# LOGGING
# =================

# logger name
LOGGER_NAME = 'unodit'

# log file
LOG_FILE = 'log.log'

# DIRECTORIES
# =================

# unodit dir
MAIN_DIR = path

# templates dir
TEMPLATES_DIR = os.path.join(MAIN_DIR, 'templates')

# pythopath directory - do not change!
IMPORT_DIR = 'pythonpath'

