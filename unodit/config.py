# This file is part of UNO Dialog Tools - UNODIT
# Copyright © 2016-2019 Sasa Kelecevic
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with UNODIT.  If not, see <http://www.gnu.org/licenses/>

"""
UNODIT configuration module.

"""


import configparser
import time
import os

path = os.path.dirname(__file__)


class ReadINI(object):
    """
    Read ini file
    """

    def __init__(self, *dir_paths):
        self.config = configparser.ConfigParser()
        self.config.optionxform = str
        # section_names = []
        for d in dir_paths:
            f = os.path.join(d, "config.ini")
            # print(f)
            if os.path.exists(f):
                self.config.read(f)
                # TODO log paths

    def get(self, section_name, prop_name):
        if section_name not in self.config.sections():  # we don't want KeyError
            return None  # just return None if not found

        return self.config.get(section_name, prop_name)


# GENERAL
# =================

# library version
VERSION = "unodit 0.8.0"

# creation time
NOW = time.strftime("%c")

# LOGGING
# =================

# logger name
LOGGER_NAME = "unodit"

# log file
LOG_FILE = "log.log"

# DIRECTORIES
# =================

# unodit dir
MAIN_DIR = path

# templates dir
TEMPLATES_DIR = os.path.join(MAIN_DIR, "templates")

# pythopath directory - do not change!
IMPORT_DIR = "pythonpath"
