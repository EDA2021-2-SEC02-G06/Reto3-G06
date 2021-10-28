"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def init():

    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos

def loadData(analyzer, ufo_file):

    ufo_file = cf.data_dir + ufo_file
    input_file = csv.DictReader(open(ufo_file, encoding="utf-8"),
                                                delimiter=",")

    for ufo in input_file:
        model.addUfo(analyzer, ufo)
    return analyzer
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def Avistamientos_Ciudad(cont, ciudad):

    return model.Avistamientos_Ciudad(cont, ciudad)

def Ufos_Hora(lim_inf, lim_sup, cont):

    return model.Ufos_Hora(lim_inf, lim_sup, cont)

def Ufos_Dia(lim_inf1, lim_sup1, cont):

    return model.Ufos_Dia(lim_inf1, lim_sup1, cont)

