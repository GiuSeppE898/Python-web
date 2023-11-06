from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        nome = request.form["nm"]
        cognome = request.form["cm"]
        return redirect(url_for("user", name=nome, surname=cognome))
    else:
        return render_template("login.html")


@app.route("/<name><surname>")
def user(name, surname):
    return f"<h1>{name}{surname}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
