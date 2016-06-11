# unodit
unodit is a Python unfinished library that takes a LibreOffice Basic Dialog XML file (XDL) and:

1. Convert XDL file to python code
2. Connect to XDL file with python code
3. Convert XDL file to python code and embed in document
4. Provides a simple dialog box

Other features are:
- if the option 1 or 4 is chosen, it is possible to create a script extension for LibreOffice (oxt file)
- callback functions are created for all button onClick events
- all steps in the conversion process are logged to log.log file in project root
- per project customization with ini file (copy config.ini in project root)

DISCLAIMER: This is a project that targets only LibreOffice 5+. Tested with Xubuntu 16.04. and LibreOffice 1:5.1.3-0ubuntu1.

##Installation

Place the unodit directory somewhere on your Python path

##Usage
    python3 ./unodit.py [-f ] [-d] [-a] [-m] [-i]
    
f  - full path to the xdl file

d - full path to the output directory (project root)

a - application name

m - mode

i - number of spaces used for indentation in the generated code. If 0, \t is used as indent
