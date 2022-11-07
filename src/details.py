#!/usr/bin/env python3

import imp
import os
import memoize

mycache = {}


###############################################################################
@memoize.memoize_with_expiry(mycache, 60)
def importer():
    mods = {}
    pyfiles = [f for f in os.listdir('samplers') if f.endswith('.py')]
    for pyf in pyfiles:
        name = pyf.replace('.py', '')
        mod = imp.load_source(name, os.path.join('samplers', pyf))
        mods[mod.application] = mod
    return mods


###############################################################################
@memoize.memoize_with_expiry(mycache, 60)
def getEnvList():
    mods = importer()
    envs = set()
    for i in mods:
        tmp = mods[i].getDetails()
        for e in tmp:
            envs.add(e['env'])
    return list(envs)


###############################################################################
@memoize.memoize_with_expiry(mycache, 60)
def getAppList():
    mods = importer()
    apps = []
    for i in mods:
        apps.append(mods[i].application)
    return apps


###############################################################################
@memoize.memoize_with_expiry(mycache, 60)
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
@memoize.memoize_with_expiry(mycache, 60)
def getAppDetails(appname, env=None):
    mods = importer()
    for i in mods:
        if i == appname:
            return mods[i].getDetails()


# EOF
