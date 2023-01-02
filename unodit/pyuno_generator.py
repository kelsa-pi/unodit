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
Generate PyUNO code
"""

import os
import string
import logging

try:
    import config as conf
except ImportError:
    import pythonpath.config as conf


class PythonGenerator:
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
        self.config = conf.ReadINI(conf.MAIN_DIR, self.pydir)
        self.logger = logging.getLogger(
            "unodit.pyuno_generator.PythonGenerator"
        )
        self.logger.info("NEW LOGGER: unodit.pyuno_generator.PythonGenerator")

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
        if self.mode == "script_convert" or self.mode == "script_all":
            # ui file
            py_tmpl_dir = os.path.join(self.tempates_dir, "convert")
            self.tmpl_main_ui = string.Template(
                self.get_template(py_tmpl_dir, "1_main_ui.txt")
            )
            self.tmpl_dialog_prop = string.Template(
                self.get_template(py_tmpl_dir, "2_dialog_properties.txt")
            )
            self.tmpl_control_model = string.Template(
                self.get_template(py_tmpl_dir, "3_control_model.txt")
            )
            self.tmpl_control_prop = string.Template(
                self.get_template(py_tmpl_dir, "4_control_properties.txt")
            )
            self.tmpl_control_insert = string.Template(
                self.get_template(py_tmpl_dir, "5_control_insert.txt")
            )
            self.tmpl_control_event_on_click = string.Template(
                self.get_template(py_tmpl_dir, "6_control_event_action.txt")
            )
            self.tmpl_event_action = string.Template(
                self.get_template(py_tmpl_dir, "7_event_action.txt")
            )
            # exec file
            self.tmpl_main = string.Template(
                self.get_template(py_tmpl_dir, "10_main.txt")
            )
            self.tmpl_event_callbacks = string.Template(
                self.get_template(py_tmpl_dir, "11_event_callbacks.txt")
            )
            self.logger.info("successfully read all templates for script files")

        elif self.mode == "connect":
            # exec file
            py_tmpl_dir = os.path.join(self.tempates_dir, "connect")
            self.connect_tmpl_main_ui = string.Template(
                self.get_template(py_tmpl_dir, "1_connect_main.txt")
            )
            self.connect_tmpl_all_controls = string.Template(
                self.get_template(py_tmpl_dir, "2_controls.txt")
            )
            self.connect_tmpl_control_event = string.Template(
                self.get_template(py_tmpl_dir, "3_control_event.txt")
            )
            self.connect_tmpl_event_action = string.Template(
                self.get_template(py_tmpl_dir, "4_event_action.txt")
            )
            self.tmpl_event_callbacks = string.Template(
                self.get_template(py_tmpl_dir, "5_event_action_callbaks.txt")
            )
            self.logger.info(
                "successfully read all templates for connect exec file"
            )

        elif self.mode == "embed_convert" or self.mode == "embed_all":
            # exec file
            py_tmpl_dir = os.path.join(self.tempates_dir, "embeded")
            self.tmpl_main_ui = string.Template(
                self.get_template(py_tmpl_dir, "1_main_ui.txt")
            )
            self.tmpl_dialog_prop = string.Template(
                self.get_template(py_tmpl_dir, "2_dialog_properties.txt")
            )
            self.tmpl_control_model = string.Template(
                self.get_template(py_tmpl_dir, "3_control_model.txt")
            )
            self.tmpl_control_prop = string.Template(
                self.get_template(py_tmpl_dir, "4_control_properties.txt")
            )
            self.tmpl_control_insert = string.Template(
                self.get_template(py_tmpl_dir, "5_control_insert.txt")
            )
            self.tmpl_control_event_on_click = string.Template(
                self.get_template(py_tmpl_dir, "6_control_event_action.txt")
            )
            self.tmpl_event_action = string.Template(
                self.get_template(py_tmpl_dir, "7_event_action.txt")
            )
            self.tmpl_event_callbacks = string.Template(
                self.get_template(py_tmpl_dir, "11_event_callbacks.txt")
            )
            self.logger.info(
                "successfully read all templates for embed convert"
            )

        # read all templates
        if self.mode == "sidebar_convert" or self.mode == "sidebar_all":
            # ui file
            py_tmpl_dir = os.path.join(self.tempates_dir, "sidebar_convert")
            self.tmpl_main_ui = string.Template(
                self.get_template(py_tmpl_dir, "1_main_ui.txt")
            )
            self.tmpl_dialog_prop = string.Template(
                self.get_template(py_tmpl_dir, "2_dialog_properties.txt")
            )
            self.tmpl_control_model = string.Template(
                self.get_template(py_tmpl_dir, "3_control_model.txt")
            )
            self.tmpl_control_prop = string.Template(
                self.get_template(py_tmpl_dir, "4_control_properties.txt")
            )
            self.tmpl_control_insert = string.Template(
                self.get_template(py_tmpl_dir, "5_control_insert.txt")
            )
            self.tmpl_control_event_on_click = string.Template(
                self.get_template(py_tmpl_dir, "6_control_event_action.txt")
            )
            self.tmpl_event_action = string.Template(
                self.get_template(py_tmpl_dir, "7_event_action.txt")
            )
            # exec file
            self.tmpl_main = string.Template(
                self.get_template(py_tmpl_dir, "10_main.txt")
            )
            self.tmpl_event_callbacks = string.Template(
                self.get_template(py_tmpl_dir, "11_event_callbacks.txt")
            )
            self.logger.info("successfully read all templates for script files")

    def get_template(self, py_tmpl_dir, template):
        templ = os.path.join(py_tmpl_dir, template)
        with open(templ, "rt") as t:
            tt = t.read()
        return tt

    def generate_py_code(self):

        dialog_properties, control_properties = self._get_dialog_and_controls()

        if self.mode == "script_convert" or self.mode == "script_all":

            ui = {
                "I": self.indent,
                "GENERATED_DATETIME": conf.NOW,
                "UNODIT_VERSION": conf.VERSION,
                "APP_NAME": self.app,
                "GEN_DIALOG_PROPERTIES": self._set_dialog_properties(
                    dialog_properties
                ),
                "GEN_CONTROLS": self._get_controls_properties(
                    control_properties
                ),
                "GEN_ACTIONS_EVENTS": self._get_event_action(
                    control_properties
                ),
                "EXEC_FUNCTION_PREFIX": self.config.get(
                    "exec_function", "prefix"
                ),
            }

            main_ui = self.tmpl_main_ui.substitute(ui)

            lg = {
                "I": self.indent,
                "APP_NAME": self.app,
                "GEN_ACTIONS_CALLBACKS": self._get_event_callbacks(
                    control_properties
                ),
                "EXEC_FUNCTION_PREFIX": self.config.get(
                    "exec_function", "prefix"
                ),
            }
            logic = self.tmpl_main.substitute(lg)

            return main_ui, logic

        elif self.mode == "connect":

            ui_lg = {
                "I": self.indent,
                "GENERATED_DATETIME": conf.NOW,
                "UNODIT_VERSION": conf.VERSION,
                "APP_NAME": self.app,
                "GEN_DIALOG_ADDRESS": self._get_dialog_address(self.xdlfile),
                "GEN_ALL_CONTROLS": self._get_controls_name(control_properties),
                "GEN_ACTIONS_EVENTS": self._get_button_event(
                    control_properties
                ),
                "GEN_ACTIONS": self._get_button_event_action(
                    control_properties
                ),
                "GEN_CALLBAKS": self._get_event_callbacks(control_properties),
                "EXEC_FUNCTION_PREFIX": self.config.get(
                    "exec_function", "prefix"
                ),
            }

            main_ui = self.connect_tmpl_main_ui.substitute(ui_lg)
            return main_ui

        elif self.mode == "embed_convert" or self.mode == "embed_all":

            ui = {
                "I": self.indent,
                "GENERATED_DATETIME": conf.NOW,
                "UNODIT_VERSION": conf.VERSION,
                "APP_NAME": self.app,
                "GEN_DIALOG_PROPERTIES": self._set_dialog_properties(
                    dialog_properties
                ),
                "GEN_CONTROLS": self._get_controls_properties(
                    control_properties
                ),
                "GEN_ACTIONS_EVENTS": self._get_event_action(
                    control_properties
                ),
                "GEN_CALLBAKS": self._get_event_callbacks(control_properties),
                "EXEC_FUNCTION_PREFIX": self.config.get(
                    "exec_function", "prefix"
                ),
            }

            main_ui = self.tmpl_main_ui.substitute(ui)

            return main_ui

        elif self.mode == "sidebar_convert":
            for name, value in self.kwargs.items():
                if name == "panel_name":
                    pn = value
            ui = {
                "I": self.indent,
                "GENERATED_DATETIME": conf.NOW,
                "UNODIT_VERSION": conf.VERSION,
                "APP_NAME": pn,
                "GEN_DIALOG_PROPERTIES": self._set_dialog_properties(
                    dialog_properties
                ),
                "GEN_CONTROLS": self._get_controls_properties(
                    control_properties
                ),
                "GEN_ACTIONS_EVENTS": self._get_event_action(
                    control_properties
                ),
                "EXEC_FUNCTION_PREFIX": self.config.get(
                    "exec_function", "prefix"
                ),
            }

            main_ui = self.tmpl_main_ui.substitute(ui)

            lg = {
                "I": self.indent,
                "UI_DIR": self.config.get("sdb_directories", "sdb_ui"),
                "APP_NAME": pn,
                "GEN_ACTIONS_CALLBACKS": self._get_event_callbacks(
                    control_properties
                ),
                "EXEC_FUNCTION_PREFIX": self.config.get(
                    "exec_function", "prefix"
                ),
            }
            logic = self.tmpl_main.substitute(lg)

            return main_ui, logic

    def _get_button_callbaks(self, cntrl_prop_dict):

        code = ""
        for key, value in cntrl_prop_dict.items():
            control = key
            control_model = cntrl_prop_dict[control]["uno_model"]
            control_name = cntrl_prop_dict[control]["Name"]

            if control_model == "Button":
                d = {"I": self.indent, "CONTROL_NAME": control_name}
                code += self.connect_tmpl_event_action_callbaks.substitute(d)
        return code

    def _get_button_event(self, cntrl_prop_dict):

        code = ""
        for key, value in cntrl_prop_dict.items():
            control = key
            control_model = cntrl_prop_dict[control]["uno_model"]
            control_name = cntrl_prop_dict[control]["Name"]

            if control_model == "Button":
                d = {"I": self.indent, "CONTROL_NAME": control_name}
                code += self.connect_tmpl_control_event.substitute(d)
        return code

    def _get_button_event_action(self, cntrl_prop_dict):

        code = ""
        for key, value in cntrl_prop_dict.items():
            control = key
            control_model = cntrl_prop_dict[control]["uno_model"]
            control_name = cntrl_prop_dict[control]["Name"]

            if control_model == "Button":
                d = {"I": self.indent, "CONTROL_NAME": control_name}
                code += self.connect_tmpl_event_action.substitute(d)
        return code

    def _get_controls_name(self, cntrl_prop_dict):

        code = ""
        for k in cntrl_prop_dict.keys():
            d = {"I": self.indent, "CONTROL_NAME": k}

            code += self.connect_tmpl_all_controls.substitute(d)

        return code

    def _get_dialog_address(self, xdlfile):

        library, dialog = os.path.split(os.path.abspath(xdlfile))
        dlg_lib = library.split(os.sep)[-1]
        dlg_name = dialog.split(".")[0]
        dlg_address = dlg_lib + "." + dlg_name

        return dlg_address

    def _get_dialog_and_controls(self):
        win_prop_dict = {}
        comp_prop_dict = {}
        for key, value in self.context.items():
            cur_comp_model = self.context[key]["model"]

            try:
                if cur_comp_model == "window":

                    win_prop_dict[key] = value
                elif not cur_comp_model == "window":

                    comp_prop_dict[key] = value
            except:
                pass

        return win_prop_dict, comp_prop_dict

    def _set_dialog_properties(self, win_prop_dict):

        code = ""
        for key, value in win_prop_dict.items():
            for k, v in value.items():

                if k == "model" or k == "uno_model":
                    pass
                else:
                    if isinstance(v, str):

                        if v == "True":
                            v = True
                        elif v == "False":
                            v = False
                        else:
                            v = '"' + v + '"'

                    d = {"I": self.indent, "PROPERTIES": k, "VALUE": v}
                    code += self.tmpl_dialog_prop.substitute(d)

        return code

    def _get_controls_properties(self, cntrl_prop_dict):

        code = ""

        for key, value in cntrl_prop_dict.items():
            try:
                control = key
                control_model = cntrl_prop_dict[control]["uno_model"]
                control_name = cntrl_prop_dict[control]["Name"]

                # write control model
                code += self._control_header(control_model, control_name)
                # write control properties
                code += self._control_properties(value, control_name)
                # write insert control in the dialog
                code += self._control_insert(control_name)
                # write control events
                if control_model == "Button":
                    code += self._control_event_onclick(control_name)

            except:
                pass

        return code

    def _control_header(self, control_model, control_name):
        code = ""
        d = {
            "I": self.indent,
            "UNOCONTROL": control_model,
            "CONTROL_NAME": control_name,
        }
        code += self.tmpl_control_model.substitute(d)

        # print(control_model + ' = ' + control_name)

        if control_model == ".tree.TreeControl":
            code = code.replace(".UnoControl", "")

        if control_model == ".grid.Grid":
            code = code.replace(
                "UnoControl.grid.GridModel", "grid.UnoControlGridModel"
            )

        return code

    def _control_properties(self, val_dict, cntrl_name):
        cp = self.tmpl_control_prop
        code = ""
        for k, v in val_dict.items():
            if k == "model" or k == "uno_model":
                pass
            else:
                # print(v)
                if isinstance(v, str):
                    if v == "True":
                        v = True
                    elif v == "False":
                        v = False
                    elif v.startswith(" uno."):
                        v = v[1:-1]
                    else:
                        v = '"' + v + '"'

                d = {
                    "I": self.indent,
                    "CONTROL_NAME": cntrl_name,
                    "PROPERTIES": k,
                    "VALUE": v,
                }
                code += str(cp.substitute(d))
        return code

    def _control_insert(self, cntrl_name):
        code = ""
        d = {"I": self.indent, "CONTROL_NAME": cntrl_name}
        code += str(self.tmpl_control_insert.substitute(d))
        return code

    def _control_event_onclick(self, cntrl_name):
        code = ""
        d = {"I": self.indent, "CONTROL_NAME": cntrl_name}
        code += str(self.tmpl_control_event_on_click.substitute(d))
        return code

    def _get_event_action(self, cntrl_prop_dict):
        cp = self.tmpl_event_action
        code = ""

        for key, value in cntrl_prop_dict.items():
            try:
                control = key
                control_model = cntrl_prop_dict[control]["uno_model"]
                control_name = cntrl_prop_dict[control]["Name"]
                # write control events
                if control_model == "Button":
                    d = {"I": self.indent, "CONTROL_NAME": control_name}
                    code += str(cp.substitute(d))
            except:
                pass

        if code == "":
            code = "pass"

        return code

    def _get_event_callbacks(self, cntrl_prop_dict):
        cp = self.tmpl_event_callbacks
        code = ""

        for key, value in cntrl_prop_dict.items():
            try:
                control = key
                control_model = cntrl_prop_dict[control]["uno_model"]
                control_name = cntrl_prop_dict[control]["Name"]
                # write control events
                if control_model == "Button":
                    d = {"I": self.indent, "CONTROL_NAME": control_name}
                    code += str(cp.substitute(d))
            except:
                pass

        return code
