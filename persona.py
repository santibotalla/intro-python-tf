#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Meri

import datetime

from cuenta import Cuenta


def convertir_fecha(string_fecha):
    # TODO: que pasa si la fecha no tiene los 10 caracteres esperados?
    anio = string_fecha[0:4]
    mes = string_fecha[5:7]
    dia = string_fecha[8:10]
    return datetime.date(int(anio), int(mes), int(dia))


class Persona(object):
    def __init__(self, dni, nombre, str_fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = convertir_fecha(str_fecha_nacimiento)
        self.dni = dni
        self.cuentas = []

    def __str__(self):
        return f'Nombre: {self.nombre}'

    @property
    def edad(self):
        hoy = datetime.date.today()
        delta = hoy - self.fecha_nacimiento
        return int(delta.days/365)

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def crear_cuenta(self):
        # TODO: Segun la edad, debería crear Cuenta o CuentaJoven()
        cuenta = Cuenta()
        self.cuentas.append(cuenta)

    def obtener_todos_los_movimientos(self):
        todos_los_movimientos = []
        for cuenta in self.cuentas:
            todos_los_movimientos += cuenta.movimientos
        return todos_los_movimientos

    def saludo(self):
        # TODO: Saludo que indique hora fecha y clima
        return f"Persona saludando {self.nombre}"
