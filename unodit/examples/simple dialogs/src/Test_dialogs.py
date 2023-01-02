from simple_dialogs import SelectBox, OptionBox, TextBox, NumberBox, DateBox, FolderPathBox, FilePathBox, MessageBox, ActionBox

def xray(myObject):
    try:
        sm = uno.getComponentContext().ServiceManager
        mspf = sm.createInstanceWithContext("com.sun.star.script.provider.MasterScriptProviderFactory", uno.getComponentContext())
        scriptPro = mspf.createScriptProvider("")
        xScript = scriptPro.getScript("vnd.sun.star.script:XrayTool._Main.Xray?language=Basic&location=application")
        xScript.invoke((myObject,), (), ())
        return
    except:
        raise _rtex("Basic library Xray is not installed", uno.getComponentContext())


def Run_Test_dialogs(*args):

    # SelectBox(message="Select one item", title="SelectBox", choices=['a','b','c'])
    # s = SelectBox(message="Select your favorite city", title="My choice", choices=["New York","London", "Paris", "Berlin"])
    # print(s)

    # OptionBox(message="Select multiple items", title="OptionBox", choices=['a','b','c'])
    # o = OptionBox(message="Select one or multiple cities", title="My choices", choices=["New York","London", "Paris", "Berlin"])
    # print(o)

    # TextBox(message="Enter your input", title="TextBox", text="")
    # t = TextBox(message="Enter your e-mail address", title="E-mail")
    # print(t)

    # NumberBox(message="Enter a number", title="NumberBox", default_value=0, min_=-10000, max_=10000, decimals=0)
    # n = NumberBox(message="Year", title="Year of birth", default_value=1999, min_=1950, max_=2020, decimals=0)
    # print(n)

    # DateBox(message="Choose a date", title='DateBox')
    # d = DateBox(message="Date of birth", title="BirthDay")
    # print(d)

    # FolderPathBox(title='Get directory path')
    # fop = FolderPathBox(title='Get directory path')
    # print(fop)

    # FilePathBox(title='Get file path')
    # fip = FilePathBox(title='Get file path')
    # print(fip)

    # MessageBox(message="Message", title="MessageBox")
    # m = MessageBox(message="Message to you Message to you Message to you Message to you Message to you Message to you", title="MessageBox")
    # print(m)

    # ActionBox(message="Message", title="ActionBox")
    a = ActionBox(message="What's Your Decision?", title="ActionBox")
    print(a)


g_exportedScripts = Run_Test_dialogs,
