from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos")
def alumnos_route():
    titulo = "UTL!!!"
    nombres = ["Mario", "Pedro", "Juan", "Angel"]
    return render_template("alumnos.html", titulo=titulo, nombres=nombres)

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")

@app.route("/hola")
def hola():
    return "<h1>Saludos desde Hola </h1>"

@app.route("/saludo")
def saludo():
    return "<h1>Saludos desde Saludo</h1>"

@app.route("/nombre/<string:nom>")
def nombre(nom):
    return "Hola: " + nom

@app.route("/numero/<int:n1>")
def numero(n1):
    return "Numero: {} ".format(n1)

@app.route("/user/<int:id>/<string:nom>")
def func(id, nom):
    return "ID: {} Nombre: {}".format(id, nom)

@app.route("/suma/<float:n1>/<float:n2>")
def func2(n1, n2):
    return "La suma {} + {} ={}".format(n1, n2, n1 + n2)

@app.route("/default")
@app.route("/default/<string:d>")
def func3(d="Dario"):
    return "El nombre de User es: " + d

if __name__ == "__main__":
    app.run(debug=True)
