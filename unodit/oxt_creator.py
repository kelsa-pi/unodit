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
Create script and sidebar extension files and extension(.oxt)
"""
import fnmatch
import os
import string
import zipfile
import logging
import shutil

try:
    from unodit import config as conf
except ImportError:
    import pythonpath.config as conf


class BaseExtension:
    def __init__(self, mode, pydir, app="MyApp", panel=2):
        self.pydir = pydir
        self.app = app
        self.mode = mode
        self.panels = panel
        self.config = conf.ReadINI(conf.MAIN_DIR, self.pydir)

    def get_template(self, ex_tmpl_dir, template):
        templ = os.path.join(ex_tmpl_dir, template)
        with open(templ, "rt") as t:
            tt = t.read()
        return tt

    def create_oxt(self, oxt_name):
        oxt = os.path.join(self.pydir, oxt_name)
        exclude_files = self.config.get("oxt", "exclude")
        exclude_dir = self.config.get("oxt", "exclude_dir")
        self.config.get("directories", "templates_dir")
        # add directories and files in zip file
        with zipfile.ZipFile(oxt, "w", zipfile.ZIP_DEFLATED) as oxt_zip_file:
            root_len = len(self.pydir) + 1
            for base, dirs, files in os.walk(self.pydir, topdown=True):
                dirs[:] = [d for d in dirs if d not in exclude_dir]
                for file in files:
                    badFile = False

                    for pattern in exclude_files.split(","):
                        if fnmatch.fnmatch(file, pattern):
                            badFile = True

                    if not badFile:
                        file_path = os.path.join(base, file)
                        zip_file_path = file_path[root_len:].replace("\\", "/")
                        # print(file_path + ' - ' + zip_file_path)
                        oxt_zip_file.write(file_path, zip_file_path)
        oxt_zip_file.close()


class ScriptExtensionFiles(BaseExtension):
    def __init__(self, *args, **kwargs):
        super(ScriptExtensionFiles, self).__init__(*args, **kwargs)
        self.code = {}
        self.config = conf.ReadINI(conf.MAIN_DIR, self.pydir)
        self.ext_tmpl_dir = os.path.join(conf.TEMPLATES_DIR, "script_ext")
        self.logger = logging.getLogger(
            "unodit.oxt_creator.ScriptExtensionFiles"
        )
        self.logger.info("NEW LOGGER: unodit.oxt_creator.ScriptExtensionFiles")

    def ext_meta(self):

        d = os.path.join(self.pydir, self.config.get("script_ext_meta", "dir"))
        if not os.path.exists(d):
            os.makedirs(d)

        s = {
            "SOURCE": self.config.get("directories", "source_dir"),
            "ADD_ON_MENU": self.config.get("script_add_on_menu", "file"),
            "APP_DESCRIPTION": self.config.get("script_app_description", "dir"),
            "APP_TITLE": self.config.get("script_app_title", "file"),
        }

        f = os.path.join(d, self.config.get("script_ext_meta", "file"))
        t = string.Template(
            self.get_template(
                self.ext_tmpl_dir,
                self.config.get("script_ext_meta", "template"),
            )
        )
        ext_text = t.substitute(s)

        ef = open(f, "w")
        ef.write(ext_text)
        ef.close()
        self.logger.info("manifest.xml " + f + " " + str(s))

    def ext_description(self):
        s = {
            "EXTENSION_IDENTIFIER_DOMAIN": self.config.get(
                "extension", "identifier_domain"
            ),
            "EXTENSION_IDENTIFIER_APP": self.config.get(
                "extension", "identifier_app"
            ),
            "EXTENSION_VERSION": self.config.get("extension", "version"),
            "EXTENSION_PLATFORM": self.config.get("extension", "platform"),
            "EXTENSION_PUBLISHER": self.config.get("extension", "publisher"),
            "EXTENSION_MAILTO": self.config.get("extension", "mailto"),
            "APP_LICENSE_DIR": self.config.get("script_app_license", "dir"),
            "APP_LICENSE": self.config.get("script_app_license", "file"),
            "DISPLAY_NAME": self.app,
            "APP_DESCRIPTION_DIR": self.config.get(
                "script_app_description", "dir"
            ),
            "APP_DESCRIPTION": self.config.get(
                "script_app_description", "file"
            ),
        }

        f = os.path.join(
            self.pydir, self.config.get("script_ext_description", "file")
        )
        t = string.Template(
            self.get_template(
                self.ext_tmpl_dir,
                self.config.get("script_ext_description", "template"),
            )
        )
        ext_text = t.substitute(s)

        ef = open(f, "w")
        ef.write(ext_text)
        ef.close()
        self.logger.info("description.xml " + f + " " + str(s))

    def app_license(self):

        d = os.path.join(
            self.pydir, self.config.get("script_app_license", "dir")
        )
        if not os.path.exists(d):
            os.makedirs(d)

        s = {}

        f = os.path.join(d, self.config.get("script_app_license", "file"))
        t = string.Template(
            self.get_template(
                self.ext_tmpl_dir,
                self.config.get("script_app_license", "template"),
            )
        )
        ext_text = t.substitute(s)

        ef = open(f, "w")
        ef.write(ext_text)
        ef.close()
        self.logger.info("license file " + f)

    def app_description(self):

        d = os.path.join(
            self.pydir, self.config.get("script_app_description", "dir")
        )
        if not os.path.exists(d):
            os.makedirs(d)

        s = {}

        f = os.path.join(d, self.config.get("script_app_description", "file"))
        t = string.Template(
            self.get_template(
                self.ext_tmpl_dir,
                self.config.get("script_app_description", "template"),
            )
        )
        ext_text = t.substitute(s)

        ef = open(f, "w")
        ef.write(ext_text)
        ef.close()
        self.logger.info("app description file " + f)

    def app_title(self):

        d = os.path.join(self.pydir, self.config.get("script_app_title", "dir"))
        if not os.path.exists(d):
            os.makedirs(d)

        s = {}

        f = os.path.join(d, self.config.get("script_app_title", "file"))
        t = string.Template(
            self.get_template(
                self.ext_tmpl_dir,
                self.config.get("script_app_title", "template"),
            )
        )
        ext_text = t.substitute(s)

        ef = open(f, "w")
        ef.write(ext_text)
        ef.close()
        self.logger.info("app title file " + f)

    def ext_add_on_menu(self):

        s = {
            "EXTENSION_IDENTIFIER_DOMAIN": self.config.get(
                "extension", "identifier_domain"
            ),
            "EXTENSION_IDENTIFIER_APP": self.config.get(
                "extension", "identifier_app"
            ),
            "TITLE": self.app,
            "OXT_NAME": self.app
            + self.config.get("oxt", "name_sufix")
            + ".oxt",
            "SOURCE": self.config.get("directories", "source_dir"),
            "EXEC_FILE_NAME": self.app + ".py",
            "EXEC_FUNCTION": self.config.get("exec_function", "prefix")
            + self.app,
            "INSTALL": self.config.get("script_install", "location"),
        }
        f = os.path.join(
            self.pydir, self.config.get("script_add_on_menu", "file")
        )
        t = string.Template(
            self.get_template(
                self.ext_tmpl_dir,
                self.config.get("script_add_on_menu", "template"),
            )
        )
        ext_text = t.substitute(s)

        ef = open(f, "w")
        ef.write(ext_text)
        ef.close()
        self.logger.info("app add_on_menu file " + f + " " + str(s))

    def create(self):
        self.ext_meta()
        self.ext_description()
        self.app_license()
        self.app_description()
        self.app_title()
        self.ext_add_on_menu()


class CreateScriptExtension(BaseExtension):
    def __init__(self, *args, **kwargs):
        super(CreateScriptExtension, self).__init__(*args, **kwargs)
        self.config = conf.ReadINI(conf.MAIN_DIR, self.pydir)
        self.logger = logging.getLogger(
            "unodit.oxt_creator.CreateScriptExtension"
        )
        self.logger.info("NEW LOGGER: unodit.oxt_creator.CreateScriptExtension")

    def create(self):
        oxt_name = self.app + self.config.get("oxt", "name_sufix") + ".oxt"
        self.create_oxt(oxt_name)
        self.logger.info("oxt: " + oxt_name)


class SidebarExtensionFiles(BaseExtension):
    def __init__(self, *args, **kwargs):
        super(SidebarExtensionFiles, self).__init__(*args, **kwargs)
        self.code = {}
        self.config = conf.ReadINI(conf.MAIN_DIR, self.pydir)
        self.ext_tmpl_dir = os.path.join(
            conf.TEMPLATES_DIR, "sidebar_convert_ext"
        )
        self.logger = logging.getLogger(
            "unodit.oxt_creator.SidebarExtensionFiles"
        )
        self.logger.info("NEW LOGGER: unodit.oxt_creator.SidebarExtensionFiles")

    def ext_meta(self):

        d = os.path.join(self.pydir, self.config.get("sidebar_ext_meta", "dir"))
        if not os.path.exists(d):
            os.makedirs(d)

        s = {
            "SOURCE": self.config.get("directories", "source_dir"),
            "EXEC_FILE_NAME": self.app + ".py",
            "FACTORY": self.config.get("sidebar_panel_factory", "file"),
            "PROTOCOL": self.config.get("sidebar_protocol_handler", "file"),
            "SIDEBAR": self.config.get("sidebar_configuration", "file"),
            "APP_DESCRIPTION": self.config.get(
                "sidebar_app_description", "dir"
            ),
            "APP_TITLE": self.config.get("sidebar_app_title", "file"),
        }

        f = os.path.join(d, self.config.get("sidebar_ext_meta", "file"))
        t = string.Template(
            self.get_template(
                self.ext_tmpl_dir,
                self.config.get("sidebar_ext_meta", "template"),
            )
        )
        ext_text = t.substitute(s)

        ef = open(f, "w")
        ef.write(ext_text)
        ef.close()
        self.logger.info("manifest.xml " + f + " " + str(s))

    def ext_description(self):
        s = {
            "EXTENSION_IDENTIFIER_DOMAIN": self.config.get(
                "extension", "identifier_domain"
            ),
            "EXTENSION_IDENTIFIER_APP": self.config.get(
                "extension", "identifier_app"
            ),
            "EXTENSION_VERSION": self.config.get("extension", "version"),
            "EXTENSION_PLATFORM": self.config.get("extension", "platform"),
            "EXTENSION_PUBLISHER": self.config.get("extension", "publisher"),
            "EXTENSION_MAILTO": self.config.get("extension", "mailto"),
            "APP_LICENSE_DIR": self.config.get("sidebar_app_license", "dir"),
            "APP_LICENSE": self.config.get("sidebar_app_license", "file"),
            "DISPLAY_NAME": self.app,
            "APP_DESCRIPTION_DIR": self.config.get(
                "sidebar_app_description", "dir"
            ),
            "APP_DESCRIPTION": self.config.get(
                "sidebar_app_description", "file"
            ),
        }

        f = os.path.join(
            self.pydir, self.config.get("script_ext_description", "file")
        )
        t = string.Template(
            self.get_template(
                self.ext_tmpl_dir,
                self.config.get("sidebar_ext_description", "template"),
            )
        )
        ext_text = t.substitute(s)

        ef = open(f, "w")
        ef.write(ext_text)
        ef.close()
        self.logger.info("description.xml " + f + " " + str(s))

    def app_license(self):

        d = os.path.join(
            self.pydir, self.config.get("sidebar_app_license", "dir")
        )
        if not os.path.exists(d):
            os.makedirs(d)

        s = {}

        f = os.path.join(d, self.config.get("sidebar_app_license", "file"))
        t = string.Template(
            self.get_template(
                self.ext_tmpl_dir,
                self.config.get("sidebar_app_license", "template"),
            )
        )
        ext_text = t.substitute(s)

        ef = open(f, "w")
        ef.write(ext_text)
        ef.close()
        self.logger.info("license file " + f)

    def app_description(self):

        d = os.path.join(
            self.pydir, self.config.get("sidebar_app_description", "dir")
        )
        if not os.path.exists(d):
            os.makedirs(d)

        s = {}

        f = os.path.join(d, self.config.get("sidebar_app_description", "file"))
        t = string.Template(
            self.get_template(
                self.ext_tmpl_dir,
                self.config.get("sidebar_app_description", "template"),
            )
        )
        ext_text = t.substitute(s)

        ef = open(f, "w")
        ef.write(ext_text)
        ef.close()
        self.logger.info("app description file " + f)

    def app_title(self):

        d = os.path.join(
            self.pydir, self.config.get("sidebar_app_title", "dir")
        )
        if not os.path.exists(d):
            os.makedirs(d)

        s = {}

        f = os.path.join(d, self.config.get("sidebar_app_title", "file"))
        t = string.Template(
            self.get_template(
                self.ext_tmpl_dir,
                self.config.get("sidebar_app_title", "template"),
            )
        )
        ext_text = t.substitute(s)

        ef = open(f, "w")
        ef.write(ext_text)
        ef.close()
        self.logger.info("app title file " + f)

    def sidebar_factory(self):
        s = {
            "EXTENSION_IDENTIFIER_DOMAIN": self.config.get(
                "extension", "identifier_domain"
            ),
            "EXTENSION_IDENTIFIER_APP": self.config.get(
                "extension", "identifier_app"
            ),
        }

        f = os.path.join(
            self.pydir, self.config.get("sidebar_panel_factory", "file")
        )
        t = string.Template(
            self.get_template(
                self.ext_tmpl_dir,
                self.config.get("sidebar_panel_factory", "template"),
            )
        )
        ext_text = t.substitute(s)

        ef = open(f, "w")
        ef.write(ext_text)
        ef.close()
        self.logger.info("sidebar panel factory " + f + " " + str(s))

    def sidebar_protocol(self):

        s = {
            "EXTENSION_IDENTIFIER_DOMAIN": self.config.get(
                "extension", "identifier_domain"
            ),
            "SIDEBAR_PROTOCOL": self.config.get("sidebar", "protocol"),
        }

        f = os.path.join(
            self.pydir, self.config.get("sidebar_protocol_handler", "file")
        )
        t = string.Template(
            self.get_template(
                self.ext_tmpl_dir,
                self.config.get("sidebar_protocol_handler", "template"),
            )
        )
        ext_text = t.substitute(s)

        ef = open(f, "w")
        ef.write(ext_text)
        ef.close()
        self.logger.info("sidebar protocol handler " + f + " " + str(s))

    def get_sidebar_panels(self):
        code = ""
        for i in range(0, self.panels):
            # read config.ini for xdl file

            panel_section = "panel" + str(i + 1)

            s = {
                "EXTENSION_IDENTIFIER_DOMAIN": self.config.get(
                    "extension", "identifier_domain"
                ),
                "EXTENSION_IDENTIFIER_APP": self.config.get(
                    "extension", "identifier_app"
                ),
                "PANEL_NAME": self.config.get(panel_section, "name"),
                "PANEL_TITLE": self.config.get(panel_section, "title").strip(
                    '"'
                ),
                "PANEL_ID": self.config.get(panel_section, "id"),
                "DECK_ID": self.config.get("deck", "id"),
                "PANEL_CONTEXT": self.config.get(panel_section, "context"),
                "PANEL_ORDER_INDEX": self.config.get(
                    panel_section, "order_index"
                ),
            }
            t = string.Template(
                self.get_template(
                    self.ext_tmpl_dir,
                    self.config.get("sidebar_panel", "template"),
                )
            )
            ext_text = t.substitute(s)
            code = code + ext_text
        return code

    def sidebar(self):
        s = {
            "EXTENSION_IDENTIFIER_DOMAIN": self.config.get(
                "extension", "identifier_domain"
            ),
            "EXTENSION_IDENTIFIER_APP": self.config.get(
                "extension", "identifier_app"
            ),
            "DECK_NAME": self.config.get("deck", "name"),
            "DECK_TITLE": self.config.get("deck", "title").strip('"'),
            "DECK_ID": self.config.get("deck", "id"),
            "SIDEBAR_ICON_DIR": self.config.get("sidebar_icon", "dir"),
            "SIDEBAR_ICON": self.config.get("sidebar_icon", "file"),
            "SIDEBAR_CONTEXT": self.config.get("deck", "context"),
            "SIDEBAR_PANELS": self.get_sidebar_panels(),
        }

        f = os.path.join(
            self.pydir, self.config.get("sidebar_configuration", "file")
        )
        t = string.Template(
            self.get_template(
                self.ext_tmpl_dir,
                self.config.get("sidebar_configuration", "template"),
            )
        )
        ext_text = t.substitute(s)

        ef = open(f, "w")
        ef.write(ext_text)
        ef.close()
        self.logger.info("sidebar protocol handler " + f + " " + str(s))

    def sidebar_icon(self):
        d = os.path.join(self.pydir, self.config.get("sidebar_icon", "dir"))
        if not os.path.exists(d):
            os.makedirs(d)

        icon_src = os.path.join(
            conf.TEMPLATES_DIR,
            "sidebar_convert_ext",
            self.config.get("sidebar_icon", "template"),
        )
        icon_dest = os.path.join(d, self.config.get("sidebar_icon", "file"))

        shutil.copy(icon_src, icon_dest)
        self.logger.info("app icon file " + icon_dest)

    def sidebar_empty_dialog(self):

        dlg_src = os.path.join(
            conf.TEMPLATES_DIR, "sidebar_convert_ext", "8_empty_dialog.xdl"
        )
        dlg_dest = os.path.join(self.pydir, "empty_dialog.xdl")

        shutil.copy(dlg_src, dlg_dest)
        self.logger.info("app empty dialog " + dlg_dest)

    def create(self):
        self.ext_meta()
        self.ext_description()
        self.app_license()
        self.app_description()
        self.app_title()
        self.sidebar_factory()
        self.sidebar_protocol()
        self.sidebar_icon()
        self.sidebar()
        self.sidebar_empty_dialog()


class CreateSidebarExtension(BaseExtension):
    def __init__(self, *args, **kwargs):
        super(CreateSidebarExtension, self).__init__(*args, **kwargs)
        self.config = conf.ReadINI(conf.MAIN_DIR, self.pydir)
        self.logger = logging.getLogger(
            "unodit.oxt_creator.CreateSidebarExtension"
        )
        self.logger.info(
            "NEW LOGGER: unodit.oxt_creator.CreateSidebarExtension"
        )

    def create(self):
        oxt_name = self.app + self.config.get("oxt", "name_sufix") + ".oxt"
        self.create_oxt(oxt_name)
        self.logger.info("oxt: " + oxt_name)
