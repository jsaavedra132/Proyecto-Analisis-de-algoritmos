from flask import Flask
from flask import render_template
from database import DBHelper

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/registro")
def registro():
    db = DBHelper()
    return render_template('registro.html', db = db)


@app.route("/tipo")
def entrar():
    return render_template('tipo.html')

@app.route("/direccion")
def direccion():
    return render_template('direccion.html')

@app.route("/login")
def login():
    return render_template('login.html')
