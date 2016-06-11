import os
import unittest
import pythonpath.extractor as extractor


class ContextGeneratorTests(unittest.TestCase):
    def test_get_namespaces(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'button.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_namespaces(dialog)
        # print(result)
        expected_result = ['window', 'button']
        self.assertEqual(result, expected_result)

    def test_iter_element(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'dialog.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        tree = ctx_generator.get_tree(dialog)
        namespace = 'window'
        result = ctx_generator.iter_element(tree, namespace)
        # print(str(result))
        expected_result = {'dialog': {'{http://openoffice.org/2000/dialog}closeable': 'true',
                                      '{http://openoffice.org/2000/dialog}left': '106',
                                      '{http://openoffice.org/2000/dialog}id': 'dialog',
                                      '{http://openoffice.org/2000/dialog}top': '65',
                                      '{http://openoffice.org/2000/dialog}moveable': 'true',
                                      '{http://openoffice.org/2000/dialog}height': '122',
                                      '{http://openoffice.org/2000/dialog}model': 'window',
                                      '{http://openoffice.org/2000/dialog}width': '136'
                                      }
                           }
        self.assertEqual(result, expected_result)

    def test_iterfind_element(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'button.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        tree = ctx_generator.get_tree(dialog)
        namespace = 'button'
        nsmap = {'dlg': 'http://openoffice.org/2000/dialog',
                 'script': 'http://openoffice.org/2000/script',
                 }
        result = ctx_generator.iterfind_element(tree, namespace, nsmap)
        # print(result)
        expected_result = {'CommandButton1': {'{http://openoffice.org/2000/dialog}tab-index': '0',
                                              '{http://openoffice.org/2000/dialog}model': 'button',
                                              '{http://openoffice.org/2000/dialog}left': '27',
                                              '{http://openoffice.org/2000/dialog}top': '20',
                                              '{http://openoffice.org/2000/dialog}id': 'CommandButton1',
                                              '{http://openoffice.org/2000/dialog}width': '88',
                                              '{http://openoffice.org/2000/dialog}height': '82',
                                              '{http://openoffice.org/2000/dialog}value': 'CommandButton1'}}

        self.assertEqual(result, expected_result)

    def test_remove_namespaces(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'button.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        contextdict = {'CommandButton1': {'{http://openoffice.org/2000/dialog}tab-index': '0',
                                          '{http://openoffice.org/2000/dialog}model': 'button',
                                          '{http://openoffice.org/2000/dialog}left': '27',
                                          '{http://openoffice.org/2000/dialog}top': '20',
                                          '{http://openoffice.org/2000/dialog}id': 'CommandButton1',
                                          '{http://openoffice.org/2000/dialog}width': '88',
                                          '{http://openoffice.org/2000/dialog}height': '82',
                                          '{http://openoffice.org/2000/dialog}value': 'CommandButton1'}}

        result = ctx_generator.remove_namespaces(contextdict)
        # print(result)
        expected_result = {'CommandButton1': {'id': 'CommandButton1',
                                              'height': '82',
                                              'width': '88',
                                              'model': 'button',
                                              'tab-index': '0',
                                              'top': '20',
                                              'left': '27',
                                              'value': 'CommandButton1'
                                              }
                           }
        self.assertEqual(result, expected_result)

    def test_value_type_string(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'button.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        self.assertEqual(ctx_generator._value_type('83', 'string'), '83')
        self.assertEqual(ctx_generator._value_type('New', 'string'), 'New')
        self.assertEqual(ctx_generator._value_type('2,000', 'string'), '2,000')

    def test_value_type_boolean(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'button.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        self.assertEqual(ctx_generator._value_type('true', 'boolean'), 'True')
        self.assertEqual(ctx_generator._value_type('false', 'boolean'), 'False')

    def test_value_type_date(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'button.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        self.assertEqual(ctx_generator._value_type('20200101', 'date'),
                         """ uno.createUnoStruct("com.sun.star.util.Date", Year = 2020, Month = 1, Day = 1) """)
        self.assertEqual(ctx_generator._value_type('20201001', 'date'),
                         """ uno.createUnoStruct("com.sun.star.util.Date", Year = 2020, Month = 10, Day = 1) """)
        self.assertEqual(ctx_generator._value_type('20201010', 'date'),
                         """ uno.createUnoStruct("com.sun.star.util.Date", Year = 2020, Month = 10, Day = 10) """)
        self.assertEqual(ctx_generator._value_type('20201231', 'date'),
                         """ uno.createUnoStruct("com.sun.star.util.Date", Year = 2020, Month = 12, Day = 31) """)

    def test_value_type_time(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'button.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        # print(ctx_generator._value_type('14050300', 'time'))
        self.assertEqual(ctx_generator._value_type('14050300', 'time'),
                         """ uno.createUnoStruct("com.sun.star.util.Time", Hours = 14, Minutes = 5, Seconds = 3, NanoSeconds = 0, IsUTC = True) """)
        self.assertEqual(ctx_generator._value_type('01020304', 'time'),
                         """ uno.createUnoStruct("com.sun.star.util.Time", Hours = 1, Minutes = 2, Seconds = 3, NanoSeconds = 4, IsUTC = True) """)
        self.assertEqual(ctx_generator._value_type('23595959', 'time'),
                         """ uno.createUnoStruct("com.sun.star.util.Time", Hours = 23, Minutes = 59, Seconds = 59, NanoSeconds = 59, IsUTC = True) """)


class ContextGeneratorTestsGetXdlContext(unittest.TestCase):
    def test_extractor_ContextGenerator_dialog(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'dialog.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {'dialog': {'closeable': 'true',
                                      'height': '122',
                                      'id': 'dialog',
                                      'left': '106',
                                      'model': 'window',
                                      'moveable': 'true',
                                      'top': '65',
                                      'width': '136'
                                      }
                           }

        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_button(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'button.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {'CommandButton1': {'model': 'button',
                                              'value': 'CommandButton1',
                                              'width': '88',
                                              'id': 'CommandButton1',
                                              'left': '27',
                                              'top': '20',
                                              'height': '82',
                                              'tab-index': '0'},
                           'button': {'model': 'window',
                                      'closeable': 'true',
                                      'width': '136',
                                      'top': '65',
                                      'id': 'button',
                                      'left': '106',
                                      'moveable': 'true',
                                      'height': '122'}
                           }

        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_check_box(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'check_box.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {'check_box': {'id': 'check_box',
                                         'model': 'window',
                                         'closeable': 'true',
                                         'width': '136',
                                         'height': '122',
                                         'left': '106',
                                         'moveable': 'true',
                                         'top': '65'},
                           'CheckBox1': {'checked': 'false',
                                         'id': 'CheckBox1',
                                         'model': 'checkbox',
                                         'width': '105',
                                         'height': '17',
                                         'top': '23',
                                         'left': '19',
                                         'tab-index': '0',
                                         'value': 'CheckBox1'},
                           }

        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_combo_box(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'combo_box.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {'combo_box': {'model': 'window',
                                         'moveable': 'true',
                                         'top': '65',
                                         'width': '136',
                                         'closeable': 'true',
                                         'height': '122',
                                         'left': '106',
                                         'id': 'combo_box'
                                         },
                           'ComboBox1': {'model': 'combobox',
                                         'top': '20',
                                         'width': '103',
                                         'spin': 'true',
                                         'height': '25',
                                         'left': '20',
                                         'tab-index': '0',
                                         'id': 'ComboBox1'
                                         }
                           }

        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_currency_field(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'currency_field.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {'currency_field': {'top': '65',
                                              'model': 'window',
                                              'width': '136',
                                              'closeable': 'true',
                                              'id': 'currency_field',
                                              'left': '95',
                                              'moveable': 'true',
                                              'height': '122'
                                              },
                           'CurrencyField1': {'top': '28',
                                              'left': '16',
                                              'model': 'currencyfield',
                                              'width': '108',
                                              'id': 'CurrencyField1',
                                              'tab-index': '0',
                                              'height': '20'}
                           }

        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_date_field(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'date_field.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {'DateField1': {'width': '92',
                                          'id': 'DateField1',
                                          'top': '28',
                                          'height': '20',
                                          'model': 'datefield',
                                          'left': '26',
                                          'tab-index': '0'
                                          },
                           'date_field': {'width': '136',
                                          'id': 'date_field',
                                          'moveable': 'true',
                                          'height': '122',
                                          'model': 'window',
                                          'left': '95',
                                          'closeable': 'true',
                                          'top': '65'
                                          }
                           }

        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_file_control(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'file_control.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {'file_control': {'height': '122',
                                            'top': '65',
                                            'moveable': 'true',
                                            'id': 'file_control',
                                            'model': 'window',
                                            'left': '95',
                                            'width': '136',
                                            'closeable': 'true'
                                            },
                           'FileControl1': {'height': '17',
                                            'tab-index': '0',
                                            'top': '18',
                                            'id': 'FileControl1',
                                            'left': '16',
                                            'width': '101',
                                            'model': 'filecontrol'
                                            }
                           }

        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_fixed_line_h(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'fixed_line_h.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {'FixedLine1': {'model': 'fixedline',
                                          'id': 'FixedLine1',
                                          'height': '4',
                                          'width': '111',
                                          'tab-index': '0',
                                          'top': '26',
                                          'left': '16'
                                          },
                           'fixed_line_h': {'left': '95',
                                            'model': 'window',
                                            'moveable': 'true',
                                            'closeable': 'true',
                                            'id': 'fixed_line_h',
                                            'width': '136',
                                            'height': '122',
                                            'top': '65'
                                            }
                           }

        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_fixed_line_v(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'fixed_line_v.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {'FixedLine1': {'model': 'fixedline',
                                          'width': '3',
                                          'height': '89',
                                          'align': 'vertical',
                                          'tab-index': '0',
                                          'top': '23',
                                          'id': 'FixedLine1',
                                          'left': '19'
                                          },
                           'fixed_line_v': {'height': '122',
                                            'id': 'fixed_line_v',
                                            'width': '136',
                                            'model': 'window',
                                            'top': '65',
                                            'moveable': 'true',
                                            'closeable': 'true',
                                            'left': '95'
                                            }
                           }

        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_formmated_field(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'formmated_field.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {'FormattedField1': {'model': 'formattedfield',
                                               'top': '18',
                                               'left': '16',
                                               'height': '22',
                                               'tab-index': '0',
                                               'id': 'FormattedField1',
                                               'width': '108'
                                               },
                           'formmated_field': {'width': '136',
                                               'top': '65',
                                               'moveable': 'true',
                                               'left': '95',
                                               'height': '122',
                                               'id': 'formmated_field',
                                               'model': 'window',
                                               'closeable': 'true'
                                               }
                           }
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_group_box(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'group_box.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {'FrameControl1': {'height': '82',
                                             'model': 'titledbox',
                                             'width': '88',
                                             'left': '28',
                                             'value': 'FrameControl1',
                                             'tab-index': '0',
                                             'top': '14',
                                             'id': 'FrameControl1'
                                             },
                           'group_box': {'height': '122',
                                         'model': 'window',
                                         'width': '136',
                                         'left': '106',
                                         'moveable': 'true',
                                         'top': '65',
                                         'id': 'group_box',
                                         'closeable': 'true'
                                         }
                           }
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_image_control(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'image_control.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {'ImageControl1': {'left': '23',
                                             'id': 'ImageControl1',
                                             'top': '28',
                                             'tab-index': '0',
                                             'height': '69',
                                             'width': '92',
                                             'model': 'img'
                                             },
                           'image_control': {'closeable': 'true',
                                             'left': '95',
                                             'id': 'image_control',
                                             'top': '65',
                                             'moveable': 'true',
                                             'height': '122',
                                             'width': '136',
                                             'model': 'window'
                                             }
                           }
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_label(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'label.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {'label': {'model': 'window',
                                     'top': '65',
                                     'width': '136',
                                     'id': 'label',
                                     'moveable': 'true',
                                     'height': '122',
                                     'left': '106',
                                     'closeable': 'true'
                                     },
                           'Label1': {'model': 'text',
                                      'value': 'Label1',
                                      'width': '99',
                                      'id': 'Label1',
                                      'tab-index': '0',
                                      'top': '26',
                                      'height': '40',
                                      'left': '21'
                                      }
                           }
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_list_box(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'list_box.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {'list_box': {'moveable': 'true',
                                        'height': '122',
                                        'left': '106',
                                        'closeable': 'true',
                                        'top': '65',
                                        'id': 'list_box',
                                        'model': 'window',
                                        'width': '136'
                                        },
                           'ListBox1': {'height': '92',
                                        'tab-index': '0',
                                        'left': '29',
                                        'top': '13',
                                        'id': 'ListBox1',
                                        'model': 'menulist',
                                        'width': '84'
                                        }
                           }
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_numeric_field(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'numeric_field.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {'NumericField1': {'tab-index': '0',
                                             'top': '24',
                                             'width': '101',
                                             'id': 'NumericField1',
                                             'left': '19',
                                             'model': 'numericfield',
                                             'height': '24'
                                             },
                           'numeric_field': {'top': '65',
                                             'width': '136',
                                             'id': 'numeric_field',
                                             'closeable': 'true',
                                             'left': '95',
                                             'model': 'window',
                                             'height': '122',
                                             'moveable': 'true'
                                             }
                           }
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_option_box(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'option_box.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {
            'option_box': {'moveable': 'true', 'closeable': 'true', 'left': '106', 'id': 'option_box', 'top': '65',
                           'model': 'window', 'width': '136', 'height': '122'},
            'OptionButton2': {'left': '27', 'id': 'OptionButton2', 'top': '50', 'tab-index': '1', 'model': 'radio',
                              'value': 'OptionButton2', 'width': '93', 'height': '19'},
            'OptionButton1': {'left': '28', 'id': 'OptionButton1', 'top': '24', 'tab-index': '0', 'model': 'radio',
                              'value': 'OptionButton1', 'width': '92', 'height': '17'}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_pattern_field(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'pattern_field.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {
            'PatternField1': {'height': '19', 'left': '15', 'model': 'patternfield', 'tab-index': '0', 'width': '111',
                              'top': '18', 'id': 'PatternField1'},
            'pattern_field': {'height': '122', 'id': 'pattern_field', 'left': '95', 'model': 'window',
                              'closeable': 'true', 'width': '136', 'top': '65', 'moveable': 'true'}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_progress_bar(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'progress_bar.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {
            'progress_bar': {'closeable': 'true', 'model': 'window', 'top': '65', 'width': '136', 'left': '106',
                             'height': '122', 'moveable': 'true', 'id': 'progress_bar'},
            'ProgressBar1': {'height': '24', 'model': 'progressmeter', 'top': '33', 'width': '97', 'left': '23',
                             'id': 'ProgressBar1', 'tab-index': '0'}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_spin_control(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'spin_control.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {
            'spin_control': {'width': '136', 'top': '65', 'moveable': 'true', 'height': '122', 'left': '95',
                             'model': 'window', 'closeable': 'true', 'id': 'spin_control'},
            'SpinButton1': {'width': '97', 'top': '28', 'model': 'spinbutton', 'left': '23', 'tab-index': '0',
                            'id': 'SpinButton1', 'height': '27'}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_text_box(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'text_box.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_xdl_context()
        # print(result)
        expected_result = {
            'text_box': {'moveable': 'true', 'model': 'window', 'closeable': 'true', 'left': '106', 'top': '65',
                         'height': '122', 'id': 'text_box', 'width': '136'},
            'TextField1': {'tab-index': '0', 'model': 'textfield', 'id': 'TextField1', 'left': '20', 'top': '26',
                           'height': '19', 'width': '103'}}
        self.assertEqual(result, expected_result)


class ContextGeneratorTestsGetUNOContext(unittest.TestCase):
    def test_extractor_ContextGenerator_dialog(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'dialog.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {'dialog': {'model': 'window', 'Name': 'dialog', 'uno_model': 'Dialog', 'PositionX': '106',
                                      'Closeable': 'True', 'Width': 136, 'PositionY': '65', 'Moveable': 'True',
                                      'Height': 122}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_button(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'button.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {
            'CommandButton1': {'Name': 'CommandButton1', 'Width': 88, 'uno_model': 'Button', 'model': 'button',
                               'PositionX': '27', 'Label': 'CommandButton1', 'TabIndex': 0, 'PositionY': '20',
                               'Height': 82},
            'button': {'model': 'window', 'Name': 'button', 'uno_model': 'Dialog', 'PositionX': '106',
                       'Closeable': 'True', 'Width': 136, 'PositionY': '65', 'Moveable': 'True', 'Height': 122}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_check_box(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'check_box.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {
            'check_box': {'model': 'window', 'Name': 'check_box', 'uno_model': 'Dialog', 'PositionX': '106',
                          'Closeable': 'True', 'Width': 136, 'PositionY': '65', 'Moveable': 'True', 'Height': 122},
            'CheckBox1': {'Name': 'CheckBox1', 'Width': 105, 'uno_model': 'CheckBox', 'model': 'checkbox',
                          'PositionX': '19', 'Label': 'CheckBox1', 'TabIndex': 0, 'PositionY': '23', 'State': 'False',
                          'Height': 17}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_combo_box(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'combo_box.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {
            'ComboBox1': {'model': 'combobox', 'Name': 'ComboBox1', 'uno_model': 'ComboBox', 'PositionX': '20',
                          'Width': 103, 'TabIndex': 0, 'Dropdown': 'True', 'PositionY': '20', 'Height': 25},
            'combo_box': {'model': 'window', 'Name': 'combo_box', 'uno_model': 'Dialog', 'PositionX': '106',
                          'Closeable': 'True', 'Width': 136, 'PositionY': '65', 'Moveable': 'True', 'Height': 122}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_currency_field(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'currency_field.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {
            'currency_field': {'model': 'window', 'Name': 'currency_field', 'uno_model': 'Dialog', 'PositionX': '95',
                               'Closeable': 'True', 'Width': 136, 'PositionY': '65', 'Moveable': 'True', 'Height': 122},
            'CurrencyField1': {'Name': 'CurrencyField1', 'Width': 108, 'uno_model': 'CurrencyField', 'PositionX': '16',
                               'model': 'currencyfield', 'TabIndex': 0, 'PositionY': '28', 'Height': 20}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_date_field(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'date_field.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {
            'DateField1': {'Name': 'DateField1', 'Width': 92, 'uno_model': 'DateField', 'PositionX': '26',
                           'model': 'datefield', 'TabIndex': 0, 'PositionY': '28', 'Height': 20},
            'date_field': {'model': 'window', 'Name': 'date_field', 'uno_model': 'Dialog',
                           'PositionX': '95', 'Closeable': 'True', 'Width': 136, 'PositionY': '65',
                           'Moveable': 'True', 'Height': 122}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_file_control(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'file_control.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {'FileControl1': {'PositionY': '18', 'PositionX': '16', 'model': 'filecontrol', 'Height': 17,
                                            'uno_model': 'FileControl', 'TabIndex': 0, 'Name': 'FileControl1',
                                            'Width': 101},
                           'file_control': {'Closeable': 'True', 'PositionY': '65', 'PositionX': '95',
                                            'model': 'window',
                                            'Height': 122, 'uno_model': 'Dialog', 'Moveable': 'True',
                                            'Name': 'file_control', 'Width': 136}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_fixed_line_h(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'fixed_line_h.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {
            'fixed_line_h': {'Height': 122, 'PositionX': '95', 'model': 'window', 'Moveable': 'True', 'Width': 136,
                             'PositionY': '65', 'Closeable': 'True', 'Name': 'fixed_line_h', 'uno_model': 'Dialog'},
            'FixedLine1': {'Height': 4, 'PositionX': '16', 'model': 'fixedline', 'Width': 111, 'PositionY': '26',
                           'Name': 'FixedLine1', 'TabIndex': 0, 'uno_model': 'FixedLine'}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_fixed_line_v(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'fixed_line_v.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {
            'fixed_line_v': {'Closeable': 'True', 'Name': 'fixed_line_v', 'Moveable': 'True', 'uno_model': 'Dialog',
                             'PositionY': '65', 'PositionX': '95', 'Height': 122, 'model': 'window', 'Width': 136},
            'FixedLine1': {'Width': 3, 'Name': 'FixedLine1', 'PositionY': '23', 'uno_model': 'FixedLine',
                           'PositionX': '19', 'Height': 89, 'model': 'fixedline', 'Orientation': 1, 'TabIndex': 0}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_formmated_field(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'formmated_field.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {
            'formmated_field': {'Closeable': 'True', 'PositionY': '65', 'Moveable': 'True', 'Height': 122,
                                'model': 'window', 'PositionX': '95', 'uno_model': 'Dialog', 'Width': 136,
                                'Name': 'formmated_field'},
            'FormattedField1': {'PositionY': '18', 'TabIndex': 0, 'Height': 22, 'model': 'formattedfield',
                                'Name': 'FormattedField1', 'uno_model': 'FormattedField', 'Width': 108,
                                'PositionX': '16'}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_group_box(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'group_box.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {
            'FrameControl1': {'Name': 'FrameControl1', 'PositionY': '14', 'PositionX': '28', 'Label': 'FrameControl1',
                              'Height': 82, 'uno_model': 'GroupBox', 'TabIndex': 0, 'model': 'titledbox', 'Width': 88},
            'group_box': {'PositionY': '65', 'Moveable': 'True', 'PositionX': '106', 'Name': 'group_box', 'Height': 122,
                          'uno_model': 'Dialog', 'Closeable': 'True', 'model': 'window', 'Width': 136}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_image_control(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'image_control.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {
            'ImageControl1': {'PositionY': '28', 'TabIndex': 0, 'Name': 'ImageControl1', 'uno_model': 'ImageControl',
                              'Height': 69, 'model': 'img', 'Width': 92, 'PositionX': '23'},
            'image_control': {'PositionY': '65', 'Moveable': 'True', 'PositionX': '95', 'Name': 'image_control',
                              'Height': 122, 'uno_model': 'Dialog', 'Closeable': 'True', 'model': 'window',
                              'Width': 136}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_label(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'label.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {
            'Label1': {'Name': 'Label1', 'PositionY': '26', 'PositionX': '21', 'Label': 'Label1', 'Height': 40,
                       'uno_model': 'FixedText', 'TabIndex': 0, 'model': 'text', 'Width': 99},
            'label': {'PositionY': '65', 'Moveable': 'True', 'PositionX': '106', 'Name': 'label', 'Height': 122,
                      'uno_model': 'Dialog', 'Closeable': 'True', 'model': 'window', 'Width': 136}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_list_box(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'list_box.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {'ListBox1': {'model': 'menulist', 'Height': 92, 'PositionY': '13', 'Name': 'ListBox1',
                                        'uno_model': 'ListBox', 'TabIndex': 0, 'Width': 84, 'PositionX': '29'},
                           'list_box': {'model': 'window', 'Height': 122, 'PositionY': '65', 'Name': 'list_box',
                                        'Moveable': 'True', 'uno_model': 'Dialog', 'Closeable': 'True', 'Width': 136,
                                        'PositionX': '106'}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_numeric_field(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'numeric_field.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {
            'numeric_field': {'model': 'window', 'Height': 122, 'PositionY': '65', 'Name': 'numeric_field',
                              'Moveable': 'True', 'uno_model': 'Dialog', 'Closeable': 'True', 'Width': 136,
                              'PositionX': '95'},
            'NumericField1': {'model': 'numericfield', 'Height': 24, 'PositionY': '24', 'Name': 'NumericField1',
                              'uno_model': 'NumericField', 'TabIndex': 0, 'Width': 101, 'PositionX': '19'}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_option_box(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'option_box.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {'option_box': {'model': 'window', 'Height': 122, 'PositionY': '65', 'Name': 'option_box',
                                          'Moveable': 'True', 'uno_model': 'Dialog', 'Closeable': 'True', 'Width': 136,
                                          'PositionX': '106'},
                           'OptionButton2': {'model': 'radio', 'Height': 19, 'PositionY': '50', 'Name': 'OptionButton2',
                                             'Label': 'OptionButton2', 'uno_model': 'RadioButton', 'TabIndex': 1,
                                             'Width': 93, 'PositionX': '27'},
                           'OptionButton1': {'model': 'radio', 'Height': 17, 'PositionY': '24', 'Name': 'OptionButton1',
                                             'Label': 'OptionButton1', 'uno_model': 'RadioButton', 'TabIndex': 0,
                                             'Width': 92, 'PositionX': '28'}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_pattern_field(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'pattern_field.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {
            'PatternField1': {'model': 'patternfield', 'Height': 19, 'PositionY': '18', 'Name': 'PatternField1',
                              'uno_model': 'PatternField', 'TabIndex': 0, 'Width': 111, 'PositionX': '15'},
            'pattern_field': {'model': 'window', 'Height': 122, 'PositionY': '65', 'Name': 'pattern_field',
                              'Moveable': 'True', 'uno_model': 'Dialog', 'Closeable': 'True', 'Width': 136,
                              'PositionX': '95'}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_progress_bar(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'progress_bar.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {'progress_bar': {'model': 'window', 'Height': 122, 'PositionY': '65', 'Name': 'progress_bar',
                                            'Moveable': 'True', 'uno_model': 'Dialog', 'Closeable': 'True',
                                            'Width': 136,
                                            'PositionX': '106'},
                           'ProgressBar1': {'model': 'progressmeter', 'Height': 24, 'PositionY': '33',
                                            'Name': 'ProgressBar1', 'uno_model': 'ProgressBar', 'TabIndex': 0,
                                            'Width': 97, 'PositionX': '23'}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_spin_control(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'spin_control.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {'spin_control': {'model': 'window', 'Height': 122, 'PositionY': '65', 'Name': 'spin_control',
                                            'Moveable': 'True', 'uno_model': 'Dialog', 'Closeable': 'True',
                                            'Width': 136,
                                            'PositionX': '95'},
                           'SpinButton1': {'model': 'spinbutton', 'Height': 27, 'PositionY': '28',
                                           'Name': 'SpinButton1',
                                           'uno_model': 'SpinButton', 'TabIndex': 0, 'Width': 97, 'PositionX': '23'}}
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_text_box(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'text_box.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_uno_context()
        # print(result)
        expected_result = {'TextField1': {'model': 'textfield', 'Height': 19, 'PositionY': '26', 'Name': 'TextField1',
                                          'uno_model': 'Edit', 'TabIndex': 0, 'Width': 103, 'PositionX': '20'},
                           'text_box': {'model': 'window', 'Height': 122, 'PositionY': '65', 'Name': 'text_box',
                                        'Moveable': 'True', 'uno_model': 'Dialog', 'Closeable': 'True', 'Width': 136,
                                        'PositionX': '106'}}
        self.assertEqual(result, expected_result)


class ContextGeneratorTestsGetDiff(unittest.TestCase):
    def test_extractor_ContextGenerator_dialog(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'dialog.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/dialog.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_button(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'button.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/button.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_check_box(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'check_box.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/check_box.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_combo_box(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'combo_box.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/combo_box.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_currency_field(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'currency_field.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/currency_field.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_date_field(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'date_field.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/date_field.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_file_control(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'file_control.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/file_control.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_fixed_line_h(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'fixed_line_h.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/fixed_line_h.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_fixed_line_v(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'fixed_line_v.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/fixed_line_v.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_formmated_field(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'formmated_field.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/formmated_field.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_group_box(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'group_box.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/group_box.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_image_control(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'image_control.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/image_control.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_label(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'label.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/label.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_list_box(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'list_box.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/list_box.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_numeric_field(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'numeric_field.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/numeric_field.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_option_box(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'option_box.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/option_box.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_pattern_field(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'pattern_field.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/pattern_field.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_progress_bar(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'progress_bar.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/progress_bar.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_spin_control(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'spin_control.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/spin_control.xdl vs. schema.py'
        self.assertEqual(result, expected_result)

    def test_extractor_ContextGenerator_text_box(self):
        test_dir = '/home/sasa/.config/libreoffice/4/user/basic/Test_dialog/'
        dialog = os.path.join(test_dir, 'text_box.xdl')
        ctx_generator = extractor.ContextGenerator(dialog)
        result = ctx_generator.get_diff(ctx_generator.get_xdl_context())
        # print(result)
        expected_result = 'NO DIFF /home/sasa/.config/libreoffice/4/user/basic/Test_dialog/text_box.xdl vs. schema.py'
        self.assertEqual(result, expected_result)


def suite():
    extractor_suite = unittest.TestSuite()
    extractor_suite.addTest(unittest.makeSuite(ContextGeneratorTests))
    extractor_suite.addTest(unittest.makeSuite(ContextGeneratorTestsGetXdlContext))
    extractor_suite.addTest(unittest.makeSuite(ContextGeneratorTestsGetUNOContext))
    extractor_suite.addTest(unittest.makeSuite(ContextGeneratorTestsGetDiff))
    return extractor_suite


def main():
    unittest.main()


if __name__ == '__main__':
    main()
