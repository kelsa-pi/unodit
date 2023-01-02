# -*- coding: utf-8 -*-
#!/usr/bin/env python

# =============================================================================
#
# Simple dialogs
#
# Created: Sat Jul  9 15:16:06 2016
#      by: unodit 0.5
# =============================================================================

import uno
import unohelper
from com.sun.star.awt import XActionListener
from com.sun.star.task import XJobExecutor
from com.sun.star.ui.dialogs.TemplateDescription import FILESAVE_SIMPLE


def xray(myObject):
    try:
        sm = uno.getComponentContext().ServiceManager
        mspf = sm.createInstanceWithContext("com.sun.star.script.provider.MasterScriptProviderFactory", uno.getComponentContext())
        scriptPro = mspf.createScriptProvider("")
        xScript = scriptPro.getScript("vnd.sun.star.script:XrayTool._Main.Xray?language=Basic&location=application")
        xScript.invoke((myObject,), (), ())
        return
    except:
        raise _rtex("Basic library Xray is not installed", uno.getComponentContext())

# -----------------------------------------------------------
#               CLASSES
# -----------------------------------------------------------


class SimpleDialog(unohelper.Base, XActionListener, XJobExecutor):
    """
    Class documentation...
    """
    def __init__(self, nPositionX=None, nPositionY=None, nWidth=None, nHeight=None, sTitle=None):
        self.sTitle = sTitle
        self.LocalContext = uno.getComponentContext()
        self.ServiceManager = self.LocalContext.ServiceManager
        self.Toolkit = self.ServiceManager.createInstanceWithContext("com.sun.star.awt.ExtToolkit", self.LocalContext)

        # --------------create dialog container and set model and properties
        self.DialogContainer = self.ServiceManager.createInstanceWithContext("com.sun.star.awt.UnoControlDialog", self.LocalContext)
        self.DialogModel = self.ServiceManager.createInstance("com.sun.star.awt.UnoControlDialogModel")
        self.DialogContainer.setModel(self.DialogModel)
        self.DialogModel.PositionX = nPositionX
        self.DialogModel.PositionY = nPositionY
        self.DialogModel.Height = nHeight
        self.DialogModel.Width = nWidth
        self.DialogModel.Name = "Default"
        self.DialogModel.Closeable = True
        self.DialogModel.Moveable = True

    def addControl(self, sAwtName, sControlName, dProps):
        oControlModel = self.DialogModel.createInstance("com.sun.star.awt.UnoControl" + sAwtName + "Model")
        while dProps:
            prp = dProps.popitem()
            uno.invoke(oControlModel, "setPropertyValue", (prp[0], prp[1]))
            oControlModel.Name = sControlName
        self.DialogModel.insertByName(sControlName, oControlModel)
        if sAwtName == "Button":
            self.DialogContainer.getControl(sControlName).addActionListener(self)
            self.DialogContainer.getControl(sControlName).setActionCommand(sControlName + '_OnClick')
        return oControlModel

    def showDialog(self):
        self.DialogContainer.setVisible(True)
        self.DialogContainer.createPeer(self.Toolkit, None)
        self.DialogContainer.execute()


class SelectBoxClass(SimpleDialog):

    def __init__(self, message="Select one item", title="SelectBox", choices=['a', 'b', 'c']):
        SimpleDialog.__init__(self, nPositionX=60, nPositionY=60, nWidth=100, nHeight=55, sTitle=None)
        self.DialogModel.Title = title

        dMessage = {"PositionY": 5, "PositionX": 5, "Height": 15, "Width": 90, "Label": message}
        self.lbMessage = self.addControl("FixedText", "lbMessage", dMessage)

        dChoices = {"PositionY": 15, "PositionX": 5, "Height": 15, "Width": 90, "Dropdown": True}
        self.cbChoices = self.addControl("ComboBox", "cbChoices", dChoices)
        self.cbChoices.StringItemList = tuple(choices)

        dOK = {"PositionY": 35, "PositionX": 30, "Height": 15, "Width": 30, "Label": "OK"}
        self.btnOK = self.addControl("Button", "btnOK", dOK)

        dCancel = {"PositionY": 35, "PositionX": 65, "Height": 15, "Width": 30, "Label": "Cancel"}
        self.btnCancel = self.addControl("Button", "btnCancel", dCancel)

        # default_text = self.cbChoices.StringItemList[0]
        # self.cbChoices.Text = default_text

        self.returnValue = None

        self.showDialog()
        # xray(self.DialogContainer)

    def actionPerformed(self, oActionEvent):
        if oActionEvent.ActionCommand == 'btnOK_OnClick':
            self.returnValue = self.cbChoices.Text
            self.DialogContainer.endExecute()

        if oActionEvent.ActionCommand == 'btnCancel_OnClick':
            self.DialogContainer.endExecute()

    def returnValue(self):
        pass


