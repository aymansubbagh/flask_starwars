from flask import Flask, render_template

app = Flask(__name__)

@app.route("/starwars")
def index():
    return render_template("index.html")


@app.route("/cv")
def cv():
    return render_template("cv.html")


@app.route("/starwars/a_new_hope")
def a_new_hope():
    return render_template("a_new_hope.html")


@app.route("/starwars/attack_of_the_clones")
def attack_of_the_clones():
    return render_template("attack_of_the_clones.html")


@app.route("/starwars/return_of_the_jedi")
def return_of_the_jedi():
    return render_template("return_of_the_jedi.html")


@app.route("/starwars/revenge_of_the_sith")
def revenge_of_the_sith():
    return render_template("revenge_of_the_sith.html")


@app.route("/starwars/the_empire_strikes_back")
def the_empire_strikes_back():
    return render_template("the_empire_strikes_back.html")


@app.route("/starwars/the_force_awakens")
def the_force_awakens():
    return render_template("the_force_awakens.html")


@app.route("/starwars/the_last_jedi")
def the_last_jedi():
    return render_template("the_last_jedi.html")


@app.route("/starwars/the_phantom_menace")
def the_phantom_menace():
    return render_template("the_phantom_menace.html")


@app.route("/starwars/the_rise_of_skywalker")
def the_rise_of_skywalker():
    return render_template("the_rise_of_skywalker.html")
