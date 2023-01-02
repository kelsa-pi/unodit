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
Write sidebars code in files
"""

import os
import string
import logging

try:
    from unodit import config as conf
except ImportError:
    import pythonpath.config as conf


class SidebarGenerator:
    """
    Generate python code
    """

    def __init__(
        self, mode, pydir, xdlfile, context, app="MyApp", indent=4, **kwargs
    ):
        self.xdlfile = xdlfile
        self.context = context
        self.pydir = pydir
        self.app = app
        self.mode = mode
        self.kwargs = kwargs
        self.panel_list = self.get_panel_list()
        self.config = conf.ReadINI(conf.MAIN_DIR, self.pydir)
        self.SOURCE_DIR = self.config.get("directories", "source_dir")
        self.logger = logging.getLogger("unodit.sidebar.SidebarGenerator")
        self.logger.info("NEW LOGGER: unodit.sidebar.SidebarGenerator")

        if self.config.get("directories", "templates_dir") == "templates":
            self.tempates_dir = os.path.join(conf.MAIN_DIR, "templates")
        else:
            self.tempates_dir = self.config.get("directories", "templates_dir")
        self.logger.info("templates directory: " + self.tempates_dir)

        if indent == 0:
            self.indent = "\t"
        else:
            self.indent = indent * " "

        # read all templates
        if self.mode == "sidebar_convert" or self.mode == "sidebar_all":
            # sidebar main exe file
            py_tmpl_dir = os.path.join(self.tempates_dir, "sidebar_convert")
            self.sidebar_main = string.Template(
                self.get_template(py_tmpl_dir, "100_sidebar_main.txt")
            )
            self.sidebar_run_default_menu_command = string.Template(
                self.get_template(py_tmpl_dir, "102_show_menu_command.txt")
            )
            self.sidebar_run_panels = string.Template(
                self.get_template(py_tmpl_dir, "101_sidebar_show_panels.txt")
            )

            self.logger.info("successfully read all templates for script files")

    def get_template(self, py_tmpl_dir, template):
        templ = os.path.join(py_tmpl_dir, template)
        with open(templ, "rt") as t:
            tt = t.read()
        return tt

    def get_panel_list(self):
        for name, value in self.kwargs.items():
            if name == "all_panels":
                pl = value  # .split(',')

        return pl

    # def get_option_panel_list(self):
    #     panel_option_name_list = []
    #     for i in range(0, 20):
    #         panel_section = 'panel' + str(i + 1)
    #         panel_name = self.config.get(panel_section, 'name')
    #         if panel_name:
    #             panel_option_name = self.config.get(panel_section, 'option_name')
    #             if panel_option_name:
    #                 panel_option_name_list.append(panel_option_name)
    #
    #     return panel_option_name_list

    def generate_sidebar_code(self):

        sdb_main = {
            "I": self.indent,
            "IMPORT_PANELS": self._get_import_panels(),
            "EXTENSION_IDENTIFIER_DOMAIN": self.config.get(
                "extension", "identifier_domain"
            ),
            "EXTENSION_IDENTIFIER_APP": self.config.get(
                "extension", "identifier_app"
            ),
            "SIDEBAR_PROTOCOL": self.config.get("sidebar", "protocol"),
            "RUN_DEFAULT_MENU_COMMAND": self._run_default_menu_command(),
            "RUN_PANELS": self._run_panels(),
        }
        sidebar_main = self.sidebar_main.substitute(sdb_main)
        self.write_sidebar_main_file(sidebar_main)

    def _get_import_panels(self):

        logic_dir = self.config.get("sdb_directories", "sdb_ui_logic")
        panels = ""

        # op = self.get_option_panel_list()
        # if op:
        #     self.panel_list = self.panel_list + op

        for panel, option in self.panel_list.items():
            exec_file_name = panel
            panels = (
                panels
                + "from "
                + logic_dir
                + "."
                + exec_file_name
                + " import "
                + exec_file_name
                + "\n"
            )
            if option:
                exec_option_file_name = option
                panels = (
                    panels
                    + "from "
                    + logic_dir
                    + "."
                    + exec_option_file_name
                    + " import "
                    + exec_option_file_name
                    + "\n"
                )

        return panels

    def _run_panels(self):
        code = ""

        for i in self.panel_list:
            pn = {
                "I": self.indent,
                "EXTENSION_IDENTIFIER_APP": self.config.get(
                    "extension", "identifier_app"
                ),
                "PANEL_NAME": i,
            }
            code += self.sidebar_run_panels.substitute(pn)

        return code

    def _run_default_menu_command(self):

        panels = {}
        for i in range(0, 20):
            panel_section = "panel" + str(i + 1)
            panel_name = self.config.get(panel_section, "name")
            if panel_name:
                panel_option_name = self.config.get(
                    panel_section, "option_name"
                )
                if panel_option_name:
                    panels[panel_name] = panel_option_name
                else:
                    panels[panel_name] = ""

        code = ""

        for panel, option in panels.items():
            pn = {
                "I": self.indent,
                "EXTENSION_IDENTIFIER_APP": self.config.get(
                    "extension", "identifier_app"
                ),
                "PANEL_NAME": panel,
                "PANEL_OPTION_NAME": option,
            }
            code += self.sidebar_run_default_menu_command.substitute(pn)

        return code

    def write_sidebar_main_file(self, sdb_text):

        sdb_main = self.app + ".py"
        py_file_path = os.path.join(self.pydir, self.SOURCE_DIR, sdb_main)

        py_main_ui_file = open(py_file_path, "w")
        py_main_ui_file.write(sdb_text)
        py_main_ui_file.close()
