#coding:utf-8

# importar o flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def firstApp():
    return "<h1>Minha primeira Aplicação desenvolvida com Flask!</h1>"

if __name__ == "__main__":
    app.run()
