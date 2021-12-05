#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Meri
import datetime


class Persona(object):

    def __init__(self, dni, nombre, fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.dni = dni

    def __str__(self):
        return f'Nombre: {self.nombre}'

    def mostrar(self):
        print(f"nombre : {self.nombre} edad :{self.edad} dni : {self.dni}")

    @property
    def edad(self):
        hoy = datetime.date.today()
        delta = hoy - self.fecha_nacimiento
        return int(delta.days/365)

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def a_tupla(self):
        return self.nombre, self.fecha_nacimiento, self.dni
