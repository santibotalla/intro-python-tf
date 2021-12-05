#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Meri
import csv


def guardar_cuentas(cuentas):
    """
    param cuentas: es un diccionario
    :return: None
    """
    # convertir desde el diccionario cuentas a una lista de tuplas
    lista_de_tuplas = [('nro_de_cuenta', 'titular', 'saldo', 'activa')]
    for elemento in cuentas:
        lista_de_tuplas.append(tuple(elemento.values()))
    archivo = open("cuentas.csv", "w", newline='')
    archivo_csv = csv.writer(archivo)
    archivo_csv.writerows(lista_de_tuplas)
    archivo.close()


def crear_cuentas():
    """
    param: None
    :return: Lista de diccionarios
    """
    cuentas = []
    archivo = open("personas.csv", "r")
    archivo_csv = csv.reader(archivo)
    titulos = next(csv_reader)
    # TODO
    archivo.close()
    return cuentas