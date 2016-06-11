#!/usr/bin/env bash

## path to unodit directory
UNODIT_DIR="/home/sasa/WorkDir/project/unodit"


# ------ path to python test directory -----
PY_DIR="/home/sasa/WorkDir/project/LibreOffice/Test_controls"

# ----- convert ui path -----
CONVERT_UI="/home/sasa/WorkDir/project/unodit/test/Default.xdl"


# ------ connect ui path ----
CONNECT_UI="/home/sasa/.config/libreoffice/4/user/basic/DialogLib/Default.xdl"

# ------ CLEAN START - remove test directory ----
#if [ -d "$PY_DIR" ]; then
#    rm -rfv ${PY_DIR} && mkdir ${PY_DIR}
#fi

# cd in unodit directory
cd ${UNODIT_DIR}

# convert ui file an create exstension
#################################################
# script_convert, script_files, script_oxt, script_all

python3 unodit.py -f ${CONVERT_UI} -d ${PY_DIR} -m 'script_convert'


# connect to ui file
#################################################
# connect

# python3 unodit.py -f ${CONNECT_UI} -d ${PY_DIR} -m 'connect'


# embed dialog in document
#################################################
# embed_convert, embed_pack, embed_all

# python3 unodit.py -f ${CONVERT_UI} -d ${PY_DIR} -m 'embed_all'


# create easy dialogs
#################################################
# dialogs_create, dialogs_files, dialogs_oxt, dialogs_all

# python3 unodit.py -d ${PY_DIR} -m 'dialogs_create'

