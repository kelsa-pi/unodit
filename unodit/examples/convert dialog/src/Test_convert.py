# -*- coding: utf-8 -*-
#!/usr/bin/env python

import uno
from com.sun.star.awt.MessageBoxButtons import BUTTONS_OK, BUTTONS_OK_CANCEL, BUTTONS_YES_NO, BUTTONS_YES_NO_CANCEL, BUTTONS_RETRY_CANCEL, BUTTONS_ABORT_IGNORE_RETRY
from com.sun.star.awt.MessageBoxButtons import DEFAULT_BUTTON_OK, DEFAULT_BUTTON_CANCEL, DEFAULT_BUTTON_RETRY, DEFAULT_BUTTON_YES, DEFAULT_BUTTON_NO, DEFAULT_BUTTON_IGNORE
from com.sun.star.awt.MessageBoxType import MESSAGEBOX, INFOBOX, WARNINGBOX, ERRORBOX, QUERYBOX

from Test_convert_UI import Test_convert_UI


# ----------------- helper code for API_inspector tool MRI ----------
# def mri(ctx, target):
#     mri = ctx.ServiceManager.createInstanceWithContext("mytools.Mri", ctx)
#     mri.inspect(target)
# -------------------------------------------------------------------


class Test_convert(Test_convert_UI):
    """
    Class documentation...
    """
    def __init__(self):
        Test_convert_UI.__init__(self)

        # --------- my code ---------------------
        self.DialogModel.Title = "Test_convert"
        # mri(self.LocalContext, self.DialogContainer)

    def myFunction(self):
        # TODO: not implemented
        pass

        # --------- helpers ---------------------

    def messageBox(self, MsgText, MsgTitle, MsgType=MESSAGEBOX, MsgButtons=BUTTONS_OK):
        sm = self.LocalContext.ServiceManager
        si = sm.createInstanceWithContext("com.sun.star.awt.Toolkit", self.LocalContext)
        mBox = si.createMessageBox(self.Toolkit, MsgType, MsgButtons, MsgTitle, MsgText)
        mBox.execute()

    # -----------------------------------------------------------
    #               Execute dialog
    # -----------------------------------------------------------

    def showDialog(self):
        self.DialogContainer.setVisible(True)
        self.DialogContainer.createPeer(self.Toolkit, None)
        self.DialogContainer.execute()

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------


    def CommandButton3_OnClick(self):
        self.DialogModel.Title = "It's Alive! - CommandButton3"
        self.messageBox("It's Alive! - CommandButton3", "Event: OnClick", INFOBOX)
        # TODO: not implemented

    def CommandButton1_OnClick(self):
        self.DialogModel.Title = "It's Alive! - CommandButton1"
        self.messageBox("It's Alive! - CommandButton1", "Event: OnClick", INFOBOX)
        # TODO: not implemented

    def CommandButton2_OnClick(self):
        self.DialogModel.Title = "It's Alive! - CommandButton2"
        self.messageBox("It's Alive! - CommandButton2", "Event: OnClick", INFOBOX)
        # TODO: not implemented



def Run_Test_convert(*args):
    app = Test_convert()
    app.showDialog()

g_exportedScripts = Run_Test_convert,
