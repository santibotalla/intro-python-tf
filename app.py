#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Meri

# import the Flask class from the flask module
from flask import Flask, render_template

from cuenta import Cuenta, MovimientoCuenta
from persona import Persona

# create the application object
app = Flask(__name__)


@app.route('/')
def home():
    persona_titular = Persona("43242342", "Maria Iervasi")
    cuenta = Cuenta(persona_titular)
    movimiento = MovimientoCuenta(cuenta, "Esta es una descripcion", 1110)
    return render_template('home-banking.html',
                           saludo="SALUDO TEST",
                           movement=str(movimiento))  # TODO: proxima clase, esto es una lista


@app.route('/index/ejemplo_vacio')
def ejemplo_vacio():
    return "Esto es lo que devolvemos en index/ejemplo_vacio"


# start the server with the 'run()' method
if __name__ == '__main__':
    # TODO: crear_cuentas
    # TODO: procesar_depositos
    # TODO: procesar_gastos
    # TODO: procesar_transferencias
    app.run(debug=True)
