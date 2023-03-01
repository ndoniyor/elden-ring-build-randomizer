import os
from flask import Flask, render_template, redirect, url_for, request

from . import player
from random import choice
import sys

app = Flask(__name__, instance_relative_config=True)
try:
    os.makedirs(app.instance_path)
except OSError:
    pass


@app.route("/", methods=["GET"])
def home_page():
    return render_template("index.html")


@app.route("/randomize", methods=["POST"])
def display():
    p1 = player.Player()
    if "armor_sets" in request.form:
        p1.build_flags.append("armor_sets")
    if "build_flags" in request.form:
        p1.build_flags.append(request.form['build_flags'])
    else:
        p1.build_flags.append(choice(["S","M","I"]))
    p1.choose_all()

    return render_template(
        "index.html",
        player_info=p1,
        checked=True if "armor_sets" in request.form else False,
    )
