# This file is part of UNO Dialog Tools - UNODIT
# Copyright © 2016-2019 Sasa Kelecevic
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with UNODIT.  If not, see <http://www.gnu.org/licenses/>

"""
UNODIT executable module.

"""


import argparse
import logging
import os

try:
    # extension
    from unodit import extractor
    from unodit import generator
    from unodit import oxt_creator as script
    from unodit import simple_dialogs as dialogs
    from unodit import embed_packer as ep
    from unodit import sidebar
    from unodit.config import (LOGGER_NAME, LOG_FILE, VERSION,
                               NOW, MAIN_DIR, ReadINI)

except ImportError:
    # command line
    import pythonpath.extractor as extractor
    import pythonpath.generator as generator
    import pythonpath.oxt_creator as script
    import pythonpath.simple_dialogs as dialogs
    import pythonpath.embed_packer as ep
    import pythonpath.sidebar as sidebar
    from pythonpath.config import (
        LOGGER_NAME,
        LOG_FILE,
        VERSION,
        NOW,
        MAIN_DIR,
        ReadINI,
    )


def create_logger(lname, ldir, lfile):
    """Create logger

    :param lname:logger name
    :param ldir: logger directory
    :param lfile: logger file

    """

    logger = logging.getLogger(lname)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    logfile = os.path.join(ldir, lfile)
    fh = logging.FileHandler(logfile, mode="w")
    fh.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        "%(module)s - %(funcName)s - %(levelname)s - %(message)s"
    )
    fh.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    return logger


