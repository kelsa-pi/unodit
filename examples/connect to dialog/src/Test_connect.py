# -*- coding: utf-8 -*-
#!/usr/bin/env python

# =============================================================================
#
# Connect Python and XDL file.
#
# Created: Sat Jul  9 15:12:55 2016
#      by: unodit 0.5
#
# WARNING! All changes made in this file will be overwritten
#          if the file is generated again!
#
# =============================================================================

import uno
import unohelper
from com.sun.star.awt import XActionListener
from com.sun.star.task import XJobExecutor

from com.sun.star.awt.MessageBoxButtons import BUTTONS_OK, BUTTONS_OK_CANCEL, BUTTONS_YES_NO, BUTTONS_YES_NO_CANCEL, BUTTONS_RETRY_CANCEL, BUTTONS_ABORT_IGNORE_RETRY
from com.sun.star.awt.MessageBoxButtons import DEFAULT_BUTTON_OK, DEFAULT_BUTTON_CANCEL, DEFAULT_BUTTON_RETRY, DEFAULT_BUTTON_YES, DEFAULT_BUTTON_NO, DEFAULT_BUTTON_IGNORE
from com.sun.star.awt.MessageBoxType import MESSAGEBOX, INFOBOX, WARNINGBOX, ERRORBOX, QUERYBOX


# ----------------- helper code for API_inspector tool MRI ----------
def mri(ctx, target):
    mri = ctx.ServiceManager.createInstanceWithContext("mytools.Mri", ctx)
    mri.inspect(target)
# -------------------------------------------------------------------


class Test_connect_UI(unohelper.Base, XActionListener, XJobExecutor):
    """
    Class documentation...
    """
    def __init__(self):
        self.LocalContext = uno.getComponentContext()
        self.ServiceManager = self.LocalContext.ServiceManager
        self.Toolkit = self.ServiceManager.createInstanceWithContext("com.sun.star.awt.ExtToolkit", self.LocalContext)

        # --------------connect dialog container and set model --

        dlg_path = "vnd.sun.star.script:DialogLib.Default?location=application"
        self.Dialog = self.ServiceManager.createInstanceWithContext("com.sun.star.awt.DialogProvider", self.LocalContext)
        self.DialogContainer = self.Dialog.createDialog(dlg_path)
        self.DialogModel = self.DialogContainer.getModel()

        # ------------- define all controls models --------------

        Label7 = self.DialogModel.getByName("Label7")
        Label9 = self.DialogModel.getByName("Label9")
        ListBox1 = self.DialogModel.getByName("ListBox1")
        TextField1 = self.DialogModel.getByName("TextField1")
        Label8 = self.DialogModel.getByName("Label8")
        CommandButton2 = self.DialogModel.getByName("CommandButton2")
        Label4 = self.DialogModel.getByName("Label4")
        PatternField1 = self.DialogModel.getByName("PatternField1")
        Label1 = self.DialogModel.getByName("Label1")
        FixedLine2 = self.DialogModel.getByName("FixedLine2")
        Label13 = self.DialogModel.getByName("Label13")
        TimeField1 = self.DialogModel.getByName("TimeField1")
        FixedLine1 = self.DialogModel.getByName("FixedLine1")
        CommandButton3 = self.DialogModel.getByName("CommandButton3")
        Label11 = self.DialogModel.getByName("Label11")
        ProgressBar1 = self.DialogModel.getByName("ProgressBar1")
        FrameControl1 = self.DialogModel.getByName("FrameControl1")
        CurrencyField1 = self.DialogModel.getByName("CurrencyField1")
        FixedLine3 = self.DialogModel.getByName("FixedLine3")
        CommandButton1 = self.DialogModel.getByName("CommandButton1")
        Label3 = self.DialogModel.getByName("Label3")
        DateField1 = self.DialogModel.getByName("DateField1")
        Label2 = self.DialogModel.getByName("Label2")
        Label12 = self.DialogModel.getByName("Label12")
        ComboBox1 = self.DialogModel.getByName("ComboBox1")
        Label10 = self.DialogModel.getByName("Label10")
        OptionButton1 = self.DialogModel.getByName("OptionButton1")
        ImageControl1 = self.DialogModel.getByName("ImageControl1")
        FileControl1 = self.DialogModel.getByName("FileControl1")
        OptionButton2 = self.DialogModel.getByName("OptionButton2")
        FormattedField1 = self.DialogModel.getByName("FormattedField1")
        CheckBox1 = self.DialogModel.getByName("CheckBox1")
        Label6 = self.DialogModel.getByName("Label6")
        Label5 = self.DialogModel.getByName("Label5")
        SpinButton1 = self.DialogModel.getByName("SpinButton1")
        NumericField1 = self.DialogModel.getByName("NumericField1")
        TreeControl1 = self.DialogModel.getByName("TreeControl1")

        # ------------- add the action listener to buttons ------

        self.DialogContainer.getControl("CommandButton2").addActionListener(self)
        self.DialogContainer.getControl("CommandButton2").setActionCommand("CommandButton2_OnClick")

        self.DialogContainer.getControl("CommandButton3").addActionListener(self)
        self.DialogContainer.getControl("CommandButton3").setActionCommand("CommandButton3_OnClick")

        self.DialogContainer.getControl("CommandButton1").addActionListener(self)
        self.DialogContainer.getControl("CommandButton1").setActionCommand("CommandButton1_OnClick")


        # --------- my code ---------------------
        self.DialogModel.Title = "Test_connect"
        # mri(self.LocalContext, self.DialogContainer)

    # --------- functions -----------------------

    def myFunction(self):
        # TODO: not implemented
        pass

    # --------- helpers -------------------------

    def messageBox(self, MsgText, MsgTitle, MsgType=MESSAGEBOX, MsgButtons=BUTTONS_OK):
        sm = self.LocalContext.ServiceManager
        si = sm.createInstanceWithContext("com.sun.star.awt.Toolkit", self.LocalContext)
        mBox = si.createMessageBox(self.Toolkit, MsgType, MsgButtons, MsgTitle, MsgText)
        mBox.execute()

    # -----------------------------------------------------------
    #                   Action events
    # -----------------------------------------------------------

    def actionPerformed(self, oActionEvent):

        if oActionEvent.ActionCommand == "CommandButton2_OnClick":
            self.CommandButton2_OnClick()

        if oActionEvent.ActionCommand == "CommandButton3_OnClick":
            self.CommandButton3_OnClick()

        if oActionEvent.ActionCommand == "CommandButton1_OnClick":
            self.CommandButton1_OnClick()



    def CommandButton2_OnClick(self):
        self.DialogContainer.Title = "It's Alive! - CommandButton2"
        self.messageBox("It's Alive! - CommandButton2", "Event: OnClick", INFOBOX)
        # TODO: not implemented

    def CommandButton3_OnClick(self):
        self.DialogContainer.Title = "It's Alive! - CommandButton3"
        self.messageBox("It's Alive! - CommandButton3", "Event: OnClick", INFOBOX)
        # TODO: not implemented

    def CommandButton1_OnClick(self):
        self.DialogContainer.Title = "It's Alive! - CommandButton1"
        self.messageBox("It's Alive! - CommandButton1", "Event: OnClick", INFOBOX)
        # TODO: not implemented


    def showDialog(self):
        self.DialogContainer.execute()


def Run_Test_connect_UI(*args):
    app = Test_connect_UI()
    app.showDialog()

g_exportedScripts = Run_Test_connect_UI,

# ----------------- END GENERATED CODE ----------------------------------------
