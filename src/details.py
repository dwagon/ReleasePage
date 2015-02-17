#!/usr/bin/env python

import imp
import os


###############################################################################
def importer():
    mods = {}
    pyfiles = [f for f in os.listdir('samplers') if f.endswith('.py')]
    for pyf in pyfiles:
        name = pyf.replace('.py', '')
        mod = imp.load_source(name, os.path.join('samplers', pyf))
        mods[name] = mod
    return mods


###############################################################################
def getAppList():
    mods = importer()
    apps = []
    for i in mods:
        apps.append(mods[i].application)
    return apps


###############################################################################
def getDetails(appname):
    mods = importer()
    for i in mods:
        if i == appname:
            return mods[i].getRelease()


###############################################################################
if __name__ == "__main__":
    importer()

# EOF
