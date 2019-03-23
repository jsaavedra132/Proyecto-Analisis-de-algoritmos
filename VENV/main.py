from flask import Flask
from flask import render_template
import sqlite3
from flask import g

DATABASE = "C:\Proyecto-Analisis-de-algoritmos\VENV\database.db"

app = Flask(__name__)

@app.route("/")
def index():
    cur = get_db().cursor()
    return render_template('login.html')

@app.route("/registro")
def registro():
    return render_template('registro.html')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()