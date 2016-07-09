# -*- coding: utf-8 -*-
#!/usr/bin/env python

# =============================================================================
#
# Dialog implementation generated from a XDL file.
#
# Created: Sat Jul  9 15:14:39 2016
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

class Test_embed(unohelper.Base, XActionListener, XJobExecutor):
    """
    Class documentation...
    """
    def __init__(self):
        self.LocalContext = uno.getComponentContext()
        self.ServiceManager = self.LocalContext.ServiceManager
        self.Toolkit = self.ServiceManager.createInstanceWithContext("com.sun.star.awt.ExtToolkit", self.LocalContext)

        # -----------------------------------------------------------
        #               Create dialog and insert controls
        # -----------------------------------------------------------

        # --------------create dialog container and set model and properties
        self.DialogContainer = self.ServiceManager.createInstanceWithContext("com.sun.star.awt.UnoControlDialog", self.LocalContext)
        self.DialogModel = self.ServiceManager.createInstance("com.sun.star.awt.UnoControlDialogModel")
        self.DialogContainer.setModel(self.DialogModel)
        self.DialogModel.Moveable = True
        self.DialogModel.Closeable = True
        self.DialogModel.Name = "Default"
        self.DialogModel.Width = 300
        self.DialogModel.PositionX = "60"
        self.DialogModel.Height = 220
        self.DialogModel.PositionY = "60"


        # --------- create an instance of ComboBox control, set properties ---
        self.ComboBox1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlComboBoxModel")

        self.ComboBox1.TabIndex = 10
        self.ComboBox1.Dropdown = True
        self.ComboBox1.StringItemList = ('one', 'two')
        self.ComboBox1.Name = "ComboBox1"
        self.ComboBox1.Width = 60
        self.ComboBox1.PositionX = "83"
        self.ComboBox1.Height = 20
        self.ComboBox1.PositionY = "143"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("ComboBox1", self.ComboBox1)

        # --------- create an instance of GroupBox control, set properties ---
        self.FrameControl1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlGroupBoxModel")

        self.FrameControl1.TabIndex = 36
        self.FrameControl1.Label = "FrameControl1"
        self.FrameControl1.Name = "FrameControl1"
        self.FrameControl1.Width = 60
        self.FrameControl1.PositionX = "9"
        self.FrameControl1.Height = 65
        self.FrameControl1.PositionY = "147"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("FrameControl1", self.FrameControl1)

        # --------- create an instance of Button control, set properties ---
        self.CommandButton1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CommandButton1.Align = 0
        self.CommandButton1.TabIndex = 0
        self.CommandButton1.Label = "CommandButton1"
        self.CommandButton1.Toggle = 1
        self.CommandButton1.Name = "CommandButton1"
        self.CommandButton1.Width = 60
        self.CommandButton1.PositionX = "9"
        self.CommandButton1.Height = 20
        self.CommandButton1.PositionY = "8"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CommandButton1", self.CommandButton1)

        # add the action listener
        self.DialogContainer.getControl('CommandButton1').addActionListener(self)
        self.DialogContainer.getControl('CommandButton1').setActionCommand('CommandButton1_OnClick')

        # --------- create an instance of FixedText control, set properties ---
        self.Label8 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label8.TabIndex = 29
        self.Label8.Label = "ProgressBar"
        self.Label8.Name = "Label8"
        self.Label8.Width = 60
        self.Label8.PositionX = "83"
        self.Label8.Height = 10
        self.Label8.PositionY = "170"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label8", self.Label8)

        # --------- create an instance of FixedText control, set properties ---
        self.Label4 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label4.TabIndex = 25
        self.Label4.Label = "NumericField"
        self.Label4.Name = "Label4"
        self.Label4.Width = 60
        self.Label4.PositionX = "158"
        self.Label4.Height = 10
        self.Label4.PositionY = "76"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label4", self.Label4)

        # --------- create an instance of FileControl control, set properties ---
        self.FileControl1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFileControlModel")

        self.FileControl1.TabIndex = 18
        self.FileControl1.Name = "FileControl1"
        self.FileControl1.Text = "/home/sasa"
        self.FileControl1.Width = 60
        self.FileControl1.PositionX = "235"
        self.FileControl1.Height = 20
        self.FileControl1.PositionY = "17"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("FileControl1", self.FileControl1)

        # --------- create an instance of FixedText control, set properties ---
        self.Label7 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label7.TabIndex = 28
        self.Label7.Label = "PatternField"
        self.Label7.Name = "Label7"
        self.Label7.Width = 60
        self.Label7.PositionX = "158"
        self.Label7.Height = 10
        self.Label7.PositionY = "185"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label7", self.Label7)

        # --------- create an instance of FixedText control, set properties ---
        self.Label5 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label5.TabIndex = 26
        self.Label5.Label = "CurrencyField"
        self.Label5.Name = "Label5"
        self.Label5.Width = 60
        self.Label5.PositionX = "158"
        self.Label5.Height = 10
        self.Label5.PositionY = "114"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label5", self.Label5)

        # --------- create an instance of Button control, set properties ---
        self.CommandButton2 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CommandButton2.TabIndex = 1
        self.CommandButton2.Label = "CommandButton2"
        self.CommandButton2.Enabled = True
        self.CommandButton2.Name = "CommandButton2"
        self.CommandButton2.Width = 29
        self.CommandButton2.PositionY = "33"
        self.CommandButton2.Height = 20
        self.CommandButton2.PositionX = "9"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CommandButton2", self.CommandButton2)

        # add the action listener
        self.DialogContainer.getControl('CommandButton2').addActionListener(self)
        self.DialogContainer.getControl('CommandButton2').setActionCommand('CommandButton2_OnClick')

        # --------- create an instance of SpinButton control, set properties ---
        self.SpinButton1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlSpinButtonModel")

        self.SpinButton1.TabIndex = 22
        self.SpinButton1.Name = "SpinButton1"
        self.SpinButton1.Width = 60
        self.SpinButton1.PositionX = "235"
        self.SpinButton1.Height = 20
        self.SpinButton1.PositionY = "167"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("SpinButton1", self.SpinButton1)

        # --------- create an instance of FixedText control, set properties ---
        self.Label13 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label13.TabIndex = 34
        self.Label13.Label = "SpinButton"
        self.Label13.Name = "Label13"
        self.Label13.Width = 60
        self.Label13.PositionX = "235"
        self.Label13.Height = 10
        self.Label13.PositionY = "156"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label13", self.Label13)

        # --------- create an instance of NumericField control, set properties ---
        self.NumericField1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlNumericFieldModel")

        self.NumericField1.TabIndex = 14
        self.NumericField1.Value = 55555
        self.NumericField1.Name = "NumericField1"
        self.NumericField1.Width = 60
        self.NumericField1.PositionX = "158"
        self.NumericField1.Height = 20
        self.NumericField1.PositionY = "87"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("NumericField1", self.NumericField1)

        # --------- create an instance of TimeField control, set properties ---
        self.TimeField1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlTimeFieldModel")

        self.TimeField1.TabIndex = 13
        self.TimeField1.TimeMin = uno.createUnoStruct("com.sun.star.util.Time", Hours = 10, Minutes = 0, Seconds = 0, NanoSeconds = 0, IsUTC = True)
        self.TimeField1.Name = "TimeField1"
        self.TimeField1.Width = 60
        self.TimeField1.PositionX = "160"
        self.TimeField1.Text = "Set Time"
        self.TimeField1.Time = uno.createUnoStruct("com.sun.star.util.Time", Hours = 14, Minutes = 5, Seconds = 3, NanoSeconds = 0, IsUTC = True)
        self.TimeField1.PositionY = "52"
        self.TimeField1.Height = 20
        self.TimeField1.TimeMax = uno.createUnoStruct("com.sun.star.util.Time", Hours = 22, Minutes = 59, Seconds = 0, NanoSeconds = 0, IsUTC = True)

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("TimeField1", self.TimeField1)

        # --------- create an instance of FixedText control, set properties ---
        self.Label1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label1.TabIndex = 7
        self.Label1.Label = "New"
        self.Label1.Name = "Label1"
        self.Label1.Width = 20
        self.Label1.PositionX = "83"
        self.Label1.Height = 20
        self.Label1.PositionY = "8"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label1", self.Label1)

        # --------- create an instance of FixedText control, set properties ---
        self.Label12 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label12.TabIndex = 33
        self.Label12.Label = "TreeControl"
        self.Label12.Name = "Label12"
        self.Label12.Width = 60
        self.Label12.PositionX = "235"
        self.Label12.Height = 10
        self.Label12.PositionY = "41"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label12", self.Label12)

        # --------- create an instance of FixedText control, set properties ---
        self.Label3 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label3.TabIndex = 24
        self.Label3.Label = "TimeField"
        self.Label3.Name = "Label3"
        self.Label3.Width = 60
        self.Label3.PositionX = "158"
        self.Label3.Height = 10
        self.Label3.PositionY = "42"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label3", self.Label3)

        # --------- create an instance of .tree.TreeControl control, set properties ---
        self.TreeControl1 = self.DialogModel.createInstance("com.sun.star.awt.tree.TreeControlModel")

        self.TreeControl1.TabIndex = 35
        self.TreeControl1.Name = "TreeControl1"
        self.TreeControl1.Width = 59
        self.TreeControl1.PositionX = "235"
        self.TreeControl1.Height = 100
        self.TreeControl1.PositionY = "53"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("TreeControl1", self.TreeControl1)

        # --------- create an instance of ImageControl control, set properties ---
        self.ImageControl1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlImageControlModel")

        self.ImageControl1.TabIndex = 3
        self.ImageControl1.ImageURL = uno.fileUrlToSystemPath("file:///home/sasa/Pictures/coquette-icons-set/png/32x32/add_home.png")
        self.ImageControl1.Name = "ImageControl1"
        self.ImageControl1.Width = 60
        self.ImageControl1.PositionX = "9"
        self.ImageControl1.Height = 60
        self.ImageControl1.PositionY = "56"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("ImageControl1", self.ImageControl1)

        # --------- create an instance of FixedText control, set properties ---
        self.Label6 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label6.TabIndex = 27
        self.Label6.Label = "FormattedField"
        self.Label6.Name = "Label6"
        self.Label6.Width = 60
        self.Label6.PositionX = "158"
        self.Label6.Height = 10
        self.Label6.PositionY = "150"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label6", self.Label6)

        # --------- create an instance of DateField control, set properties ---
        self.DateField1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlDateFieldModel")

        self.DateField1.TabIndex = 12
        self.DateField1.RepeatDelay = 50
        self.DateField1.Date = uno.createUnoStruct("com.sun.star.util.Date", Year = 2015, Month = 3, Day = 26)
        self.DateField1.Name = "DateField1"
        self.DateField1.Width = 60
        self.DateField1.PositionX = "158"
        self.DateField1.DateFormat = 9
        self.DateField1.Dropdown = True
        self.DateField1.DateMax = uno.createUnoStruct("com.sun.star.util.Date", Year = 2020, Month = 1, Day = 1)
        self.DateField1.Text = "Set Date"
        self.DateField1.DateMin = uno.createUnoStruct("com.sun.star.util.Date", Year = 1820, Month = 1, Day = 1)
        self.DateField1.PositionY = "17"
        self.DateField1.Height = 20

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("DateField1", self.DateField1)

        # --------- create an instance of Button control, set properties ---
        self.CommandButton3 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CommandButton3.TabIndex = 2
        self.CommandButton3.Label = "CommandButton3"
        self.CommandButton3.Name = "CommandButton3"
        self.CommandButton3.EnableVisible = False
        self.CommandButton3.Width = 26
        self.CommandButton3.PositionX = "43"
        self.CommandButton3.Height = 20
        self.CommandButton3.PositionY = "33"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CommandButton3", self.CommandButton3)

        # add the action listener
        self.DialogContainer.getControl('CommandButton3').addActionListener(self)
        self.DialogContainer.getControl('CommandButton3').setActionCommand('CommandButton3_OnClick')

        # --------- create an instance of RadioButton control, set properties ---
        self.OptionButton2 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.OptionButton2.TabIndex = 6
        self.OptionButton2.Label = "OptionButton2"
        self.OptionButton2.Name = "OptionButton2"
        self.OptionButton2.Width = 50
        self.OptionButton2.PositionX = "14"
        self.OptionButton2.Height = 20
        self.OptionButton2.PositionY = "187"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("OptionButton2", self.OptionButton2)

        # --------- create an instance of FixedLine control, set properties ---
        self.FixedLine1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedLineModel")

        self.FixedLine1.TabIndex = 19
        self.FixedLine1.Orientation = 1
        self.FixedLine1.Name = "FixedLine1"
        self.FixedLine1.Width = 4
        self.FixedLine1.PositionX = "75"
        self.FixedLine1.Height = 210
        self.FixedLine1.PositionY = "5"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("FixedLine1", self.FixedLine1)

        # --------- create an instance of CheckBox control, set properties ---
        self.CheckBox1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlCheckBoxModel")

        self.CheckBox1.TabIndex = 4
        self.CheckBox1.Label = "CheckBox1"
        self.CheckBox1.PositionY = "121"
        self.CheckBox1.Name = "CheckBox1"
        self.CheckBox1.Width = 60
        self.CheckBox1.State = True
        self.CheckBox1.PositionX = "9"
        self.CheckBox1.Height = 20
        self.CheckBox1.TriState = True

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CheckBox1", self.CheckBox1)

        # --------- create an instance of ListBox control, set properties ---
        self.ListBox1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlListBoxModel")

        self.ListBox1.MultiSelection = True
        self.ListBox1.TabIndex = 9
        self.ListBox1.Align = 1
        self.ListBox1.StringItemList = ('one', 'two')
        self.ListBox1.Name = "ListBox1"
        self.ListBox1.Width = 60
        self.ListBox1.PositionX = "83"
        self.ListBox1.Height = 82
        self.ListBox1.PositionY = "45"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("ListBox1", self.ListBox1)

        # --------- create an instance of FixedLine control, set properties ---
        self.FixedLine3 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedLineModel")

        self.FixedLine3.TabIndex = 21
        self.FixedLine3.Orientation = 1
        self.FixedLine3.Name = "FixedLine3"
        self.FixedLine3.Width = 4
        self.FixedLine3.PositionX = "225"
        self.FixedLine3.Height = 210
        self.FixedLine3.PositionY = "5"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("FixedLine3", self.FixedLine3)

        # --------- create an instance of CurrencyField control, set properties ---
        self.CurrencyField1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlCurrencyFieldModel")

        self.CurrencyField1.TabIndex = 15
        self.CurrencyField1.Value = 5555
        self.CurrencyField1.PositionY = "124"
        self.CurrencyField1.Name = "CurrencyField1"
        self.CurrencyField1.Width = 60
        self.CurrencyField1.PositionX = "158"
        self.CurrencyField1.Height = 20
        self.CurrencyField1.ShowThousandsSeparator = True

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CurrencyField1", self.CurrencyField1)

        # --------- create an instance of ProgressBar control, set properties ---
        self.ProgressBar1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlProgressBarModel")

        self.ProgressBar1.ProgressValue = 50
        self.ProgressBar1.TabIndex = 11
        self.ProgressBar1.Name = "ProgressBar1"
        self.ProgressBar1.Width = 60
        self.ProgressBar1.PositionX = "85"
        self.ProgressBar1.Height = 20
        self.ProgressBar1.PositionY = "184"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("ProgressBar1", self.ProgressBar1)

        # --------- create an instance of RadioButton control, set properties ---
        self.OptionButton1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.OptionButton1.TabIndex = 5
        self.OptionButton1.Label = "OptionButton1"
        self.OptionButton1.Name = "OptionButton1"
        self.OptionButton1.Width = 50
        self.OptionButton1.State = True
        self.OptionButton1.PositionX = "14"
        self.OptionButton1.Height = 20
        self.OptionButton1.PositionY = "162"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("OptionButton1", self.OptionButton1)

        # --------- create an instance of FormattedField control, set properties ---
        self.FormattedField1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFormattedFieldModel")

        self.FormattedField1.EffectiveMax = 5000
        self.FormattedField1.TabIndex = 16
        self.FormattedField1.EffectiveMin = 1000
        self.FormattedField1.Name = "FormattedField1"
        self.FormattedField1.Width = 60
        self.FormattedField1.PositionX = "158"
        self.FormattedField1.EffectiveValue = 2000
        self.FormattedField1.Text = "2,000"
        self.FormattedField1.PositionY = "160"
        self.FormattedField1.Height = 20

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("FormattedField1", self.FormattedField1)

        # --------- create an instance of FixedLine control, set properties ---
        self.FixedLine2 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedLineModel")

        self.FixedLine2.TabIndex = 20
        self.FixedLine2.Orientation = 1
        self.FixedLine2.Name = "FixedLine2"
        self.FixedLine2.Width = 4
        self.FixedLine2.PositionX = "150"
        self.FixedLine2.Height = 210
        self.FixedLine2.PositionY = "5"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("FixedLine2", self.FixedLine2)

        # --------- create an instance of FixedText control, set properties ---
        self.Label2 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label2.TabIndex = 23
        self.Label2.Label = "DateField"
        self.Label2.Name = "Label2"
        self.Label2.Width = 60
        self.Label2.PositionX = "158"
        self.Label2.Height = 10
        self.Label2.PositionY = "6"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label2", self.Label2)

        # --------- create an instance of FixedText control, set properties ---
        self.Label9 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label9.TabIndex = 30
        self.Label9.Label = "ListBox"
        self.Label9.Name = "Label9"
        self.Label9.Width = 60
        self.Label9.PositionX = "85"
        self.Label9.Height = 10
        self.Label9.PositionY = "35"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label9", self.Label9)

        # --------- create an instance of FixedText control, set properties ---
        self.Label10 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label10.TabIndex = 31
        self.Label10.Label = "ComboBox"
        self.Label10.Name = "Label10"
        self.Label10.Width = 60
        self.Label10.PositionX = "83"
        self.Label10.Height = 10
        self.Label10.PositionY = "133"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label10", self.Label10)

        # --------- create an instance of Edit control, set properties ---
        self.TextField1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlEditModel")

        self.TextField1.TabIndex = 8
        self.TextField1.Name = "TextField1"
        self.TextField1.Text = "New Text"
        self.TextField1.Width = 40
        self.TextField1.PositionX = "103"
        self.TextField1.Height = 20
        self.TextField1.PositionY = "8"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("TextField1", self.TextField1)

        # --------- create an instance of PatternField control, set properties ---
        self.PatternField1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlPatternFieldModel")

        self.PatternField1.TabIndex = 17
        self.PatternField1.EditMask = "NNLNNLLLLL"
        self.PatternField1.Name = "PatternField1"
        self.PatternField1.Width = 60
        self.PatternField1.LiteralMask = "__.__.2015"
        self.PatternField1.PositionX = "158"
        self.PatternField1.StrictFormat = True
        self.PatternField1.Text = "Pattern Field Text"
        self.PatternField1.PositionY = "194"
        self.PatternField1.Height = 20

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("PatternField1", self.PatternField1)

        # --------- create an instance of FixedText control, set properties ---
        self.Label11 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label11.TabIndex = 32
        self.Label11.Label = "FileControl"
        self.Label11.Name = "Label11"
        self.Label11.Width = 60
        self.Label11.PositionX = "235"
        self.Label11.Height = 10
        self.Label11.PositionY = "6"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label11", self.Label11)


    def showDialog(self):
        self.DialogContainer.setVisible(True)
        self.DialogContainer.createPeer(self.Toolkit, None)
        self.DialogContainer.execute()

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------

    def actionPerformed(self, oActionEvent):

        if oActionEvent.ActionCommand == 'CommandButton1_OnClick':
            self.CommandButton1_OnClick()

        if oActionEvent.ActionCommand == 'CommandButton2_OnClick':
            self.CommandButton2_OnClick()

        if oActionEvent.ActionCommand == 'CommandButton3_OnClick':
            self.CommandButton3_OnClick()



    def CommandButton1_OnClick(self):
        self.DialogModel.Title = "It's Alive! - CommandButton1"
        self.messageBox("It's Alive! - CommandButton1", "Event: OnClick", INFOBOX)
        # TODO: not implemented

    def CommandButton2_OnClick(self):
        self.DialogModel.Title = "It's Alive! - CommandButton2"
        self.messageBox("It's Alive! - CommandButton2", "Event: OnClick", INFOBOX)
        # TODO: not implemented

    def CommandButton3_OnClick(self):
        self.DialogModel.Title = "It's Alive! - CommandButton3"
        self.messageBox("It's Alive! - CommandButton3", "Event: OnClick", INFOBOX)
        # TODO: not implemented


def Run_Test_embed(*args):
    app = Test_embed()
    app.showDialog()

g_exportedScripts = Run_Test_embed,
