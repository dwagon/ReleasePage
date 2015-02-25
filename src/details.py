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
        mods[mod.application] = mod
    return mods


###############################################################################
def getEnvList():
    return ['prod', 'preprod']


###############################################################################
def getAppList():
    mods = importer()
    apps = []
    for i in mods:
        apps.append(mods[i].application)
    return apps


###############################################################################
def getEnvDetails(envname):
    mods = importer()
    ans = []
    for i in mods:
        tmp = mods[i].getDetails(env=envname)
        for e in tmp:
            if e['env'] == envname:
                e['appname'] = i
                ans.append(e)
    return ans


###############################################################################
def getAppDetails(appname, env=None):
    mods = importer()
    for i in mods:
        if i == appname:
            return mods[i].getDetails()


###############################################################################
if __name__ == "__main__":
    importer()

# EOF
