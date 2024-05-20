import re
from datetime import datetime
import os.path

from flask import Flask
from flask import render_template
from flask import abort
from flask import redirect

from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def web_home():
    return render_template("home.html")

@app.route("/portfolio")
def web_portfolio():
    return render_template("portfolio.html")

@app.route("/contact")
def web_contact():
    return render_template("contact.html")

@app.route("/blog/<title>")
def web_blog(title):
    title = secure_filename(title)

    if os.path.isfile("templates/blog/" + title + ".html"):
        return render_template("/blog/" + title + ".html")
    
    abort(404)

#~~~~~~~~~~~~~~~~~~
# Redirect old URLS
#~~~~~~~~~~~~~~~~~~

@app.route("/ewelborn/")
@app.route("/ewelborn/<a>")
@app.route("/ewelborn/<a>/<b>")
def web_old_pages(a = "", b = ""):
    a = secure_filename(a)
    b = secure_filename(b)

    if a == "":
        return redirect("/")
    elif a == "academic":
        return redirect("/")
    elif a == "portfolio":
        return redirect("/portfolio")
    elif a == "contact":
        return redirect("/contact")
    elif a == "article":
        return redirect("/blog/" + b)
    else:
        return redirect("/")