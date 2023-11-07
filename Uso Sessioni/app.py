from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)  # Per quanto tempo conserva i dati di sessione


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():

    if request.method == "POST":
        session.permanent = True                  # la sessione è permanente
        usern = request.form["nm"]              # acquisisce dal form il valore di nm
        userc = request.form["cg"]              # acquisisce dal form il valore di cg
        session["user"] = usern
        session["userc"] = userc

        return redirect(url_for("user"))
    else:                                        # la richiesta è di tipo get
        if "user" in session:                    # se l'utente è in sessione
            return redirect(url_for("user"))     # redirect alla pagina user

        return render_template("login.html")     # redirect al login


@app.route("/user")
def user():
    if "user" in session:
        usern = session["user"]
        userc = session["userc"]
        return f"<h1>{usern} {userc}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)
