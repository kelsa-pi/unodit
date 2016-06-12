# unodit
**UNO** **Di**alog **T**ools is a Python3 library (alpha version) that takes a LibreOffice Basic Dialog XML file (.xdl) and:

1. Convert `xdl` file to python (pyuno) code
2. Connect to `xdl` file with python (pyuno) code
3. Convert `xdl` file to python (pyuno) code and embed in document
4. Provides a simple dialog boxes for interaction with a user with python (pyuno)

Other features are:
- if the option `1` or `4` is chosen, it is possible to create a script extension for LibreOffice (oxt file)
- callback functions are created for all button onClick events
- all steps in the conversion process are logged to `log.log` file in project root
- per project customization with ini file (copy `config.ini` in project root)

 
If you have experience with macros, use this library to prepare your python script as extension for LibreOffice or embed in document. Newcomers would benefit from writing macros with simple dialog boxes for interaction with a user.

DISCLAIMER:
I'm not a programmer.
This is a project that targets LibreOffice 5+ and Python3 only.
Tested with Xubuntu 16.04. and LibreOffice 1:5.1.3-0ubuntu1.

##Installation

Place the unodit directory somewhere on your Python path.

##Usage
    python3 ./unodit.py [-f ] [-d] [-a] [-m] [-i]
    
f  - full path to the xdl file

d - full path to the output directory (project root)

a - application name

m - mode

i - number of spaces used for indentation in the generated code. If 0, \t is used as indent

##Customization 
You can copy `config.ini` in your project root directory. Edit section in `my_project_dir/config.ini` file to make changes.

##Examples
Create python project dir `TestLib` in `LIBREOFFICE_PATH/4/user/Scripts/python/`.

Replace `LIBREOFFICE_PATH` with actual path.

###Convert XDL file to python code and create extension

Use parameter `-f` to set the path to any local directory with `xdl` file.

    python3 ./unodit.py -f 'LIBREOFFICE_PATH/4/user/basic/DialogLib/Default.xdl'
                        -d 'LIBREOFFICE_PATH/4/user/Scripts/python/TestLib'
                        -a 'Test_convert'
                        -m 'script_convert'

Available options for parameter -m: `'script_convert'` , `'script_files'` , `'script_oxt'` , `'script_all'`

| Parameter|Description|Note|
|---------|------------|----|
|`'script_convert'`|convert `xdl` file|write your code in `src/MyApp.py`|
|`'script_files'`|create script extension files|change `description.txt`, `title.txt` and `license.txt`|
|`'script_oxt'`|create script extension      |extension file `MyApp_Devel.oxt`|
|`'script_all'`|all in one|convert `xdl` file + create script extension files + script extension|

**Directory structure and parameters**

    TestLib/
            src/
                MyApp.py           script_convert
                pythonpath/
                    MyApp_UI.py   ---------------       
            META-INF/
                manifest.xml
            description/
                description.txt    script_files
                title.txt
            registration/
                license.txt
            Addons.xcu
            description.xml       --------------
            MyApp_Devel.oxt        script_oxt
            
            

###Connect to XDL file with python code

Create dialog in dialog project DialogLib in My Macros (`Tools - Macros - Organize Dialogs - Dialogs - My Dialogs`)
    
    python3 ./unodit.py -f 'LIBREOFFICE_PATH/4/user/basic/DialogLib/Default.xdl'
                        -d 'LIBREOFFICE_PATH/4/user/Scripts/python/TestLib''
                        -a 'Test_connect'
                        -m 'connect'
               
Available options for parameter `-m`: `'connect'`.

`'connect'` - connect to xdl file --> write your code in `my_project/src/MyApp.py`

###Convert XDL file to python code and embed in document

Use parameter `-f` to set the path to any local directory with `xdl` file.
Place odt document in  project dir.

    python3 ./unodit.py -f 'LIBREOFFICE_PATH/4/user/basic/DialogLib/Default.xdl'
                        -d 'LIBREOFFICE_PATH/4/user/Scripts/python/TestLib'
                        -a 'Test_embed'
                        -m 'embed_convert'

Available options for parameter `-m`: `‘embed_convert’`, `‘embed_pack’`, `‘embed_all’`

`‘embed_convert’` - convert `xdl` file --> write your code in `my_project/src/MyApp.py`

`‘embed_pack’` -

`‘embed_all’` -

###Provides a simple dialog boxes for scripts

    python3 ./unodit.py -d 'LIBREOFFICE_PATH/4/user/Scripts/python/TestLib'
                        -a 'Test_dialogs
                        -m 'dialogs_create'
                        
Available options for parameter `-m`: `‘dialogs_create’`, `‘dialogs_files’`, `‘dialogs_oxt’`, `‘dialogs_all’`

`‘dialogs_create’` -  --> write your code in `my_project/src/MyApp.py`

`‘dialogs_files’` - create script extension files

`‘dialogs_oxt’` - create script extension

`‘dialogs_all’` - all in one (create script extension files and script extension)

##Installing an extension

Choose Tools - Extension Manager or command-line:

Ubuntu - `/usr/bin/unopkg add ./MyApp_Devel.oxt`

##Unodit directory structure

    unodit/
        
        pythonpath/                    > submodules dir
            config.py                      > config file
            embed_packer.py                > embed script in ODF file
            extractor.py                   > extract context from ui file
            generator.py                   > code generator
            pyuno_generator.py             > python code generator
            schema.py                      > supported properties
            script_oxt_creator.py          > extension creator
            simple_dialogs.py              > like easygui dialogs
            
        templates/                     > tempaltes dir
            connect/
            convert/
            dialogs/
            embeded/
            script_ext/
        
        config.ini                         > config file
        LICENSE.txt
        README.md
        unodit.py                          > main script


##Similar projects

The following is an incomplete lists of a few projects that share some similarity with `unodit`.

[Gladex](https://launchpad.net/gladex): Gladex is a Python application which takes a .glade file written in the Glade User Interface Builder and generates code in Perl, Python, or Ruby.

[pyuic4](http://pyqt.sourceforge.net/Docs/PyQt4/designer.html#the-uic-module): Convert a .ui file written with Qt Designer into a Python script.

[EasyGUI](https://sourceforge.net/projects/easygui): Very easy GUI programming in Python and Tkinter

[EasyGUI_Qt](https://github.com/aroberge/easygui_qt): Inspired by EasyGUI, designed for PyQt



