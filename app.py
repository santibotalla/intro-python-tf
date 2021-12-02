#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Meri

# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)


# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string


@app.route('/welcome')
def welcome():
    return render_template('welcome.html', saludo="Hola chicas de Ada, este es un saludo",
                           movement="Jueves 2 de Diciembre de 2021. Descripcion del movimiento  $100")


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
