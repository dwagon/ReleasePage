#!/usr/bin/env python

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from details import getDetails, getAppList

app = Flask(__name__)
Bootstrap(app)


###############################################################################
@app.route("/")
def index():
    apps = getAppList()
    return render_template('index.html', apps=apps)


###############################################################################
@app.route("/help")
def help():
    return render_template('help.html')


###############################################################################
@app.route("/app/<appname>")
def appversion(appname):
    details = getDetails(appname)
    return render_template('details.html', app=app, details=details)


###############################################################################
if __name__ == "__main__":
    app.run(debug=True)

# EOF
