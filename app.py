#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Meri

import datetime

import flask
from flask import Flask, render_template, request, redirect

from cuenta import Cuenta, MovimientoCuenta
from persona import Persona

# create the application object
app = Flask(__name__)

# definimos configuraciones
app.config['UPLOAD_FOLDER'] = './'
app.config['MAX_CONTENT_PATH'] = 2048


@app.route('/uploader', methods=['POST'])
def uploader_file():
    # TODO: Reemplazar por cada uno de los procesos
    if request.method == 'POST':
        import ipdb;ipdb.set_trace()
        f = request.files['file']
        f.save(f.filename)
        return flask.redirect(flask.url_for('home'), code=302)


@app.route('/proceso')
def proceso():
    return render_template('proceso.html')


@app.route('/')
def home():
    dni = request.args.get('dni')
    # TODO: Reemplazar por obtener Cuenta por dni
    persona_titular = Persona(dni, "Maria Iervasi", datetime.date(1986,7,3))
    cuenta = Cuenta(persona_titular)
    movimiento = MovimientoCuenta(cuenta, "Esta es una descripcion", 1110)
    return render_template('home-banking.html',
                           saludo=persona_titular.dni,
                           movements=[movimiento])


# start the server with the 'run()' method
if __name__ == '__main__':
    # TODO: crear_cuentas
    # TODO: procesar_depositos
    # TODO: procesar_gastos
    # TODO: procesar_transferencias
    app.run(debug=True)
