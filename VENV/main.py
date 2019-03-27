from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.security import generate_password_hash, check_password_hash


dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

user_logged = -1

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
    return redirect(url_for('login'))

if __name__ == "__main__":
    db.create_all()
    app.run()

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        hashed_password = generate_password_hash(request.form["contrasena"], method="sha256")
        new_user = Usuarios(usuario=request.form["usuario"], nombre=request.form["nombre"], apellido=request.form["apellido"], contrasena=hashed_password, celular=request.form["celular"], correo=request.form["email"], universidad=request.form["uni"])
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')

    return render_template('registro.html')


@app.route("/tipo")
def tipo():
    if(user_logged<0):
        return redirect(url_for('login'))
    else:
        return render_template("tipo.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    global user_logged
    if request.method == "POST":

        if '@' in request.form['usuario']:
            user =  Usuarios.query.filter_by(correo=request.form["usuario"]).first()
        else:
            user = Usuarios.query.filter_by(usuario=request.form["usuario"]).first()

        if user and check_password_hash(user.contrasena, request.form["contrasena"]): 
            user_logged = user.id
            return redirect(url_for('tipo'))

    return render_template('login.html')

@app.route("/direccion", methods=["GET", "POST"])
def direccion():
    if(user_logged<0):
        return redirect(url_for('login'))
    else:
        return render_template("direccion.html")

    if request.method == "POST":
        new_ruta = Rutas(inicio=request.form["inicio"], medio=request.form["medio"], finruta=request.form["finruta"], hora=request.form["hora"], fecha=request.form["fecha"])
        db.session.add(new_ruta)
        db.session.commit()
        return redirect(url_for('direccion'))

    

@app.route("/usuario")
def usuario():
    if(user_logged<0):
        return redirect(url_for('login'))
    else:
        return render_template("usuario.html")

@app.route("/escogertipo")
def escogertipo():
    if(user_logged<0):
        return redirect(url_for('login'))
    else:
        return render_template("escogertipo.html")
