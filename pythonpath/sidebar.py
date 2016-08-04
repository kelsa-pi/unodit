import os
import string
import logging

try:
    import config as conf
except ImportError:
    import pythonpath.config as conf


class SidebarGenerator:
    """
    Generate python code
    """

    def __init__(self, mode, pydir, xdlfile, context, app='MyApp', indent=4, **kwargs):
        self.xdlfile = xdlfile
        self.context = context
        self.pydir = pydir
        self.app = app
        self.mode = mode
        self.kwargs = kwargs
        self.panel_list = self.get_panel_list()
        self.config = conf.ReadINI(conf.MAIN_DIR, self.pydir)
        self.SOURCE_DIR = self.config.get('directories', 'source_dir')
        self.logger = logging.getLogger('unodit.sidebar.SidebarGenerator')
        self.logger.info('NEW LOGGER: unodit.sidebar.SidebarGenerator')

        if self.config.get('directories', 'templates_dir') == 'templates':
            self.tempates_dir = os.path.join(conf.MAIN_DIR, 'templates')
        else:
            self.tempates_dir = self.config.get('directories', 'templates_dir')
        self.logger.info('templates directory: ' + self.tempates_dir)

        if indent == 0:
            self.indent = '\t'
        else:
            self.indent = indent * " "

        # read all templates
        if self.mode == 'sidebar_convert':
            # sidebar main exe file
            py_tmpl_dir = os.path.join(self.tempates_dir, 'sidebar_convert')
            self.sidebar_main = string.Template(self.get_template(py_tmpl_dir, '100_sidebar_main.txt'))
            self.sidebar_run_panels = string.Template(self.get_template(py_tmpl_dir, '101_sidebar_show_panels.txt'))

            self.logger.info('successfully read all templates for script files')

    def get_template(self, py_tmpl_dir, template):
        templ = os.path.join(py_tmpl_dir, template)
        with open(templ, 'rt') as t:
            tt = t.read()
        return tt

    def get_panel_list(self):
        for name, value in self.kwargs.items():
            if name == 'all_panels':
                pl = value.split(',')
        return pl

    def generate_sidebar_code(self):

        sdb_main = {'I': self.indent,
                    'IMPORT_PANELS': self._get_import_panels(),
                    'EXTENSION_IDENTIFIER_DOMAIN': self.config.get('extension', 'identifier_domain'),
                    'EXTENSION_IDENTIFIER_APP': self.config.get('extension', 'identifier_app'),
                    'SIDEBAR_PROTOCOL': self.config.get('sidebar', 'protocol'),
                    'RUN_PANELS': self._run_panels(),
                    }
        sidebar_main = self.sidebar_main.substitute(sdb_main)
        self.write_sidebar_main_file(sidebar_main)

    def _get_import_panels(self):

        logic_dir = self.config.get('sdb_directories', 'sdb_ui_logic')
        panels = ''

        for i in self.panel_list:
            exec_file_name = i
            panels = panels + 'from ' + logic_dir + '.' + exec_file_name + ' import ' + exec_file_name + '\n'

        return panels

    def _run_panels(self):
        code = ''

        for i in self.panel_list:
            pn = {'I': self.indent,
                  'PANEL_NAME': i
                  }
            code += self.sidebar_run_panels.substitute(pn)

        return code

    def write_sidebar_main_file(self, sdb_text):

        sdb_main = self.app + '.py'
        py_file_path = os.path.join(self.pydir, self.SOURCE_DIR, sdb_main)

        py_main_ui_file = open(py_file_path, 'w')
        py_main_ui_file.write(sdb_text)
        py_main_ui_file.close()

