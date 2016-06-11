import os
import shutil
import unittest
import pythonpath.extractor as extractor
import pythonpath.generator as generator
import pythonpath.script_oxt_creator as script


class TestDialog(unittest.TestCase):
    def test_get_xdl_context(self):
        test_dialog = '/home/sasa/WorkDir/project/LibreOffice/xdl2py/test/Default.xdl'
        ctx_generator = extractor.ContextGenerator(test_dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {
            'ComboBox1': {'spin': 'true', 'left': '83', 'tab-index': '10', 'id': 'ComboBox1', 'height': '20',
                          'top': '143', 'width': '60', 'value': ['one', 'two'], 'model': 'combobox'},
            'CurrencyField1': {'left': '158', 'tab-index': '15', 'thousands-separator': 'true', 'id': 'CurrencyField1',
                               'height': '20', 'top': '124', 'width': '60', 'value': '5555', 'model': 'currencyfield'},
            'TextField1': {'left': '103', 'tab-index': '8', 'id': 'TextField1', 'height': '20', 'top': '8',
                           'width': '40', 'value': 'New Text', 'model': 'textfield'},
            'ListBox1': {'multiselection': 'true', 'left': '83', 'align': 'center', 'tab-index': '9', 'id': 'ListBox1',
                         'height': '82', 'top': '45', 'width': '60', 'value': ['one', 'two'], 'model': 'menulist'},
            'OptionButton1': {'left': '14', 'tab-index': '5', 'group-name': 'Group1', 'top': '162',
                              'id': 'OptionButton1', 'height': '20', 'checked': 'true', 'width': '50',
                              'value': 'OptionButton1', 'model': 'radio'},
            'Label3': {'left': '158', 'tab-index': '24', 'id': 'Label3', 'height': '10', 'top': '42', 'width': '60',
                       'value': 'TimeField', 'model': 'text'},
            'FrameControl1': {'left': '9', 'tab-index': '36', 'id': 'FrameControl1', 'height': '65', 'top': '147',
                              'width': '60', 'value': 'FrameControl1', 'model': 'titledbox'},
            'Label12': {'left': '235', 'tab-index': '33', 'id': 'Label12', 'height': '10', 'top': '41', 'width': '60',
                        'value': 'TreeControl', 'model': 'text'},
            'Default': {'left': '60', 'width': '300', 'moveable': 'true', 'id': 'Default', 'height': '220', 'top': '60',
                        'closeable': 'true', 'model': 'window'},
            'DateField1': {'date-format': 'short_YYYYMMDD', 'left': '158', 'tab-index': '12', 'text': 'Set Date',
                           'dropdown': 'true', 'width': '60', 'value-min': '18200101', 'value-max': '20200101',
                           'repeat': '50', 'id': 'DateField1', 'height': '20', 'top': '17', 'value': '20150326',
                           'model': 'datefield'}, 'ImageControl1': {'left': '9', 'tab-index': '3',
                                                                    'src': 'file:///home/sasa/Pictures/coquette-icons-set/png/32x32/add_home.png',
                                                                    'id': 'ImageControl1', 'height': '60', 'top': '56',
                                                                    'width': '60', 'model': 'img'},
            'CommandButton1': {'toggled': '1', 'left': '9', 'align': 'left', 'tab-index': '0', 'id': 'CommandButton1',
                               'height': '20', 'top': '8', 'width': '60', 'value': 'CommandButton1', 'model': 'button'},
            'Label1': {'left': '83', 'tab-index': '7', 'id': 'Label1', 'height': '20', 'top': '8', 'width': '20',
                       'value': 'New', 'model': 'text'},
            'Label6': {'left': '158', 'tab-index': '27', 'id': 'Label6', 'height': '10', 'top': '150', 'width': '60',
                       'value': 'FormattedField', 'model': 'text'},
            'TreeControl1': {'left': '235', 'tab-index': '35', 'id': 'TreeControl1', 'height': '100', 'top': '53',
                             'width': '59', 'model': 'treecontrol'},
            'FixedLine1': {'left': '75', 'align': 'vertical', 'tab-index': '19', 'id': 'FixedLine1', 'height': '210',
                           'top': '5', 'width': '4', 'model': 'fixedline'},
            'FixedLine2': {'left': '150', 'align': 'vertical', 'tab-index': '20', 'id': 'FixedLine2', 'height': '210',
                           'top': '5', 'width': '4', 'model': 'fixedline'},
            'PatternField1': {'edit-mask': 'NNLNNLLLLL', 'left': '158', 'tab-index': '17', 'width': '60',
                              'value': 'Pattern Field Text', 'id': 'PatternField1', 'height': '20', 'top': '194',
                              'literal-mask': '__.__.2015', 'strict-format': 'true', 'model': 'patternfield'},
            'Label4': {'left': '158', 'tab-index': '25', 'id': 'Label4', 'height': '10', 'top': '76', 'width': '60',
                       'value': 'NumericField', 'model': 'text'},
            'FormattedField1': {'left': '158', 'format-code': '#,##0', 'tab-index': '16', 'format-locale': 'en;US',
                                'width': '60', 'text': '2,000', 'value-min': '1000', 'value-max': '5000',
                                'id': 'FormattedField1', 'height': '20', 'top': '160', 'value': '2000',
                                'model': 'formattedfield'},
            'Label5': {'left': '158', 'tab-index': '26', 'id': 'Label5', 'height': '10', 'top': '114', 'width': '60',
                       'value': 'CurrencyField', 'model': 'text'},
            'FixedLine3': {'left': '225', 'align': 'vertical', 'tab-index': '21', 'id': 'FixedLine3', 'height': '210',
                           'top': '5', 'width': '4', 'model': 'fixedline'},
            'Label2': {'left': '158', 'tab-index': '23', 'id': 'Label2', 'height': '10', 'top': '6', 'width': '60',
                       'value': 'DateField', 'model': 'text'},
            'SpinButton1': {'left': '235', 'tab-index': '22', 'id': 'SpinButton1', 'height': '20', 'top': '167',
                            'width': '60', 'model': 'spinbutton'},
            'TimeField1': {'left': '160', 'tab-index': '13', 'value-max': '22590000', 'value-min': '1000000',
                           'text': 'Set Time', 'id': 'TimeField1', 'height': '20', 'top': '52', 'width': '60',
                           'value': '14050300', 'model': 'timefield'},
            'Label7': {'left': '158', 'tab-index': '28', 'id': 'Label7', 'height': '10', 'top': '185', 'width': '60',
                       'value': 'PatternField', 'model': 'text'},
            'CommandButton3': {'left': '43', 'model': 'button', 'tab-index': '2', 'id': 'CommandButton3',
                               'height': '20', 'top': '33', 'width': '26', 'value': 'CommandButton3',
                               'visible': 'false'},
            'NumericField1': {'left': '158', 'tab-index': '14', 'id': 'NumericField1', 'height': '20', 'top': '87',
                              'width': '60', 'value': '55555', 'model': 'numericfield'},
            'Label10': {'left': '83', 'tab-index': '31', 'id': 'Label10', 'height': '10', 'top': '133', 'width': '60',
                        'value': 'ComboBox', 'model': 'text'},
            'Label8': {'left': '83', 'tab-index': '29', 'id': 'Label8', 'height': '10', 'top': '170', 'width': '60',
                       'value': 'ProgressBar', 'model': 'text'},
            'Label13': {'left': '235', 'tab-index': '34', 'id': 'Label13', 'height': '10', 'top': '156', 'width': '60',
                        'value': 'SpinButton', 'model': 'text'},
            'CommandButton2': {'disabled': 'true', 'left': '9', 'tab-index': '1', 'id': 'CommandButton2',
                               'height': '20', 'top': '33', 'width': '29', 'value': 'CommandButton2',
                               'model': 'button'},
            'FileControl1': {'left': '235', 'tab-index': '18', 'id': 'FileControl1', 'height': '20', 'top': '17',
                             'width': '60', 'value': '/home/sasa', 'model': 'filecontrol'},
            'Label9': {'left': '85', 'tab-index': '30', 'id': 'Label9', 'height': '10', 'top': '35', 'width': '60',
                       'value': 'ListBox', 'model': 'text'},
            'CheckBox1': {'left': '9', 'tab-index': '4', 'width': '60', 'top': '121', 'tristate': 'true',
                          'height': '20', 'checked': 'true', 'id': 'CheckBox1', 'value': 'CheckBox1',
                          'model': 'checkbox'},
            'OptionButton2': {'left': '14', 'tab-index': '6', 'group-name': 'Group1', 'id': 'OptionButton2',
                              'height': '20', 'top': '187', 'width': '50', 'value': 'OptionButton2', 'model': 'radio'},
            'ProgressBar1': {'left': '85', 'tab-index': '11', 'id': 'ProgressBar1', 'height': '20', 'top': '184',
                             'width': '60', 'value': '50', 'model': 'progressmeter'},
            'Label11': {'left': '235', 'tab-index': '32', 'id': 'Label11', 'height': '10', 'top': '6', 'width': '60',
                        'value': 'FileControl', 'model': 'text'}}
        self.assertEqual(result, expected_result)

    def test_get_uno_context(self):
        test_dialog = '/home/sasa/WorkDir/project/LibreOffice/xdl2py/test/Default.xdl'
        ctx_generator = extractor.ContextGenerator(test_dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {
            'Label7': {'uno_model': 'FixedText', 'TabIndex': 28, 'PositionY': '185', 'Label': 'PatternField',
                       'Width': 60, 'Height': 10, 'Name': 'Label7', 'PositionX': '158', 'model': 'text'},
            'SpinButton1': {'uno_model': 'SpinButton', 'TabIndex': 22, 'PositionY': '167', 'Width': 60, 'Height': 20,
                            'Name': 'SpinButton1', 'PositionX': '235', 'model': 'spinbutton'}, 'DateField1': {
                'DateMax': ' uno.createUnoStruct("com.sun.star.util.Date", Year = 2020, Month = 1, Day = 1) ',
                'uno_model': 'DateField', 'DateFormat': 9,
                'DateMin': ' uno.createUnoStruct("com.sun.star.util.Date", Year = 1820, Month = 1, Day = 1) ',
                'Width': 60, 'Dropdown': 'True',
                'Date': ' uno.createUnoStruct("com.sun.star.util.Date", Year = 2015, Month = 3, Day = 26) ',
                'PositionX': '158', 'TabIndex': 12, 'PositionY': '17', 'Text': 'Set Date', 'Height': 20,
                'Name': 'DateField1', 'RepeatDelay': 50, 'model': 'datefield'},
            'CommandButton3': {'uno_model': 'Button', 'TabIndex': 2, 'PositionY': '33', 'Label': 'CommandButton3',
                               'EnableVisible': 'False', 'Width': 26, 'Height': 20, 'Name': 'CommandButton3',
                               'PositionX': '43', 'model': 'button'},
            'Label13': {'uno_model': 'FixedText', 'TabIndex': 34, 'PositionY': '156', 'Label': 'SpinButton',
                        'Width': 60, 'Height': 10, 'Name': 'Label13', 'PositionX': '235', 'model': 'text'},
            'FixedLine1': {'uno_model': 'FixedLine', 'TabIndex': 19, 'PositionY': '5', 'Orientation': 1, 'Width': 4,
                           'Height': 210, 'Name': 'FixedLine1', 'PositionX': '75', 'model': 'fixedline'},
            'Default': {'uno_model': 'Dialog', 'PositionY': '60', 'model': 'window', 'Name': 'Default', 'Width': 300,
                        'Height': 220, 'Closeable': 'True', 'Moveable': 'True', 'PositionX': '60'},
            'FileControl1': {'uno_model': 'FileControl', 'TabIndex': 18, 'PositionY': '17', 'Text': '/home/sasa',
                             'Width': 60, 'Height': 20, 'Name': 'FileControl1', 'PositionX': '235',
                             'model': 'filecontrol'},
            'Label6': {'uno_model': 'FixedText', 'TabIndex': 27, 'PositionY': '150', 'Label': 'FormattedField',
                       'Width': 60, 'Height': 10, 'Name': 'Label6', 'PositionX': '158', 'model': 'text'},
            'Label2': {'uno_model': 'FixedText', 'TabIndex': 23, 'PositionY': '6', 'Label': 'DateField', 'Width': 60,
                       'Height': 10, 'Name': 'Label2', 'PositionX': '158', 'model': 'text'},
            'FormattedField1': {'uno_model': 'FormattedField', 'Height': 20, 'Width': 60, 'PositionX': '158',
                                'EffectiveValue': 2000, 'EffectiveMin': 1000, 'TabIndex': 16, 'Text': '2,000',
                                'EffectiveMax': 5000, 'PositionY': '160', 'Name': 'FormattedField1',
                                'model': 'formattedfield'},
            'ListBox1': {'uno_model': 'ListBox', 'MultiSelection': 'True', 'TabIndex': 9, 'PositionY': '45',
                         'StringItemList': ('one', 'two'), 'Align': 1, 'Width': 60, 'Height': 82, 'Name': 'ListBox1',
                         'PositionX': '83', 'model': 'menulist'},
            'Label4': {'uno_model': 'FixedText', 'TabIndex': 25, 'PositionY': '76', 'Label': 'NumericField',
                       'Width': 60, 'Height': 10, 'Name': 'Label4', 'PositionX': '158', 'model': 'text'},
            'CheckBox1': {'uno_model': 'CheckBox', 'TabIndex': 4, 'PositionY': '121', 'model': 'checkbox',
                          'Label': 'CheckBox1', 'TriState': 'True', 'Width': 60, 'Height': 20, 'Name': 'CheckBox1',
                          'State': 'True', 'PositionX': '9'},
            'OptionButton1': {'uno_model': 'RadioButton', 'TabIndex': 5, 'PositionY': '162', 'model': 'radio',
                              'Label': 'OptionButton1', 'Width': 50, 'Height': 20, 'Name': 'OptionButton1',
                              'State': 'True', 'PositionX': '14'},
            'FixedLine3': {'uno_model': 'FixedLine', 'TabIndex': 21, 'PositionY': '5', 'Orientation': 1, 'Width': 4,
                           'Height': 210, 'Name': 'FixedLine3', 'PositionX': '225', 'model': 'fixedline'},
            'ImageControl1': {'PositionY': '56', 'TabIndex': 3,
                              'ImageURL': ' uno.fileUrlToSystemPath("file:///home/sasa/Pictures/coquette-icons-set/png/32x32/add_home.png") ',
                              'uno_model': 'ImageControl', 'Width': 60, 'Height': 60, 'Name': 'ImageControl1',
                              'PositionX': '9', 'model': 'img'},
            'ProgressBar1': {'uno_model': 'ProgressBar', 'TabIndex': 11, 'PositionY': '184', 'model': 'progressmeter',
                             'Width': 60, 'Height': 20, 'Name': 'ProgressBar1', 'PositionX': '85', 'ProgressValue': 50},
            'FrameControl1': {'uno_model': 'GroupBox', 'TabIndex': 36, 'PositionY': '147', 'Label': 'FrameControl1',
                              'Width': 60, 'Height': 65, 'Name': 'FrameControl1', 'PositionX': '9',
                              'model': 'titledbox'},
            'CommandButton1': {'uno_model': 'Button', 'TabIndex': 0, 'PositionY': '8', 'Label': 'CommandButton1',
                               'Align': 0, 'Toggle': 1, 'Width': 60, 'Height': 20, 'Name': 'CommandButton1',
                               'PositionX': '9', 'model': 'button'},
            'Label8': {'uno_model': 'FixedText', 'TabIndex': 29, 'PositionY': '170', 'Label': 'ProgressBar',
                       'Width': 60, 'Height': 10, 'Name': 'Label8', 'PositionX': '83', 'model': 'text'},
            'CommandButton2': {'Enabled': 'True', 'TabIndex': 1, 'PositionY': '33', 'Label': 'CommandButton2',
                               'uno_model': 'Button', 'Width': 29, 'Height': 20, 'Name': 'CommandButton2',
                               'PositionX': '9', 'model': 'button'},
            'OptionButton2': {'uno_model': 'RadioButton', 'TabIndex': 6, 'PositionY': '187', 'Label': 'OptionButton2',
                              'Width': 50, 'Height': 20, 'Name': 'OptionButton2', 'PositionX': '14', 'model': 'radio'},
            'Label12': {'uno_model': 'FixedText', 'TabIndex': 33, 'PositionY': '41', 'Label': 'TreeControl',
                        'Width': 60, 'Height': 10, 'Name': 'Label12', 'PositionX': '235', 'model': 'text'},
            'FixedLine2': {'uno_model': 'FixedLine', 'TabIndex': 20, 'PositionY': '5', 'Orientation': 1, 'Width': 4,
                           'Height': 210, 'Name': 'FixedLine2', 'PositionX': '150', 'model': 'fixedline'},
            'PatternField1': {'uno_model': 'PatternField', 'EditMask': 'NNLNNLLLLL', 'Width': 60,
                              'StrictFormat': 'True', 'PositionX': '158', 'TabIndex': 17, 'PositionY': '194',
                              'Text': 'Pattern Field Text', 'LiteralMask': '__.__.2015', 'Height': 20,
                              'Name': 'PatternField1', 'model': 'patternfield'},
            'Label3': {'uno_model': 'FixedText', 'TabIndex': 24, 'PositionY': '42', 'Label': 'TimeField', 'Width': 60,
                       'Height': 10, 'Name': 'Label3', 'PositionX': '158', 'model': 'text'},
            'NumericField1': {'PositionY': '87', 'TabIndex': 14, 'Value': 55555, 'uno_model': 'NumericField',
                              'Width': 60, 'Height': 20, 'Name': 'NumericField1', 'PositionX': '158',
                              'model': 'numericfield'},
            'Label5': {'uno_model': 'FixedText', 'TabIndex': 26, 'PositionY': '114', 'Label': 'CurrencyField',
                       'Width': 60, 'Height': 10, 'Name': 'Label5', 'PositionX': '158', 'model': 'text'},
            'Label1': {'uno_model': 'FixedText', 'TabIndex': 7, 'PositionY': '8', 'Label': 'New', 'Width': 20,
                       'Height': 20, 'Name': 'Label1', 'PositionX': '83', 'model': 'text'}, 'TimeField1': {
                'Time': ' uno.createUnoStruct("com.sun.star.util.Time", Hours = 14, Minutes = 5, Seconds = 3, NanoSeconds = 0, IsUTC = True) ',
                'uno_model': 'TimeField', 'Height': 20, 'Width': 60, 'PositionX': '160', 'TabIndex': 13,
                'Text': 'Set Time',
                'TimeMax': ' uno.createUnoStruct("com.sun.star.util.Time", Hours = 22, Minutes = 59, Seconds = 0, NanoSeconds = 0, IsUTC = True) ',
                'PositionY': '52', 'Name': 'TimeField1',
                'TimeMin': ' uno.createUnoStruct("com.sun.star.util.Time", Hours = 10, Minutes = 0, Seconds = 0, NanoSeconds = 0, IsUTC = True) ',
                'model': 'timefield'},
            'TreeControl1': {'uno_model': '.tree.TreeControl', 'TabIndex': 35, 'PositionY': '53', 'Width': 59,
                             'Height': 100, 'Name': 'TreeControl1', 'PositionX': '235', 'model': 'treecontrol'},
            'CurrencyField1': {'PositionY': '124', 'TabIndex': 15, 'ShowThousandsSeparator': 'True', 'Value': 5555,
                               'uno_model': 'CurrencyField', 'Width': 60, 'Height': 20, 'Name': 'CurrencyField1',
                               'PositionX': '158', 'model': 'currencyfield'},
            'Label10': {'uno_model': 'FixedText', 'TabIndex': 31, 'PositionY': '133', 'Label': 'ComboBox', 'Width': 60,
                        'Height': 10, 'Name': 'Label10', 'PositionX': '83', 'model': 'text'},
            'Label11': {'uno_model': 'FixedText', 'TabIndex': 32, 'PositionY': '6', 'Label': 'FileControl', 'Width': 60,
                        'Height': 10, 'Name': 'Label11', 'PositionX': '235', 'model': 'text'},
            'Label9': {'uno_model': 'FixedText', 'TabIndex': 30, 'PositionY': '35', 'Label': 'ListBox', 'Width': 60,
                       'Height': 10, 'Name': 'Label9', 'PositionX': '85', 'model': 'text'},
            'ComboBox1': {'uno_model': 'ComboBox', 'TabIndex': 10, 'PositionY': '143', 'model': 'combobox',
                          'StringItemList': ('one', 'two'), 'Width': 60, 'Height': 20, 'Name': 'ComboBox1',
                          'Dropdown': 'True', 'PositionX': '83'},
            'TextField1': {'uno_model': 'Edit', 'TabIndex': 8, 'PositionY': '8', 'Text': 'New Text', 'Width': 40,
                           'Height': 20, 'Name': 'TextField1', 'PositionX': '103', 'model': 'textfield'}}
        self.assertEqual(result, expected_result)


class TestDialogScript(unittest.TestCase):
    def setUp(self):
        pydir = '/home/sasa/WorkDir/project/LibreOffice/Test_controls'
        if not os.path.exists(pydir):
            os.makedirs(pydir)

    def tearDown(self):
        pydir = '/home/sasa/WorkDir/project/LibreOffice/Test_controls'
        shutil.rmtree(pydir)

    def test_script_convert_src_dir(self):
        test_dialog = '/home/sasa/WorkDir/project/LibreOffice/xdl2py/test/Default.xdl'
        pydir = '/home/sasa/WorkDir/project/LibreOffice/Test_controls'
        app = 'TestApp'
        mode = 'script_convert'
        ctx_generator = extractor.ContextGenerator(test_dialog)
        uno_context = ctx_generator.get_uno_context()
        cg = generator.CodeGenerator(test_dialog, uno_context, pydir, app, mode, indent=4)
        cg.generate_code()
        pydir_src = '/home/sasa/WorkDir/project/LibreOffice/Test_controls/src'
        self.assertTrue(os.path.exists(pydir_src))

    def test_script_convert_src_ui_file(self):
        test_dialog = '/home/sasa/WorkDir/project/LibreOffice/xdl2py/test/Default.xdl'
        pydir = '/home/sasa/WorkDir/project/LibreOffice/Test_controls'
        app = 'TestApp'
        mode = 'script_convert'
        ctx_generator = extractor.ContextGenerator(test_dialog)
        uno_context = ctx_generator.get_uno_context()
        cg = generator.CodeGenerator(test_dialog, uno_context, pydir, app, mode, indent=4)
        cg.generate_code()
        pydir_ui_file = '/home/sasa/WorkDir/project/LibreOffice/Test_controls/src/pythonpath/TestApp_UI.py'
        self.assertTrue(os.path.exists(pydir_ui_file))

    def test_script_convert_src_exe_file(self):
        test_dialog = '/home/sasa/WorkDir/project/LibreOffice/xdl2py/test/Default.xdl'
        pydir = '/home/sasa/WorkDir/project/LibreOffice/Test_controls'
        app = 'TestApp'
        mode = 'script_convert'
        ctx_generator = extractor.ContextGenerator(test_dialog)
        uno_context = ctx_generator.get_uno_context()
        cg = generator.CodeGenerator(test_dialog, uno_context, pydir, app, mode, indent=4)
        cg.generate_code()
        pydir_exe_file = '/home/sasa/WorkDir/project/LibreOffice/Test_controls/src/TestApp.py'
        self.assertTrue(os.path.exists(pydir_exe_file))

    def test_script_files_meta_dir(self):
        test_dialog = '/home/sasa/WorkDir/project/LibreOffice/xdl2py/test/Default.xdl'
        pydir = '/home/sasa/WorkDir/project/LibreOffice/Test_controls'
        app = 'TestApp'
        mode = 'script_files'
        ctx_generator = extractor.ContextGenerator(test_dialog)
        uno_context = ctx_generator.get_uno_context()
        cg = generator.CodeGenerator(test_dialog, uno_context, pydir, app, mode, indent=4)
        cg.generate_code()
        sef = script.ScriptExtensionFiles(pydir, app)
        sef.create()
        test = '/home/sasa/WorkDir/project/LibreOffice/Test_controls/META-INF'
        self.assertTrue(os.path.exists(test))

    def test_script_files_manifest_file(self):
        test_dialog = '/home/sasa/WorkDir/project/LibreOffice/xdl2py/test/Default.xdl'
        pydir = '/home/sasa/WorkDir/project/LibreOffice/Test_controls'
        app = 'TestApp'
        mode = 'script_files'
        ctx_generator = extractor.ContextGenerator(test_dialog)
        uno_context = ctx_generator.get_uno_context()
        cg = generator.CodeGenerator(test_dialog, uno_context, pydir, app, mode, indent=4)
        cg.generate_code()
        sef = script.ScriptExtensionFiles(pydir, app)
        sef.create()
        test = '/home/sasa/WorkDir/project/LibreOffice/Test_controls/META-INF/manifest.xml'
        self.assertTrue(os.path.exists(test))

    def test_script_files_registration_dir(self):
        test_dialog = '/home/sasa/WorkDir/project/LibreOffice/xdl2py/test/Default.xdl'
        pydir = '/home/sasa/WorkDir/project/LibreOffice/Test_controls'
        app = 'TestApp'
        mode = 'script_files'
        ctx_generator = extractor.ContextGenerator(test_dialog)
        uno_context = ctx_generator.get_uno_context()
        cg = generator.CodeGenerator(test_dialog, uno_context, pydir, app, mode, indent=4)
        cg.generate_code()
        sef = script.ScriptExtensionFiles(pydir, app)
        sef.create()
        test = '/home/sasa/WorkDir/project/LibreOffice/Test_controls/registration'
        self.assertTrue(os.path.exists(test))

    def test_script_files_license_file(self):
        test_dialog = '/home/sasa/WorkDir/project/LibreOffice/xdl2py/test/Default.xdl'
        pydir = '/home/sasa/WorkDir/project/LibreOffice/Test_controls'
        app = 'TestApp'
        mode = 'script_files'
        ctx_generator = extractor.ContextGenerator(test_dialog)
        uno_context = ctx_generator.get_uno_context()
        cg = generator.CodeGenerator(test_dialog, uno_context, pydir, app, mode, indent=4)
        cg.generate_code()
        sef = script.ScriptExtensionFiles(pydir, app)
        sef.create()
        test = '/home/sasa/WorkDir/project/LibreOffice/Test_controls/registration/license.txt'
        self.assertTrue(os.path.exists(test))

    def test_script_files_description_dir(self):
        test_dialog = '/home/sasa/WorkDir/project/LibreOffice/xdl2py/test/Default.xdl'
        pydir = '/home/sasa/WorkDir/project/LibreOffice/Test_controls'
        app = 'TestApp'
        mode = 'script_files'
        ctx_generator = extractor.ContextGenerator(test_dialog)
        uno_context = ctx_generator.get_uno_context()
        cg = generator.CodeGenerator(test_dialog, uno_context, pydir, app, mode, indent=4)
        cg.generate_code()
        sef = script.ScriptExtensionFiles(pydir, app)
        sef.create()
        test = '/home/sasa/WorkDir/project/LibreOffice/Test_controls/description'
        self.assertTrue(os.path.exists(test))

    def test_script_files_description_file(self):
        test_dialog = '/home/sasa/WorkDir/project/LibreOffice/xdl2py/test/Default.xdl'
        pydir = '/home/sasa/WorkDir/project/LibreOffice/Test_controls'
        app = 'TestApp'
        mode = 'script_files'
        ctx_generator = extractor.ContextGenerator(test_dialog)
        uno_context = ctx_generator.get_uno_context()
        cg = generator.CodeGenerator(test_dialog, uno_context, pydir, app, mode, indent=4)
        cg.generate_code()
        sef = script.ScriptExtensionFiles(pydir, app)
        sef.create()
        test = '/home/sasa/WorkDir/project/LibreOffice/Test_controls/description/description.txt'
        self.assertTrue(os.path.exists(test))

    def test_script_files_title_file(self):
        test_dialog = '/home/sasa/WorkDir/project/LibreOffice/xdl2py/test/Default.xdl'
        pydir = '/home/sasa/WorkDir/project/LibreOffice/Test_controls'
        app = 'TestApp'
        mode = 'script_files'
        ctx_generator = extractor.ContextGenerator(test_dialog)
        uno_context = ctx_generator.get_uno_context()
        cg = generator.CodeGenerator(test_dialog, uno_context, pydir, app, mode, indent=4)
        cg.generate_code()
        sef = script.ScriptExtensionFiles(pydir, app)
        sef.create()
        test = '/home/sasa/WorkDir/project/LibreOffice/Test_controls/description/title.txt'
        self.assertTrue(os.path.exists(test))

    def test_script_files_addons_xcu_file(self):
        test_dialog = '/home/sasa/WorkDir/project/LibreOffice/xdl2py/test/Default.xdl'
        pydir = '/home/sasa/WorkDir/project/LibreOffice/Test_controls'
        app = 'TestApp'
        mode = 'script_files'
        ctx_generator = extractor.ContextGenerator(test_dialog)
        uno_context = ctx_generator.get_uno_context()
        cg = generator.CodeGenerator(test_dialog, uno_context, pydir, app, mode, indent=4)
        cg.generate_code()
        sef = script.ScriptExtensionFiles(pydir, app)
        sef.create()
        test = '/home/sasa/WorkDir/project/LibreOffice/Test_controls/Addons.xcu'
        self.assertTrue(os.path.exists(test))

    def test_script_files_description_xml_file(self):
        test_dialog = '/home/sasa/WorkDir/project/LibreOffice/xdl2py/test/Default.xdl'
        pydir = '/home/sasa/WorkDir/project/LibreOffice/Test_controls'
        app = 'TestApp'
        mode = 'script_files'
        ctx_generator = extractor.ContextGenerator(test_dialog)
        uno_context = ctx_generator.get_uno_context()
        cg = generator.CodeGenerator(test_dialog, uno_context, pydir, app, mode, indent=4)
        cg.generate_code()
        sef = script.ScriptExtensionFiles(pydir, app)
        sef.create()
        test = '/home/sasa/WorkDir/project/LibreOffice/Test_controls/description.xml'
        self.assertTrue(os.path.exists(test))


def suite():
    dialog_suite = unittest.TestSuite()
    dialog_suite.addTest(unittest.makeSuite(TestDialog))
    dialog_suite.addTest(unittest.makeSuite(TestDialogScript))
    return dialog_suite


def main():
    unittest.main()


if __name__ == '__main__':
    main()
