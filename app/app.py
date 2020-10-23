#./app/app.py
from markupsafe import escape
from flask import ( Flask, url_for, redirect)

import ej2 as ej2
import ej3 as ej3
import ej4 as ej4
import ej5 as ej5
import ej6 as ej6
import ejNota as ejNota

app = Flask(__name__)

"""
@app.route('/')
def hello_world():
    return 'Hello, World!'
"""
@app.route('/usuario')
def hello():
    return 'Hello, Antonio'

@app.route('/usuario/<username>')
def show_user_profile(username):
    return 'User %s' % escape(username)

# Ejercicio 2
@app.route('/ordena/<lista>')
def ejercicio2(lista):
  return ej2.ordena(lista)

# Ejercicio 3
@app.route('/criba/<int:n>')
def ejercicio3(n):
  return ej3.CribadeEratóstenes(n)

# Ejercicio 4
@app.route('/fibonacci/')
def ejercicio4():
    num = ej4.leerFichero()
    ej4.escribirFichero(num)
    solucion = '<h1>SUCESIÓN DE FIBONACCI</h1><p>'
    solucion += str(ej4.fib(num))
    solucion += '</p>'
    return solucion

# Ejercicio 5
@app.route('/balanceo/')
def balanceo():
    solucion = '<h2> Generamos la cadena aleatorio </h2>'
    cadenaAleatoria = ej5.generarCadenaAleatoria()
    solucion += '<p>' + cadenaAleatoria + '</p>'
    solucion += '<h2>' + ej5.comprobarBalanceo(cadenaAleatoria) + '</h2>'
    return solucion

#Ejercicio 6
@app.route('/palabra+mayuscula/<cadena>')
def palabraMayuscula(cadena):
    solucion = '<h2> La palabra introducida es: ' + cadena + '</h2>'
    if ej6.palabrayMayuscula(cadena):
        solucion += "<p>la palabra es mayusucla</p>"
    else:
        solucion += "<p>la palabra no esta en mayusucla</p>"
    return solucion
@app.route('/correo/<cadena>')
def correoElectronicoValido(cadena):
    solucion = '<h2> El correo introducio es: ' + cadena + '</h2>'
    if ej6.correoValido(cadena):
        solucion += "<p>Correo aceptado</p>"
    else:
        solucion += "<p>Este correo electrónico no es valido</p>"
    return solucion

@app.route('/tarjetaCredito/<cadena>')
def tarjeraCreditoAceptada(cadena):
    solucion = '<h2> La tarjeta de credito es: ' + cadena + '</h2>'
    if ej6.tarjetaCredito(cadena):
        solucion += "<p>Tarjeta de crédito aceptada</p>"
    else:
        solucion += "<p>Este tarjeta de crédito no es correcta</p>"
    return solucion

# Hacer lo de static
@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

# En caso de error
@app.errorhandler(404)
def error(error):
    return 'Error. Sitio no encontrado.'

# Subir nota
@app.route('/ejercicioParaNota/')
def random_svg():
    cadena = ejNota.svg()
    return cadena