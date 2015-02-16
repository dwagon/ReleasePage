#!/usr/bin/env python

from flask import Flask, render_template
from details import getDetails
app = Flask(__name__)


###############################################################################
@app.route("/")
def index():
    apps = getAppList()
    return render_template('index.html', apps=apps)


###############################################################################
def getAppList():
    """ Get the list of apps we can return details on """
    return ['soe']  # STUB


###############################################################################
@app.route("/app/<appname>")
def appversion(appname):
    details = getDetails(appname)
    return render_template('details.html', app=app, details=details)


###############################################################################
if __name__ == "__main__":
    app.run()

# EOF
