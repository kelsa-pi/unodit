import argparse
import logging
import os

try:
    # extension
    import extractor
    import generator
    import oxt_creator as script
    import simple_dialogs as dialogs
    import embed_packer as ep
    import sidebar
    from config import LOGGER_NAME, LOG_FILE, VERSION, NOW, MAIN_DIR, ReadINI

except ImportError:
    # command line
    import pythonpath.extractor as extractor
    import pythonpath.generator as generator
    import pythonpath.oxt_creator as script
    import pythonpath.simple_dialogs as dialogs
    import pythonpath.embed_packer as ep
    import pythonpath.sidebar as sidebar
    from pythonpath.config import LOGGER_NAME, LOG_FILE, VERSION, NOW, MAIN_DIR, ReadINI


def create_logger(lname, ldir, lfile):
    # create logger
    logger = logging.getLogger(lname)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    logfile = os.path.join(ldir, lfile)
    fh = logging.FileHandler(logfile, mode='w')
    fh.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(module)s - %(funcName)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    return logger


def unodit(mode, pydir, xdlfile='', app='MyApp', panel=2, indent=4):
    """
    UNODialogTools automate some of the tedious tasks with dialogs in order to help you write your own extension for LibreOffice in Python(PyUNO).

    :param mode:
    :param pydir: full path to the output directory
    :param xdlfile: full path to the xdl file
    :param app: application name
    :param panel: number od panels in sidebar, work with mode sidebar_convert
    :param indent: number of spaces used for indentation in the generated code. If 0, \t is used as indent

    """
    logger = logging.getLogger('unodit')

    start_log = """
Version:  {}      Created:  {}

unodit directory = {}
---------------------------------------------------------------------
mode      = {}
pydir     = {}
xdlfile   = {}
app name  = {}
panel     = {}
indent    = {}
---------------------------------------------------------------------
""".format(VERSION, NOW, MAIN_DIR, mode, pydir, xdlfile, app, panel, indent)

    logger.info(start_log)

    def mode_script_convert():

        logger.info('MODE: ---------- script_convert ----------------------------------')
        ctx = extractor.ContextGenerator(xdlfile)
        ctx.get_xdl_context()
        uno_ctx = ctx.get_uno_context()
        cg = generator.CodeGenerator(mode, pydir, xdlfile, uno_ctx, app, indent=4)
        cg.generate_code()

    def mode_script_files():
        logger.info('MODE: ---------- script_files ------------------------------------')
        sef = script.ScriptExtensionFiles(mode, pydir, app)
        sef.create()

    def mode_script_oxt():
        logger.info('MODE: ---------- script_oxt --------------------------------------')
        cse = script.CreateScriptExtension(mode, pydir, app)
        cse.create()

    def mode_script_all():
        mode_script_convert()
        mode_script_files()
        mode_script_oxt()

    def mode_connect():

        logger.info('MODE: ---------- connect -----------------------------------------')
        ctx = extractor.ContextGenerator(xdlfile)
        ctx.get_xdl_context()
        uno_ctx = ctx.get_uno_context()
        cg = generator.CodeGenerator(mode, pydir, xdlfile, uno_ctx, app, indent=4)
        cg.generate_code()

    def mode_embed_convert():

        logger.info('MODE: ---------- embed_convert -----------------------------------')
        ctx = extractor.ContextGenerator(xdlfile)
        ctx.get_xdl_context()
        uno_ctx = ctx.get_uno_context()
        cg = generator.CodeGenerator(mode, pydir, xdlfile, uno_ctx, app, indent=4)
        cg.generate_code()

    def mode_embed_pack():
        logger.info('MODE: ---------- embed_pack --------------------------------------')
        e = ep.EmbedScript(pydir, app)
        e.pack_script()

    def mode_embed_all():
        mode_embed_convert()
        mode_embed_pack()

    def mode_dialogs_create():
        logger.info('MODE: ---------- dialogs_create ----------------------------------')
        e = dialogs.EasyDialog(pydir, app)
        e.create_template()

    def mode_dialogs_files():
        logger.info('MODE: ---------- dialogs_files -----------------------------------')
        sef = script.ScriptExtensionFiles(mode, pydir, app, )
        sef.create()

    def mode_dialogs_oxt():
        logger.info('MODE: ---------- dialogs_oxt -------------------------------------')
        cse = script.CreateScriptExtension(mode, pydir, app, )
        cse.create()

    def mode_dialogs_all():
        logger.info('MODE: ---------- dialogs_all -------------------------------------')
        mode_dialogs_create()
        mode_dialogs_files()
        mode_dialogs_oxt()

    def mode_sidebar_convert():
        logger.info('MODE: ---------- sidebar_convert ---------------------------------')
        p_names = ''

        for i in range(0, panel):

            # read config.ini for xdl file
            read_conf = ReadINI(MAIN_DIR, pydir)
            panel_section = 'panel'+ str(i + 1)
            file_xdl = read_conf.get(panel_section, 'xdl_ui')
            panel_name = read_conf.get(panel_section, 'name')

            # generate panel files
            ctx = extractor.ContextGenerator(file_xdl)
            ctx.get_xdl_context()
            uno_ctx = ctx.get_uno_context()
            cg = generator.CodeGenerator(mode, pydir, file_xdl, uno_ctx, app, indent=4, panel_name=panel_name)
            cg.generate_code()

            p_names = p_names + panel_name + ','

        # generate sidebar main file
        p_names = p_names[:-1]
        sb = sidebar.SidebarGenerator(mode, pydir, file_xdl, uno_ctx, app, indent=4, all_panels=p_names)
        sb.generate_sidebar_code()

    def mode_sidebar_files():
        logger.info('MODE: ---------- dialogs_files -----------------------------------')
        sef = script.SidebarExtensionFiles(mode, pydir, app, panel)
        sef.create()

    def get_sidebar_panels():

        for i in range(0, panel):
            # read config.ini for xdl file
            read_conf = ReadINI(MAIN_DIR, pydir)
            panel_section = 'panel' + str(i + 1)
            file_xdl = read_conf.get(panel_section, 'xdl_ui')
            panel_name = read_conf.get(panel_section, 'name')
            p_names = p_names + panel_name + ','

        p_names = p_names[:-1]
        return p_names

    # script - convert xdl file (1)
    if mode == 'script_convert':
        mode_script_convert()

    # script - create script extension files (2)
    elif mode == 'script_files':
        mode_script_files()

    # script - create script exstension (3)
    elif mode == 'script_oxt':
        mode_script_oxt()

    # script all |1+2+3| (4)
    elif mode == 'script_all':
        mode_script_all()

    # connect - connect to xdl file (5)
    elif mode == 'connect':
        mode_connect()

    # embed dialog in document - convert xdl file (6)
    elif mode == 'embed_convert':
        mode_embed_convert()

    # embed dialog in document - pack script in document (7)
    elif mode == 'embed_pack':
        mode_embed_pack()

    # embed dialog in document all |6+7| (8)
    elif mode == 'embed_all':
        mode_embed_all()

    # simple dialogs - create (9)
    elif mode == 'dialogs_create':
        mode_dialogs_create()

    # simple dialogs - create script extension files (10)
    elif mode == 'dialogs_files':
        mode_dialogs_files()

    # simple dialogs - create script exstension (11)
    elif mode == 'dialogs_oxt':
        mode_dialogs_oxt()

    # simple dialogs all |9+10+11| (12)
    elif mode == 'dialogs_all':
        mode_dialogs_all()

    # sidebar - convert xdl fils (13)
    elif mode == 'sidebar_convert':
        mode_sidebar_convert()

    # sidebar - convert xdl fils (13)
    elif mode == 'sidebar_files':
        mode_sidebar_files()

    print(start_log + '\nStatus: Finished')

    return 0


