"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import orderedmap as om


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

ufo_file = "UFOS//UFOS-utf8-small.csv"
cont = None

def printMenu():
    print("\n")
    print("***********************************************************************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar informacion de UFOS")
    print("3- Altura y elementos del arbol ciudades")
    print("4- REQ1: Contar los avistamientos en una ciudad")
    print("5- REQ2: Contar los avistamientos por duración")
    print("6- REQ3: Contar avistamientos por hora/minutos del día")
    print("7- REQ4: Contar los avsitamientos en un rango de fechas")
    print("8- REQ5: Contar los avistamientos de una zona geografica")
    print("9- REQ6: Vizualizar los avistamientos de una zona geografica")
    print("0- Fin del programa")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("\nInicializando. . . .")
        cont = controller.init()
        

    elif int(inputs[0]) == 2:
        print("\nCargando información de los archivos ....")
        controller.loadData(cont, ufo_file)
        print("Datos cargados")
        print("\n")

    elif int(inputs[0]) == 3:
        contados = lt.size(cont["ufos"])
        print("Ufos contados " + str(contados))
        cantidad_arbol_ciudad = om.size(cont["cityIndex"])
        print("Numero de ciudades: " + str(cantidad_arbol_ciudad))
        altura_arbol_ciudad = om.height(cont["cityIndex"])
        print("Altura del arbol ciudades: " + str(altura_arbol_ciudad))

    elif int(inputs[0]) == 4:

        ciudad = input("Que ciudad desea revisar: ")
        print("")
        print("")
        avistamientos = controller.Avistamientos_Ciudad(cont, ciudad)
        
    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        print("")
        lim_inf = input("Ingrese la hora mas baja (mas temprana) que desea buscar: ")
        print("")
        lim_sup = input("Ingrese la hora mas alta (mas tardia) que desea buscar: ")
        print("")
        buscar_rango = controller.Ufos_Hora(lim_inf, lim_sup, cont)
        
    elif int(inputs[0]) == 7:
        pass

    elif int(inputs[0]) == 8:
        pass

    elif int(inputs[0]) == 9:
        pass

    elif int(inputs[0]) == 0:
        pass

    else:
        sys.exit(0)

sys.exit(0)
