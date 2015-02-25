#!/usr/bin/env python

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from details import getAppDetails, getEnvDetails, getAppList, getEnvList

app = Flask(__name__)
Bootstrap(app)


###############################################################################
@app.route("/")
def index():
    apps = getAppList()
    envs = getEnvList()
    return render_template('index.html', apps=apps, envs=envs)


###############################################################################
@app.route("/help")
def help():
    return render_template('help.html')


###############################################################################
@app.route("/app/<appname>")
def appversion(appname):
    details = getAppDetails(appname)
    return render_template('appdetails.html', app=appname, details=details)


###############################################################################
@app.route("/env/<envname>")
def envview(envname):
    details = getEnvDetails(envname)
    return render_template('envdetails.html', env=envname, details=details)


###############################################################################
if __name__ == "__main__":
    app.run(debug=True)

# EOF
