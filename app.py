from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/<name>')
def home(name):
    #collego la pagina index.html alla richiesta con url "/qualsiasinome settando il nome in content e l'anno"
    return render_template("index.html", content=name, anno=2023)


if __name__ == '__main__':
    app.run()
