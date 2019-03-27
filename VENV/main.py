from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import os



dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    contrasena = db.Column(db.String(80), nullable=False)
    celular = db.Column(db.Integer, nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    universidad = db.Column(db.String(10), nullable=False)

class Rutas(db.Model):
    id_usuario = db.Column(db.String(50), db.ForeignKey("usuarios.id"), primary_key=True)
    inicio = db.Column(db.String(50), nullable=False)
    medio = db.Column(db.String(50), nullable=False)
    finRuta = db.Column(db.String(50), nullable=False)
    hora = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.String(50), nullable=False)

@app.route("/")
def index():
    return render_template('login.html')

if __name__ == "__main__":
    db.create_all()
    app.run()

@app.route("/registro")
def registro():
    return render_template('registro.html')


@app.route("/tipo")
def entrar():
    return render_template('tipo.html')

@app.route("/direccion")
def direccion():
    return render_template('direccion.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/usuario")
def usuario():
    return render_template('usuario.html')
@app.route("/escogertipo")
def escogertipo():
    return render_template('escogertipo.html')
