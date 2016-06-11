import os
import string
import zipfile
import logging

try:
    import config as conf
except ImportError:
    import pythonpath.config as conf


class EasyDialog:
    def __init__(self, pydir='', app='MyApp'):
        self.pydir = pydir
        self.app = app
        self.code = {}
        self.config = conf.ReadINI(conf.MAIN_DIR, self.pydir)
        self.ext_tmpl_dir = os.path.join(conf.TEMPLATES_DIR, 'dialogs')
        self.logger = logging.getLogger('unodit.simple_dialogs.EasyDialog')
        self.logger.info('NEW LOGGER: unodit.simple_dialogs.EasyDialog')

    def get_template(self, ex_tmpl_dir, template):
        templ = os.path.join(ex_tmpl_dir, template)
        with open(templ, 'rt') as t:
            tt = t.read()
        return tt

    def create_template(self):
        # ui file
        d = os.path.join(self.pydir, self.config.get('directories', 'source_dir'), 'pythonpath')
        if not os.path.exists(d):
            os.makedirs(d)

        s = {
            'GENERATED_DATETIME': conf.NOW,
            'UNODIT_VERSION': conf.VERSION,
        }

        f = os.path.join(d, 'simple_dialogs.py')
        t = string.Template(self.get_template(self.ext_tmpl_dir, '1_dialogs_ui.txt'))
        ext_text = t.substitute(s)
        self.logger.info('simple dialogs file ' + f + ' ' + str(s))

        ef = open(f, 'w')
        ef.write(ext_text)
        ef.close()

        # exec file
        d = os.path.join(self.pydir, self.config.get('directories', 'source_dir'))
        if not os.path.exists(d):
            os.makedirs(d)

        s = {
            'APP_NAME': self.app,
            'EXEC_FUNCTION_PREFIX': self.config.get('exec_function', 'prefix')
        }

        f = os.path.join(d, self.app + '.py')
        t = string.Template(self.get_template(self.ext_tmpl_dir, '2_dialogs_main.txt'))
        ext_text = t.substitute(s)
        self.logger.info('application file ' + f + ' ' + str(s))

        ef = open(f, 'w')
        ef.write(ext_text)
        ef.close()