def unodit(mode, pydir, xdlfile="", app="MyApp", panel=2, indent=4):
    """
    UNODialogTools automate some of the tedious tasks with dialogs in order to help you write your own extension for LibreOffice in Python(PyUNO).

    :param mode:
    :param pydir: full path to the output directory
    :param xdlfile: full path to the xdl file
    :param app: application name
    :param panel: number od panels in sidebar, work with mode sidebar_convert
    :param indent: number of spaces used for indentation in the generated code. If 0, \t is used as indent

    """
    logger = logging.getLogger("unodit")

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
""".format(
        VERSION, NOW, MAIN_DIR, mode, pydir, xdlfile, app, panel, indent
    )

    logger.info(start_log)

    def mode_script_convert():
        logger.info(
            "\nMODE: ---------- script_convert ----------------------------------"
        )
        ctx = extractor.ContextGenerator(xdlfile)
        ctx.get_xdl_context()
        uno_ctx = ctx.get_uno_context()
        cg = generator.CodeGenerator(
            mode, pydir, xdlfile, uno_ctx, app, indent=4
        )
        cg.generate_code()

    def mode_script_files():
        logger.info(
            "\nMODE: ---------- script_files ------------------------------------"
        )
        sef = script.ScriptExtensionFiles(mode, pydir, app)
        sef.create()

    def mode_script_oxt():
        logger.info(
            "\nMODE: ---------- script_oxt --------------------------------------"
        )
        cse = script.CreateScriptExtension(mode, pydir, app)
        cse.create()

    def mode_script_all():
        mode_script_convert()
        mode_script_files()
        mode_script_oxt()

    def mode_connect():
        logger.info(
            "\nMODE: ---------- connect -----------------------------------------"
        )
        ctx = extractor.ContextGenerator(xdlfile)
        ctx.get_xdl_context()
        uno_ctx = ctx.get_uno_context()
        cg = generator.CodeGenerator(
            mode, pydir, xdlfile, uno_ctx, app, indent=4
        )
        cg.generate_code()

    def mode_embed_convert():
        logger.info(
            "\nMODE: ---------- embed_convert -----------------------------------"
        )
        ctx = extractor.ContextGenerator(xdlfile)
        ctx.get_xdl_context()
        uno_ctx = ctx.get_uno_context()
        cg = generator.CodeGenerator(
            mode, pydir, xdlfile, uno_ctx, app, indent=4
        )
        cg.generate_code()

    def mode_embed_pack():
        logger.info(
            "\nMODE: ---------- embed_pack --------------------------------------"
        )
        e = ep.EmbedScript(pydir, app)
        e.pack_script()

    def mode_embed_all():
        mode_embed_convert()
        mode_embed_pack()

    def mode_dialogs_create():
        logger.info(
            "\nMODE: ---------- dialogs_create ----------------------------------"
        )
        e = dialogs.EasyDialog(pydir, app)
        e.create_template()

    def mode_dialogs_files():
        logger.info(
            "\nMODE: ---------- dialogs_files -----------------------------------"
        )
        sef = script.ScriptExtensionFiles(mode, pydir, app)
        sef.create()

    def mode_dialogs_oxt():
        logger.info(
            "\nMODE: ---------- dialogs_oxt -------------------------------------"
        )
        cse = script.CreateScriptExtension(mode, pydir, app)
        cse.create()

    def mode_dialogs_all():
        logger.info(
            "\nMODE: ---------- dialogs_all -------------------------------------"
        )
        mode_dialogs_create()
        mode_dialogs_files()
        mode_dialogs_oxt()

    def mode_sidebar_convert():
        logger.info(
            "\nMODE: ---------- sidebar_convert ---------------------------------"
        )
        p_names = ""

        panel_names = {}

        # read config.ini for xdl file
        read_conf = ReadINI(MAIN_DIR, pydir)

        for i in range(0, panel):
            panel_section = "panel" + str(i + 1)
            file_xdl = read_conf.get(panel_section, "xdl_ui")
            panel_name = read_conf.get(panel_section, "name")
            # generate panel files
            ctx = extractor.ContextGenerator(file_xdl)
            ctx.get_xdl_context()
            uno_ctx = ctx.get_uno_context()
            cg = generator.CodeGenerator(
                mode,
                pydir,
                file_xdl,
                uno_ctx,
                app,
                indent=4,
                panel_name=panel_name,
            )
            cg.generate_code()
            # generate panel options files
            panel_option_name = read_conf.get(panel_section, "option_name")
            file_option_xdl = read_conf.get(panel_section, "xdl_option_ui")
            if file_option_xdl:
                panel_names[panel_name] = panel_option_name
                ctx_option = extractor.ContextGenerator(file_option_xdl)
                ctx_option.get_xdl_context()
                uno_ctx_option = ctx_option.get_uno_context()
                cg_option = generator.CodeGenerator(
                    mode,
                    pydir,
                    file_option_xdl,
                    uno_ctx_option,
                    app,
                    indent=4,
                    panel_name=panel_option_name,
                )
                cg_option.generate_code()
            else:
                panel_names[panel_name] = ""

            p_names = p_names + panel_name + ","

        # generate sidebar main file
        p_names = p_names[:-1]
        # print(str(panel_names))
        sb = sidebar.SidebarGenerator(
            mode,
            pydir,
            file_xdl,
            uno_ctx,
            app,
            indent=4,
            all_panels=panel_names,
        )
        sb.generate_sidebar_code()

    def mode_sidebar_files():
        logger.info(
            "\nMODE: ---------- dialogs_files -----------------------------------"
        )
        sef = script.SidebarExtensionFiles(mode, pydir, app, panel)
        sef.create()

    def mode_sidebar_oxt():
        logger.info(
            "\nMODE: ---------- sidebar_oxt -------------------------------------"
        )
        cse = script.CreateSidebarExtension(mode, pydir, app, panel)
        cse.create()

    # def get_sidebar_panels():
    #
    #     for i in range(0, panel):
    #         # read config.ini for xdl file
    #         read_conf = ReadINI(MAIN_DIR, pydir)
    #         panel_section = 'panel' + str(i + 1)
    #         file_xdl = read_conf.get(panel_section, 'xdl_ui')
    #         panel_name = read_conf.get(panel_section, 'name')
    #         p_names = p_names + panel_name + ','
    #
    #     p_names = p_names[:-1]
    #     return p_names

    # script - convert xdl file (1)
    if mode == "script_convert":
        mode_script_convert()

    # script - create script extension files (2)
    elif mode == "script_files":
        mode_script_files()

    # script - create script exstension (3)
    elif mode == "script_oxt":
        mode_script_oxt()

    # script all |1+2+3| (4)
    elif mode == "script_all":
        mode_script_all()

    # connect - connect to xdl file (5)
    elif mode == "connect":
        mode_connect()

    # embed dialog in document - convert xdl file (6)
    elif mode == "embed_convert":
        mode_embed_convert()

    # embed dialog in document - pack script in document (7)
    elif mode == "embed_pack":
        mode_embed_pack()

    # embed dialog in document all |6+7| (8)
    elif mode == "embed_all":
        mode_embed_all()

    # simple dialogs - create (9)
    elif mode == "dialogs_create":
        mode_dialogs_create()

    # simple dialogs - create script extension files (10)
    elif mode == "dialogs_files":
        mode_dialogs_files()

    # simple dialogs - create script exstension (11)
    elif mode == "dialogs_oxt":
        mode_dialogs_oxt()

    # simple dialogs all |9+10+11| (12)
    elif mode == "dialogs_all":
        mode_dialogs_all()

    # sidebar - convert xdl files (13)
    elif mode == "sidebar_convert":
        mode_sidebar_convert()

    # sidebar - create extension files (14)
    elif mode == "sidebar_files":
        mode_sidebar_files()

    # sidebar - create script exstension (15)
    elif mode == "sidebar_oxt":
        mode_sidebar_oxt()

    # sidebar all |13+14+15| (16)
    elif mode == "sidebar_all":
        mode_sidebar_convert()
        mode_sidebar_files()
        mode_sidebar_oxt()

    paths = ""
    for path, subdirs, files in os.walk(pydir):
        for name in files:
            paths = paths + os.path.join(path, name) + ",\n"
            # print(os.path.join(path, name))

    logger.info("\nCONTENT:" + pydir + " directory:\n" + paths)

    print("Finished", " mode " + mode)
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
        description="UNO Dialog Tools - unodit",
    )

    # add arguments
    parser.add_argument(
        "-m",
        "--mode",
        type=str,
        help="choose mode",
        choices=[
            "script_convert",
            "script_files",
            "script_oxt",
            "script_all",
            "connect",
            "embed_convert",
            "embed_pack",
            "embed_all",
            "dialogs_create",
            "dialogs_files",
            "dialogs_oxt",
            "dialogs_all",
            "sidebar_convert",
            "sidebar_files",
            "sidebar_oxt",
            "sidebar_all",
        ],
        required=True,
    )

    parser.add_argument(
        "-d",
        "--dir",
        type=str,
        help="full path to the output directory",
        default=os.getcwd(),
        required=True,
    )

    parser.add_argument(
        "-f",
        "--file",
        type=str,
        help="full path to the xdl file",
        required=False,
    )

    parser.add_argument(
        "-a",
        "--appname",
        type=str,
        default="MyApp",
        help="application name",
        required=False,
    )

    parser.add_argument(
        "-p",
        "--panel",
        type=int,
        default=2,
        help="number of panels in sidebar",
        required=False,
    )

    parser.add_argument(
        "-i",
        "--indent",
        type=int,
        default=4,
        help="number of spaces used for indentation in the generated code. If 0, \t is used as indent",
        choices=[0, 1, 2, 3, 4],
        required=False,
    )

    return parser


def main():
    """Run unodit."""

    # parse arguments
    parser = create_parser()
    args = parser.parse_args()

    # normalize path
    args.dir = args.dir.rstrip(os.sep)
    # project directory
    if not os.path.exists(args.dir):
        os.makedirs(args.dir)

    # start logging
    create_logger(LOGGER_NAME, args.dir, LOG_FILE)

    unodit(
        args.mode, args.dir, args.file, args.appname, args.panel, args.indent
    )


if __name__ == "__main__":
    main()