class OptionBoxClass(SimpleDialog):
    def __init__(self, message="Select multiple items", title="OptionBox", choices=['a', 'b', 'c']):
        SimpleDialog.__init__(self, nPositionX=60, nPositionY=60, nWidth=135, nHeight=120, sTitle=None)
        self.DialogModel.Title = title

        dMessage = {"PositionY": 5, "PositionX": 5, "Height": 15, "Width": 110, "Label": message}
        self.lbMessage = self.addControl("FixedText", "lbMessage", dMessage)

        dChoices = {"PositionY": 15, "PositionX": 5, "Height": 80, "Width": 125, "MultiSelection": True}
        self.lbChoices = self.addControl("ListBox", "lbChoices", dChoices)
        self.lbChoices.StringItemList = tuple(choices)

        dSelectAll = {"PositionY": 100, "PositionX": 5, "Height": 15, "Width": 30, "Label": "Select All"}
        self.btnSelectAll = self.addControl("Button", "btnSelectAll", dSelectAll)

        dClearAll = {"PositionY": 100, "PositionX": 35, "Height": 15, "Width": 30, "Label": "Clear All"}
        self.btnClearAll = self.addControl("Button", "btnClearAll", dClearAll)

        dOK = {"PositionY": 100, "PositionX": 70, "Height": 15, "Width": 30, "Label": "OK"}
        self.btnOK = self.addControl("Button", "btnOK", dOK)

        dCancel = {"PositionY": 100, "PositionX": 100, "Height": 15, "Width": 30, "Label": "Cancel"}
        self.btnCancel = self.addControl("Button", "btnCancel", dCancel)

        self.returnValue = ()

        self.showDialog()
        # xray(self.DialogContainer)

    def actionPerformed(self, oActionEvent):
        if oActionEvent.ActionCommand == 'btnOK_OnClick':

            n = len(self.DialogContainer.getControl('lbChoices').getSelectedItems())
            if n == 0:
                self.returnValue = ()
            elif n == 1:
                item = self.DialogContainer.getControl('lbChoices').getSelectedItem()
                self.returnValue = (item,)
            else:
                self.returnValue = self.DialogContainer.getControl('lbChoices').getSelectedItems()

            self.DialogContainer.endExecute()

        if oActionEvent.ActionCommand == 'btnCancel_OnClick':
            self.DialogContainer.endExecute()

        if oActionEvent.ActionCommand == 'btnSelectAll_OnClick':
            for item in self.lbChoices.StringItemList:
                self.DialogContainer.getControl('lbChoices').selectItem(item, True)

        if oActionEvent.ActionCommand == 'btnClearAll_OnClick':
            for item in self.lbChoices.StringItemList:
                self.DialogContainer.getControl('lbChoices').selectItem(item, False)

    def returnValue(self):
        pass


class TextBoxClass(SimpleDialog):

    def __init__(self, message="Enter a text", title="TextBox", text=""):
        SimpleDialog.__init__(self, nPositionX=60, nPositionY=60, nWidth=100, nHeight=55, sTitle=None)
        self.DialogModel.Title = title

        dMessage = {"PositionY": 5, "PositionX": 5, "Height": 15, "Width": 90, "Label": message}
        self.lbMessage = self.addControl("FixedText", "lbMessage", dMessage)

        dText = {"PositionY": 15, "PositionX": 5, "Height": 15, "Width": 90, "Text": text}
        self.txtText = self.addControl("Edit", "txtText", dText)

        dOK = {"PositionY": 35, "PositionX": 30, "Height": 15, "Width": 30, "Label": "OK"}
        self.btnOK = self.addControl("Button", "btnOK", dOK)

        dCancel = {"PositionY": 35, "PositionX": 65, "Height": 15, "Width": 30, "Label": "Cancel"}
        self.btnCancel = self.addControl("Button", "btnCancel", dCancel)

        self.returnValue = None

        self.showDialog()
        # xray(self.nfNumber)

    def actionPerformed(self, oActionEvent):
        if oActionEvent.ActionCommand == 'btnOK_OnClick':
            self.returnValue = self.txtText.Text
            self.DialogContainer.endExecute()

        if oActionEvent.ActionCommand == 'btnCancel_OnClick':
            self.DialogContainer.endExecute()

    def returnValue(self):
        pass


