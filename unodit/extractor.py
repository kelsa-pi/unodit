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

import logging

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

try:
    # extension
    from unodit import schema

except ImportError:
    # command line
    import pythonpath.schema as schema

ns_tag = "{http://openoffice.org/2000/dialog}"
escape_components = [
    "bulletinboard",
    "styles",
    "style",
    "menupopup",
    "menuitem",
    "radiogroup",
    "event",
    "title",
]


class ContextGenerator:
    """
    Parse xdl file

    Parse xdl file and generate xdl context dictionary (get_xdl_context()).
    Translate xdl context dictionary in uno context dictionary (get_uno_context()) using schema.

    :param xdl_file: full path to ui file
    :type xdl_file: object

    :Example:

    ctx = ContextGenerator(xdlfile)

    xdl_context = ctx.get_xdl_context()
    print(xdl_context)

    uno_ctx = ctx.get_uno_context()
    print(uno_ctx)
    """

    def __init__(self, xdl_file):
        self.xdlfile = xdl_file
        self.tree = self.get_tree(self.xdlfile)
        self.ns = ns_tag
        self.logger = logging.getLogger("unodit.extractor.ContextGenerator")
        self.logger.info("NEW LOGGER: unodit.extractor.ContextGenerator")
        self.logger.info(self.xdlfile)

    def get_tree(self, ui_xdl_file):
        """
        Parse xml tree

        :param ui_xdl_file: full path to ui file
        :type ui_xdl_file: str
        :return: ElementTree
        :rtype: object
        """
        with open(ui_xdl_file, "rt") as f:
            xml_tree = ET.parse(f)
        return xml_tree

    def get_namespaces(self, ui_xdl_file):
        """
        Extract namespaces from xdl file

        :param ui_xdl_file: Full path to ui file
        :type ui_xdl_file: str
        :return: namespaces list
        :rtype: list

        :Example:

        ctx = ContextGenerator(xdlfile)
        my_namespaces = ctx.get_namespaces(xdlfile)
        print(my_namespaces)

        ['window', 'button', 'img', 'checkbox', 'radio', 'text', 'textfield', 'menulist',
         'combobox', 'fixedline', 'datefield', 'timefield', 'numericfield', 'currencyfield',
         'formattedfield', 'patternfield', 'filecontrol', 'spinbutton', 'progressmeter',
         'treecontrol', 'titledbox']
        """
        namespaces = []
        tree = self.get_tree(ui_xdl_file)
        for node in tree.iter():
            component = node.tag.split("}")
            current_component = component[1]
            if current_component not in escape_components:
                if current_component not in namespaces:
                    namespaces.append(current_component)
        self.logger.info(str(namespaces))
        return namespaces

    def get_xdl_context(self):
        """

        :return: dialog and control propeties
        :rtype: dict

        :Example:

        ctx = ContextGenerator(xdlfile)
        xdl_context = ctx.get_xdl_context()
        print(xdl_context)

        {'Default': {'top': '60', 'model': 'window', 'id': 'Default', 'closeable': 'true', 'left': '60', 'height': '220', 'width': '300', 'moveable': 'true'},
         'Label11': {'model': 'text', 'value': 'FileControl', 'left': '235', 'top': '6', 'id': 'Label11', 'height': '10', 'width': '60', 'tab-index': '32'}}
        """
        namespaces = self.get_namespaces(self.xdlfile)
        nsmap = {
            "dlg": "http://openoffice.org/2000/dialog",
            "script": "http://openoffice.org/2000/script",
        }
        context = {}
        z = context.copy()
        for namespace in namespaces:
            if namespace == "window":
                window_element = self.iter_element(self.tree, namespace)
                z.update(window_element)
            else:
                new_element = self.iterfind_element(self.tree, namespace, nsmap)
                z.update(new_element)

        context.update(z)
        new_context = self.remove_namespaces(context)
        self.logger.info(str(new_context))
        return new_context

    def iter_element(self, tree, namespace):

        """ Parse only dialog element"""

        context = {}
        # component_properties = {}
        component_ns = "{http://openoffice.org/2000/dialog}" + namespace
        component_name = ""
        for node in tree.iter():
            if node.tag == component_ns:
                component_properties = {
                    "{http://openoffice.org/2000/dialog}model": namespace
                }
                for name, value in node.attrib.items():
                    component_properties[name] = value
                    if name == "{http://openoffice.org/2000/dialog}id":
                        component_name = value

                context[component_name] = component_properties
        return context

    def iterfind_element(self, tree, namespace, nsmap):

        """
        Parse controls in dialog

        :param tree:
        :param namespace:
        :param nsmap:
        :type tree: object
        :type namespace: str
        :type nsmap: dict
        :return:
        :rtype: dict
        """
        ns = ".//dlg:" + namespace
        current_component = namespace
        new_element = {}
        box_values = []
        for one in tree.iterfind(ns, namespaces=nsmap):
            # level_one = {}
            current_component_name = one.get(
                "{http://openoffice.org/2000/dialog}id"
            )
            level_one = one.attrib
            z = level_one.copy()

            # level_two = {}
            for two in one:
                level_two = two.attrib
                if level_two:
                    z.update(level_two)

                level_three = {}
                for three in two:

                    if (
                        current_component == "menulist"
                        or current_component == "combobox"
                    ):
                        val = three.attrib[
                            "{http://openoffice.org/2000/dialog}value"
                        ]
                        box_values.append(val)
                    else:
                        level_three = three.attrib

                if level_three:
                    z.update(level_three)
                elif len(box_values) > 0:
                    z["{http://openoffice.org/2000/dialog}value"] = box_values

            new_element[current_component_name] = z
            new_element[current_component_name][
                "{http://openoffice.org/2000/dialog}model"
            ] = namespace
        return new_element

    def remove_namespaces(self, contextdict):
        """
        Remove {http://openoffice.org/2000/dialog} from context dict

        :param contextdict:
        :type contextdict: dict
        """
        new_context = {}
        for elem, v_dct in contextdict.items():
            new_context[elem] = {}
            for k, v in v_dct.items():
                new_k = k.split("}")
                new_k = new_k[1]
                new_context[elem][new_k] = v
        return new_context

    def get_diff(self, xdl_ctx):
        """
        Diff xdl vs. schema.py

        :param xdl_ctx:
        :return: dialog and control propeties
        :rtype: dict

        :Example:

        ctx = ContextGenerator(xdlfile, )
        xdl_context = ctx.get_xdl_context()

        diff_context = ctx.get_get_diff(xdl_context)
        print(diff_context)

        button / CommandButton1  :  'value': {'name': '', 'type': ''},
        checkbox / CheckBox1     :  'value': {'name': '', 'type': ''},

        """

        all_maping = "DIFF " + self.xdlfile + " vs. schema.py: "
        maping = ""

        for component, values in xdl_ctx.items():
            current_xdl_component = xdl_ctx[component]["model"]
            current_xdl_component_name = xdl_ctx[component]["id"]
            current_uno_component = schema.properties.get(current_xdl_component)

            for xdl_prop, xdl_value in values.items():
                if xdl_prop not in current_uno_component:
                    if xdl_prop != "model":
                        s = (
                            current_xdl_component
                            + " / "
                            + current_xdl_component_name
                        )
                        s = s.ljust(25)
                        maping += (
                            s
                            + ":  '"
                            + xdl_prop
                            + "': {'name': '', 'type': ''},\n"
                        )
            all_maping += maping
            maping = ""

        # no diff
        if all_maping == "DIFF " + self.xdlfile + " vs. schema.py: ":
            all_maping = "NO DIFF " + self.xdlfile + " vs. schema.py"

        self.logger.info(all_maping)

        return all_maping

    def get_uno_context(self):
        """
        Get dictionary with properties and values adapted for PyUNO
        :return: dialog and control propeties adapted to uno
        :rtype: dict

        :Example:

        ctx = ContextGenerator(xdlfile, )
        xdl_context = ctx.get_xdl_context()
        uno_ctx = ctx.get_uno_context()
        print(uno_ctx)

        {'Default': {'Name': 'Default', 'PositionX': '60', 'Moveable': 'True', 'Height': 220, 'uno_model': 'Dialog', 'Closeable': 'True', 'model': 'window', 'Width': 300, 'PositionY': '60'},
         'Label11': {'Name': 'Label11', 'TabIndex': 32, 'PositionX': '235', 'Height': 10, 'uno_model': 'FixedText', 'model': 'text', 'Width': 60, 'Label': 'FileControl', 'PositionY': '6'}
         }

        """
        xdl_ctx = self.get_xdl_context()
        context_uno = {}

        for component, values in xdl_ctx.items():
            component_uno_properties = {}
            current_xdl_component = xdl_ctx[component]["model"]
            current_uno_component = schema.properties.get(current_xdl_component)

            for xdl_prop, xdl_value in values.items():

                if xdl_prop == "model":
                    component_uno_properties["model"] = current_xdl_component
                    uno_name = current_uno_component["uno_name"]["name"]
                    component_uno_properties["uno_model"] = uno_name

                elif component == "":
                    pass

                else:
                    try:
                        uno_prop = current_uno_component[xdl_prop]["name"]
                        uno_type = current_uno_component[xdl_prop]["type"]

                        if uno_prop == "" or uno_type == "":
                            pass

                        elif "special" in current_uno_component[xdl_prop]:
                            # uno_special = current_uno_component[xdl_prop]['special']
                            xdl_value = str(
                                current_uno_component[xdl_prop]["special"][
                                    xdl_value
                                ]
                            )

                            component_uno_properties[
                                uno_prop
                            ] = self._value_type(xdl_value, uno_type)
                        else:
                            # print(xdl_value + " " + uno_type + "  " + self._value_type(xdl_value, uno_type))
                            component_uno_properties[
                                uno_prop
                            ] = self._value_type(xdl_value, uno_type)
                    except:
                        pass

            context_uno[component] = component_uno_properties
        self.logger.info(str(context_uno))
        return context_uno

    def _value_type(self, val, u_type):

        if u_type == "string":
            # url
            if val.startswith("file:/"):
                uno_value = ' uno.fileUrlToSystemPath("' + val + '") '
            else:
                uno_value = val

        elif u_type == "integer" or u_type == "short" or u_type == "long":
            uno_value = int(val)
        elif u_type == "double":
            uno_value = int(val)
        elif u_type == "boolean":
            uno_value = val.capitalize()
        elif u_type == "sequence":
            uno_value = tuple(val)
        elif u_type == "date":
            # 20161025
            yr = val[:4]
            mn = val[4:6]
            dy = val[-2:]
            if mn.startswith("0"):
                mn = mn[1]
            if dy.startswith("0"):
                dy = dy[1]
            uno_value = (
                " uno.createUnoStruct("
                + '"com.sun.star.util.Date"'
                + ", Year = "
                + yr
                + ", Month = "
                + mn
                + ", Day = "
                + dy
                + ") "
            )
        elif u_type == "time":
            # 14050300
            hr = val[:2]
            mn = val[2:4]
            sc = val[4:6]
            ms = val[-2:]
            if hr.startswith("0"):
                hr = hr[1]
            if mn.startswith("0"):
                mn = mn[1]
            if sc.startswith("0"):
                sc = sc[1]
            if ms.startswith("0"):
                ms = ms[1]

            uno_value = (
                " uno.createUnoStruct("
                + '"com.sun.star.util.Time"'
                + ", Hours = "
                + hr
                + ", Minutes = "
                + mn
                + ", Seconds = "
                + sc
                + ", NanoSeconds = "
                + ms
                + ", IsUTC = True"
                + ") "
            )

        else:
            uno_value = val

        return uno_value
