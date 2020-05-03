# -*- coding: utf-8 -*-
"""
Created on May 03 2020

@authors: Julia Gruber, Max Schlicher, Caroline Steiner, Jelena Zimmermann
"""

import os
import importlib

def auto_install():
    try:
        try:
            importlib.import_module("squarify")
        except ImportError:
            print ("Trying to Install required module: squarify\n")
            os.system('python -m pip install squarify')
            #pip.main(['install', package])
    except ImportError:
        print("install error")
    return