import argparse
import logging
import os

try:
    # extension
    import extractor
    import generator
    import script_oxt_creator as script
    import simple_dialogs as dialogs
    import embed_packer as ep
    from config import LOGGER_NAME, LOG_FILE, VERSION, NOW, MAIN_DIR

except ImportError:
    # command line
    import pythonpath.extractor as extractor
    import pythonpath.generator as generator
    import pythonpath.script_oxt_creator as script
    import pythonpath.simple_dialogs as dialogs
    import pythonpath.embed_packer as ep
    from pythonpath.config import LOGGER_NAME, LOG_FILE, VERSION, NOW, MAIN_DIR


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


def unodit(xdlfile='', pydir='', app='MyApp', mode='script_convert', indent=4):
    """
    UNO Dialog Tools is a Python3 library (alpha version) that takes a LibreOffice Basic Dialog XML file (XDL) and:

    1. Convert XDL file to python code
    2. Connect to XDL file with python code
    3. Convert XDL file to python code and embed in document
    4. Provides a simple dialog boxes for interaction with a user

    Other features are:
    - if the option 1 or 4 is chosen, it is possible to create a script extension for LibreOffice (oxt file)
    - callback functions are created for all button onClick events
    - all steps in the conversion process are logged to log.log file in project root
    - per project customization with ini file (copy config.ini in project root)

    :param xdlfile: full path to the xdl file
    :param pydir: full path to the output directory
    :param app: application name
    :param mode: 'script_convert', 'script_files', 'script_oxt', 'script_all', 'connect'
    :param indent: number of spaces used for indentation in the generated code. If 0, \t is used as indent

    """
    logger = logging.getLogger('unodit')

    start_log = """

Version:  {}      Created:  {}

unodit directory = {}
---------------------------------------------------------------------
xdlfile   = {}
pydir     = {}
app name  = {}
mode      = {}
indent    = {}
---------------------------------------------------------------------
    """.format(VERSION, NOW, MAIN_DIR, xdlfile, pydir, app, mode, indent)

    logger.info(start_log)

    def mode_script_convert():

        logger.info('MODE: ---------- script_convert ----------------------------------')
        ctx = extractor.ContextGenerator(xdlfile)
        ctx.get_xdl_context()
        uno_ctx = ctx.get_uno_context()
        cg = generator.CodeGenerator(xdlfile, uno_ctx, pydir, app, mode, indent=4)
        cg.generate_code()

    def mode_script_files():
        logger.info('MODE: ---------- script_files ------------------------------------')
        sef = script.ScriptExtensionFiles(pydir, app)
        sef.create()

    def mode_script_oxt():
        logger.info('MODE: ---------- script_oxt --------------------------------------')
        cse = script.CreateScriptExtension(pydir, app)
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
        cg = generator.CodeGenerator(xdlfile, uno_ctx, pydir, app, mode, indent=4)
        cg.generate_code()

    def mode_embed_convert():

        logger.info('MODE: ---------- embed_convert -----------------------------------')
        ctx = extractor.ContextGenerator(xdlfile)
        ctx.get_xdl_context()
        uno_ctx = ctx.get_uno_context()
        cg = generator.CodeGenerator(xdlfile, uno_ctx, pydir, app, mode, indent=4)
        cg.generate_code()

    def mode_embed_pack():
        logger.info('MODE: ---------- embed_pack --------------------------------------')
        e = ep.EmbedScript(pydir, app, language='python')
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
        sef = script.ScriptExtensionFiles(pydir, app, mode)
        sef.create()
        pass

    def mode_dialogs_oxt():
        logger.info('MODE: ---------- dialogs_oxt -------------------------------------')
        cse = script.CreateScriptExtension(pydir, app, mode)
        cse.create()

    def mode_dialogs_all():
        logger.info('MODE: ---------- dialogs_all -------------------------------------')
        mode_dialogs_create()
        mode_dialogs_files()
        mode_dialogs_oxt()

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

    print('Finished')


def main():
    """
    Parses and returns arguments passed in
    """

    desc = """

    Example:

    Create python project TestLib in LIBREOFFICE_PATH/4/user/Scripts/python/
    Replace LIBREOFFICE_PATH with actual path.

    1) Convert XDL file to python code
    Use parameter -f to set the path to any local directory with ui file.
    Available options for parameter -m:
    'script_convert' - convert xdl file,
    'script_files' - create script extension files,
    'script_oxt' - create script extension,
    'script_all' - convert xdl file, create script extension files and script extension.

    python 3 unodit -f 'LIBREOFFICE_PATH/4/user/basic/DialogLib/Default.xdl'
                    -d 'LIBREOFFICE_PATH/4/user/Scripts/python/TestLib'
                    -a 'Test_convert'
                    -m  'script_convert'

    More examples in docs

    """

    # assign description to the help doc
    parser = argparse.ArgumentParser(
        prog="unodit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=desc,
        description="unodit is a Python unfinished library that takes a LibreOffice Basic Dialog XML file and: a) converts it to python code (PyUNO) b) connects it to other python code (PyUNO)")

    # add arguments

    parser.add_argument(
        '-f', '--file', type=str, help='full path to the xdl file', required=False)

    parser.add_argument(
        '-d', '--dir', type=str, help='full path to the output directory', default=os.getcwd(), required=False)

    parser.add_argument(
        '-a', '--appname', type=str, default='MyApp', help='application name', required=False)

    parser.add_argument(
        '-m', '--mode', type=str, default='script_convert',
        help='script_convert - convert xdl file, script_files - create script extension files, script_oxt - create script extension, script_all - convert xdl file, create script extension files and script extension, connect - connect to xdl file.',
        choices=['script_convert', 'script_files', 'script_oxt', 'script_all',
                 'connect', 'embed_convert', 'embed_pack', 'embed_all',
                 'dialogs_create', 'dialogs_files', 'dialogs_oxt', 'dialogs_all'], required=False)

    parser.add_argument(
        '-i', '--indent', type=int, default=4,
        help='number of spaces used for indentation in the generated code. If 0, \t is used as indent',
        choices=[0, 1, 2, 3, 4], required=False)

    args = parser.parse_args()

    if args.dir == '' or args.dir is None:
        args.dir = os.getcwd()

    if not os.path.exists(args.dir):
        os.makedirs(args.dir)

    if args.mode is None:
        args.mode = 1

    create_logger(LOGGER_NAME, args.dir, LOG_FILE)

    unodit(args.file,
           args.dir,
           args.appname,
           args.mode,
           args.indent,
           )


def run():
    # unfinished - LibreOffice extension
    xdlfile = 'LIBREOFFICE_PATH/4/user/basic/DialogLib/Default.xdl'
    mydir = 'LIBREOFFICE_PATH/4/user/Scripts/python/TestLib'

    create_logger(LOGGER_NAME, mydir, LOG_FILE)

    unodit(xdlfile, pydir=mydir, app='MyApp', mode='script_convert', indent=4)


if __name__ == '__main__':
    main()

g_exportedScripts = run,