class NumberBoxClass(SimpleDialog):

    def __init__(self, message="Enter a number", title="NumberBox", default_value=0, min_=-10000, max_=10000, decimals=0):
        SimpleDialog.__init__(self, nPositionX=60, nPositionY=60, nWidth=100, nHeight=55, sTitle=None)
        self.DialogModel.Title = title

        self.default_value = default_value
        self.min_ = min_
        self.max_ = max_
        self.decimals = decimals

        dMessage = {"PositionY": 5, "PositionX": 5, "Height": 15, "Width": 90, "Label": message}
        self.lbMessage = self.addControl("FixedText", "lbMessage", dMessage)

        dNumber = {"PositionY": 15, "PositionX": 5, "Height": 15, "Width": 90}
        self.nfNumber = self.addControl("NumericField", "nfNumber", dNumber)
        self.nfNumber.setPropertyValue("DecimalAccuracy", self.decimals)
        self.nfNumber.setPropertyValue("StrictFormat", True)
        self.nfNumber.setPropertyValue("Value", self.default_value)
        self.nfNumber.setPropertyValue("ValueMin", self.min_)
        self.nfNumber.setPropertyValue("ValueMax", self.max_)

        dOK = {"PositionY": 35, "PositionX": 30, "Height": 15, "Width": 30, "Label": "OK"}
        self.btnOK = self.addControl("Button", "btnOK", dOK)

        dCancel = {"PositionY": 35, "PositionX": 65, "Height": 15, "Width": 30, "Label": "Cancel"}
        self.btnCancel = self.addControl("Button", "btnCancel", dCancel)

        self.returnValue = None

        self.showDialog()
        # xray(self.DialogContainer)

    def actionPerformed(self, oActionEvent):
        if oActionEvent.ActionCommand == 'btnOK_OnClick':
            if self.decimals == 0:
                self.returnValue = int(self.nfNumber.Value)
            else:
                self.returnValue = self.nfNumber.Value

            self.DialogContainer.endExecute()

        if oActionEvent.ActionCommand == 'btnCancel_OnClick':
            self.DialogContainer.endExecute()

    def returnValue(self):
        pass


class DateBoxClass(SimpleDialog):

    def __init__(self, message="Choose a date", title='DateBox'):
        """
        the format of the displayed date 9: short YYYYMMDD

        """
        SimpleDialog.__init__(self, nPositionX=60, nPositionY=60, nWidth=100, nHeight=55, sTitle=None)
        self.DialogModel.Title = title

        dMessage = {"PositionY": 5, "PositionX": 5, "Height": 15, "Width": 90, "Label": message}
        self.lbMessage = self.addControl("FixedText", "lbMessage", dMessage)

        dDate = {"PositionY": 15, "PositionX": 5, "Height": 15, "Width": 90, "Dropdown": True,
                 "StrictFormat": True, "DateFormat": 9}
        self.dbDate = self.addControl("DateField", "dbDate", dDate)

        dOK = {"PositionY": 35, "PositionX": 30, "Height": 15, "Width": 30, "Label": "OK"}
        self.btnOK = self.addControl("Button", "btnOK", dOK)

        dCancel = {"PositionY": 35, "PositionX": 65, "Height": 15, "Width": 30, "Label": "Cancel"}
        self.btnCancel = self.addControl("Button", "btnCancel", dCancel)

        self.returnValue = ""

        self.showDialog()
        # xray(self.DialogContainer)

    def actionPerformed(self, oActionEvent):
        if oActionEvent.ActionCommand == 'btnOK_OnClick':
            self.returnValue = self.dbDate.Text
            self.DialogContainer.endExecute()

        if oActionEvent.ActionCommand == 'btnCancel_OnClick':
            self.DialogContainer.endExecute()

    def returnValue(self):
        pass


