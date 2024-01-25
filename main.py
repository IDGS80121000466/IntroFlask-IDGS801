from flask import Flask, render_template, request
from flask import Flask, render_template, request, send_from_directory
import os

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

@app.route("/calcular", methods=["GET", "POST"])
def calcular():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La multiplicacion de {} x {} = {}".format(num1, num2, int(num1) * int(num2))
    else:
        return '''
            <form action="/calcular" method="POST">
                <label>N1:</label>
                <input type="text" name="n1"><br>
                <label>N2:</label>
                <input type="text" name="n2"><br>
                <input type="submit"/>
            </form>
        '''
@app.route("/OperasBass")
def operas():
    return render_template("OperasBass.html")

@app.route("/static/bootstrap/css/<path:filename>")
def send_css(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'bootstrap', 'css'), filename, mimetype='text/css')


@app.route("/resultado", methods=["GET", "POST"])
def resul():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        operacion = request.form.get("operacion")

        if operacion == "Suma":
            return "La Suma de {} + {} = {}".format(num1, num2, str(int(num1) + int(num2)))
        elif operacion == "Resta":
            return "La Resta de {} - {} = {}".format(num1, num2, str(int(num1) - int(num2)))
        elif operacion == "Multiplicacion":
            return "La Multiplicacion de {} x {} = {}".format(num1, num2, str(int(num1) * int(num2)))
        elif operacion == "Division":
            if int(num2) != 0:
                return "La Division de {} / {} = {}".format(num1, num2, str(int(num1) // int(num2)))
            else:
                return "Error: No se puede dividir por cero."
        else:
            return "Operación no válida."


if __name__ == "__main__":
    app.run(debug=True)