def create_parser():
    """
    Parses and returns arguments passed in
    """

    desc = """

    Example:

    Create python project TestLib in LIBREOFFICE_PATH/4/user/Scripts/python/
    Replace LIBREOFFICE_PATH with actual path.

    """

    # assign description to the help doc
    parser = argparse.ArgumentParser(
        prog="unodit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=desc,
        description="unodit is a Python unfinished library that takes a LibreOffice Basic Dialog XML file and: a) converts it to python code (PyUNO) b) connects it to other python code (PyUNO)")

    # add arguments
    parser.add_argument(
        '-m', '--mode', type=str, default='script_convert',
        help='script_convert - convert xdl file, script_files - create script extension files, script_oxt - create script extension, script_all - convert xdl file, create script extension files and script extension, connect - connect to xdl file.',
        choices=['script_convert', 'script_files', 'script_oxt', 'script_all',
                 'connect', 'embed_convert', 'embed_pack', 'embed_all',
                 'dialogs_create', 'dialogs_files', 'dialogs_oxt', 'dialogs_all', 'sidebar_convert', 'sidebar_files'],
        required=True)

    parser.add_argument(
        '-d', '--dir', type=str, help='full path to the output directory', default=os.getcwd(), required=True)

    parser.add_argument(
        '-f', '--file', type=str, help='full path to the xdl file', required=False)

    parser.add_argument(
        '-a', '--appname', type=str, default='MyApp', help='application name', required=False)

    parser.add_argument(
        '-p', '--panel', type=int, default=2,
        help='number of panels in sidebar', required=False)

    parser.add_argument(
        '-i', '--indent', type=int, default=4,
        help='number of spaces used for indentation in the generated code. If 0, \t is used as indent',
        choices=[0, 1, 2, 3, 4], required=False)

    return parser


def main():

    parser = create_parser()
    args = parser.parse_args()

    # if args.mode is None:
    #     args.mode = 1
    #
    # if args.dir == '' or args.dir is None:
    #     args.dir = os.getcwd()

    if not os.path.exists(args.dir):
        os.makedirs(args.dir)

    create_logger(LOGGER_NAME, args.dir, LOG_FILE)

    unodit(args.mode,
           args.dir,
           args.file,
           args.appname,
           args.panel,
           args.indent,
           )

if __name__ == '__main__':
    main()
