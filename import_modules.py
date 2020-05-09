#being used for calling operating system calls
import os
#being used for importing modules
import importlib

def auto_install():
    try:
        try:
            #trying to import the given module
            importlib.import_module("squarify")
        except ImportError:
            #in case the module has not been installed, it will now
            #   be installed
            print ("Trying to Install required module: squarify\n")
            os.system('python -m pip install squarify')
    except ImportError:
        print("install error")
    return
