# not xdl propeties: ns, uno_name
# SpinButton1  {'model': 'spinbutton', 'uno_model': 'SpinButton', 'Name': 'SpinButton1', 'PositionX': '235', 'TabIndex': '22', 'Width': '60', 'Height': '20', 'PositionY': '167'}

properties = {
    'bulletinboard': {
        'ns': {'name': './/dlg:bulletinboard', 'type': 'string'},
        'uno_name': {'name': '', 'type': 'string'}},
    'button': {
        'align': {'name': 'Align', 'type': 'short', 'special': {'center': 1, 'left': 0, 'right': 2, 'default': 1}},
        'button-type': {'name': 'PushButtonType', 'type': 'integer',
                        'special': {'help': 3, 'ok': 1, 'cancel': 2, 'default': 0}},
        'disabled': {'name': 'Enabled', 'type': 'boolean'},
        'grab-focus': {'name': 'FocusOnClick', 'type': 'boolean'},
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'ns': {'name': './/dlg:button', 'type': 'string'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'toggled': {'name': 'Toggle', 'type': 'integer'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'Button', 'type': 'string'},
        'value': {'name': 'Label', 'type': 'string'},
        'visible': {'name': 'EnableVisible', 'type': 'boolean'},
        'width': {'name': 'Width', 'type': 'long'}},
    'checkbox': {
        'checked': {'name': 'State', 'type': 'boolean'},
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'ns': {'name': './/dlg:checkbox', 'type': 'string'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'tristate': {'name': 'TriState', 'type': 'boolean'},
        'uno_name': {'name': 'CheckBox', 'type': 'string'},
        'value': {'name': 'Label', 'type': 'string'},
        'width': {'name': 'Width', 'type': 'long'}},
    'combobox': {
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'ns': {'name': './/dlg:combobox', 'type': 'string'},
        'spin': {'name': 'Dropdown', 'type': 'boolean'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'ComboBox', 'type': 'string'},
        'value': {'name': 'StringItemList', 'type': 'sequence'},
        'width': {'name': 'Width', 'type': 'long'}},
    'currencyfield': {
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'ns': {'name': './/dlg:currencyfield', 'type': 'string'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'thousands-separator': {'name': 'ShowThousandsSeparator', 'type': 'boolean'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'CurrencyField', 'type': 'string'},
        'value': {'name': 'Value', 'type': 'integer'},
        'width': {'name': 'Width', 'type': 'long'}},
    'datefield': {
        'date-format': {'name': 'DateFormat', 'type': 'integer',
                        'special': {'short_MMDDYYYY': 8, 'short_DDMMYY': 4, 'short_YYMMDD': 6, 'system_short YYYY': 2,
                                    'short_MMDDYY': 5, 'short_YYYYMMDD': 9, 'system_long': 3,
                                    'short_YYMMDD_DIN5008': 10, 'system_short': 0, 'short_YYYYMMDD_DIN5008': 11,
                                    'short_DDMMYYYY': 7, 'system_short YY': 1}},
        'dropdown': {'name': 'Dropdown', 'type': 'boolean'},
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'ns': {'name': './/dlg:datefield', 'type': 'string'},
        'repeat': {'name': 'RepeatDelay', 'type': 'integer'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'text': {'name': 'Text', 'type': 'string'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'DateField', 'type': 'string'},
        'value': {'name': 'Date', 'type': 'date'},
        'value-max': {'name': 'DateMax', 'type': 'date'},
        'value-min': {'name': 'DateMin', 'type': 'date'},
        'width': {'name': 'Width', 'type': 'long'}},
    'filecontrol': {
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'ns': {'name': './/dlg:filecontrol', 'type': 'string'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'FileControl', 'type': 'string'},
        'value': {'name': 'Text', 'type': 'string'},
        'width': {'name': 'Width', 'type': 'long'}},
    'fixedline': {
        'align': {'name': 'Orientation', 'type': 'integer', 'special': {'vertical': 1, 'horizontal': 0}},
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'ns': {'name': './/dlg:fixedline', 'type': 'string'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'FixedLine', 'type': 'string'},
        'width': {'name': 'Width', 'type': 'long'}},
    'formattedfield': {
        'align': {'name': 'Align', 'type': 'short', 'special': {'center': 1, 'left': 0, 'right': 2}},
        'format-code': {'name': '', 'type': ''},
        'format-locale': {'name': '', 'type': ''},
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'ns': {'name': './/dlg:formattedfield', 'type': 'string'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'text': {'name': 'Text', 'type': 'string'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'FormattedField', 'type': 'string'},
        'value': {'name': 'EffectiveValue', 'type': 'double'},
        'value-max': {'name': 'EffectiveMax', 'type': 'double'},
        'value-min': {'name': 'EffectiveMin', 'type': 'double'},
        'width': {'name': 'Width', 'type': 'long'}},
    'img': {
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'ns': {'name': './/dlg:img', 'type': 'string'},
        'src': {'name': 'ImageURL', 'type': 'string'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'ImageControl', 'type': 'string'},
        'width': {'name': 'Width', 'type': 'long'}},
    'menulist': {
        'align': {'name': 'Align', 'type': 'short', 'special': {'left': 0, 'center': 1, 'right': 2}},
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'linecount': {'name': 'LineCount', 'type': 'short'},
        'multiselection': {'name': 'MultiSelection', 'type': 'boolean'},
        'ns': {'name': './/dlg:menulist', 'type': 'string'},
        'spin': {'name': 'Dropdown', 'type': 'boolean'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'ListBox', 'type': 'string'},
        'value': {'name': 'StringItemList', 'type': 'sequence'},
        'width': {'name': 'Width', 'type': 'long'}},
    'numericfield': {
        'decimal-accuracy': {'name': 'DecimalAccuracy', 'type': 'short'},
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'ns': {'name': './/dlg:numericfield', 'type': 'string'},
        'spin': {'name': 'Spin', 'type': 'boolean'},
        'strict-format': {'name': 'StrictFormat', 'type': 'boolean'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'NumericField', 'type': 'string'},
        'value': {'name': 'Value', 'type': 'double'},
        'value-max': {'name': 'ValueMax', 'type': 'double'},
        'value-min': {'name': 'ValueMin', 'type': 'double'},
        'width': {'name': 'Width', 'type': 'long'}},
    'patternfield': {
        'edit-mask': {'name': 'EditMask', 'type': 'string'},
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'literal-mask': {'name': 'LiteralMask', 'type': 'string'},
        'ns': {'name': './/dlg:patternfield', 'type': 'string'},
        'strict-format': {'name': 'StrictFormat', 'type': 'boolean'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'PatternField', 'type': 'string'},
        'value': {'name': 'Text', 'type': 'string'},
        'width': {'name': 'Width', 'type': 'long'}},
    'progressmeter': {
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'ns': {'name': './/dlg:progressmeter', 'type': 'string'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'ProgressBar', 'type': 'string'},
        'value': {'name': 'ProgressValue', 'type': 'integer'},
        'width': {'name': 'Width', 'type': 'long'}},
    'radio': {
        'checked': {'name': 'State', 'type': 'boolean'},
        'group-name': {'name': '', 'type': ''},
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'ns': {'name': './/dlg:radio', 'type': 'string'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'RadioButton', 'type': 'string'},
        'value': {'name': 'Label', 'type': 'string'},
        'width': {'name': 'Width', 'type': 'long'}},
    'radiogroup': {
        'ns': {'name': './/dlg:radiogroup', 'type': 'string'},
        'uno_name': {'name': 'RadioGroup', 'type': 'string'}},
    'scrollbar': {
        'ns': {'name': './/dlg:scrollbar', 'type': 'string'},
        'uno_name': {'name': 'ScrollBar', 'type': 'string'}},
    'spinbutton': {
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'ns': {'name': './/dlg:spinbutton', 'type': 'string'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'SpinButton', 'type': 'string'},
        'width': {'name': 'Width', 'type': 'long'}},
    'style': {
        'ns': {'name': './/dlg:style', 'type': 'string'},
        'uno_name': {'name': '', 'type': 'string'}},
    'styles': {
        'ns': {'name': './/dlg:styles', 'type': 'string'},
        'uno_name': {'name': '', 'type': 'string'}},
    'text': {
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'ns': {'name': './/dlg:text', 'type': 'string'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'FixedText', 'type': 'string'},
        'value': {'name': 'Label', 'type': 'string'},
        'width': {'name': 'Width', 'type': 'long'}},
    'textfield': {
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'ns': {'name': './/dlg:textfield', 'type': 'string'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'Edit', 'type': 'string'},
        'value': {'name': 'Text', 'type': 'string'},
        'width': {'name': 'Width', 'type': 'long'}},
    'timefield': {
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'ns': {'name': './/dlg:timefield', 'type': 'string'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'text': {'name': 'Text', 'type': 'string'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'TimeField', 'type': 'string'},
        'value': {'name': 'Time', 'type': 'time'},
        'value-max': {'name': 'TimeMax', 'type': 'time'},
        'value-min': {'name': 'TimeMin', 'type': 'time'},
        'width': {'name': 'Width', 'type': 'long'}},
    'title': {
        'ns': {'name': './/dlg:title', 'type': 'string'},
        'uno_name': {'name': 'title', 'type': 'string'},
        'value': {'name': 'Label', 'type': 'string'}},
    'titledbox': {
        'height': {'name': 'Height', 'type': 'long'},
        'help-text': {'name': 'HelpText', 'type': 'string'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'ns': {'name': './/dlg:titledbox', 'type': 'string'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'GroupBox', 'type': 'string'},
        'value': {'name': 'Label', 'type': 'string'},
        'width': {'name': 'Width', 'type': 'long'}},
    'treecontrol': {
        'height': {'name': 'Height', 'type': 'long'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'ns': {'name': './/dlg:treecontrol', 'type': 'string'},
        'tab-index': {'name': 'TabIndex', 'type': 'short'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': '.tree.TreeControl', 'type': 'string'},
        'width': {'name': 'Width', 'type': 'long'}},
    'window': {
        'closeable': {'name': 'Closeable', 'type': 'boolean'},
        'height': {'name': 'Height', 'type': 'long'},
        'id': {'name': 'Name', 'type': 'string'},
        'left': {'name': 'PositionX', 'type': 'string'},
        'moveable': {'name': 'Moveable', 'type': 'boolean'},
        'ns': {'name': './/dlg:window', 'type': 'string'},
        'title': {'name': 'Title', 'type': 'string'},
        'top': {'name': 'PositionY', 'type': 'string'},
        'uno_name': {'name': 'Dialog', 'type': 'string'},
        'width': {'name': 'Width', 'type': 'long'}},
    'event': {
        'ns': {'name': './/script:event', 'type': 'string'}},
}