class MessageBoxClass(SimpleDialog):

    def __init__(self, message="Message", title="MessageBox"):
        SimpleDialog.__init__(self, nPositionX=60, nPositionY=60, nWidth=100, nHeight=55, sTitle=None)
        self.DialogModel.Title = title

        dMessage = {"PositionY": 5, "PositionX": 5, "Height": 30, "Width": 90, "Label": message, "MultiLine": True}
        self.lbMessage = self.addControl("FixedText", "lbMessage", dMessage)

        dOK = {"PositionY": 35, "PositionX": 35, "Height": 15, "Width": 30, "Label": "OK"}
        self.btnOK = self.addControl("Button", "btnOK", dOK)

        self.returnValue = None

        self.showDialog()

    def actionPerformed(self, oActionEvent):
        if oActionEvent.ActionCommand == 'btnOK_OnClick':
            self.DialogContainer.endExecute()

    def returnValue(self):
        pass


class ActionBoxClass(SimpleDialog):

    def __init__(self, message="Message", title="ActionBox"):
        SimpleDialog.__init__(self, nPositionX=60, nPositionY=60, nWidth=100, nHeight=55, sTitle=None)
        self.DialogModel.Title = title

        dMessage = {"PositionY": 15, "PositionX": 5, "Height": 15, "Width": 90, "Label": message, "MultiLine": True}
        self.lbMessage = self.addControl("FixedText", "lbMessage", dMessage)

        dOK = {"PositionY": 35, "PositionX": 5, "Height": 15, "Width": 30, "Label": "OK"}
        self.btnOK = self.addControl("Button", "btnOK", dOK)

        dNO = {"PositionY": 35, "PositionX": 35, "Height": 15, "Width": 30, "Label": "NO"}
        self.btnNO = self.addControl("Button", "btnNO", dNO)

        dCancel = {"PositionY": 35, "PositionX": 65, "Height": 15, "Width": 30, "Label": "Cancel"}
        self.btnCancel = self.addControl("Button", "btnCancel", dCancel)

        self.returnValue = None

        self.showDialog()

    def actionPerformed(self, oActionEvent):
        if oActionEvent.ActionCommand == 'btnOK_OnClick':
            self.returnValue = "OK"
            self.DialogContainer.endExecute()

        if oActionEvent.ActionCommand == 'btnNO_OnClick':
            self.returnValue = "NO"
            self.DialogContainer.endExecute()

        if oActionEvent.ActionCommand == 'btnCancel_OnClick':
            self.returnValue = "Cancel"
            self.DialogContainer.endExecute()

    def returnValue(self):
        pass

# -----------------------------------------------------------
#               FUNCTIONS
# -----------------------------------------------------------


def SelectBox(message="Select one item", title="SelectBox", choices=['a', 'b', 'c']):
    app = SelectBoxClass(message, title, choices)
    return app.returnValue


def OptionBox(message="Select multiple items", title="OptionBox", choices=['a', 'b', 'c']):
    app = OptionBoxClass(message, title, choices)
    return app.returnValue


def TextBox(message="Enter your input", title="TextBox", text=""):
    app = TextBoxClass(message, title, text)
    return app.returnValue


def NumberBox(message="Enter a number", title="NumberBox", default_value=0, min_=-10000, max_=10000, decimals=0):
    app = NumberBoxClass(message, title, default_value, min_, max_, decimals)
    return app.returnValue


def DateBox(message="Choose a date", title='DateBox'):
    app = DateBoxClass(message, title)
    return app.returnValue


def FolderPathBox(title='Get directory path'):
    ctx = uno.getComponentContext()
    smgr = ctx.getServiceManager()
    folder_picker = smgr.createInstanceWithContext("com.sun.star.ui.dialogs.FolderPicker", ctx)
    folder_picker.setTitle(title)
    folder_picker.execute()
    return folder_picker.getDirectory()


def FilePathBox(title='Get file path'):
    ctx = uno.getComponentContext()
    smgr = ctx.getServiceManager()
    open_file_picker = smgr.createInstanceWithContext("com.sun.star.ui.dialogs.FilePicker", ctx)
    open_file_picker.setMultiSelectionMode(False)
    open_file_picker.setTitle(title)
    open_file_picker.appendFilter("All files (*.*)", "*.*")
    open_file_picker.execute()
    return open_file_picker.getSelectedFiles()[0]


def MessageBox(message="Message", title="MessageBox"):
    app = MessageBoxClass(message, title)
    return app.returnValue


def ActionBox(message="Message", title="ActionBox"):
    app = ActionBoxClass(message, title)
    return app.returnValue



