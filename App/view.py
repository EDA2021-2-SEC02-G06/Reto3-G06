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
import time
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import orderedmap as om


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
StartTime = time.process_time()
StopTime = time.process_time()
ElapsedTime = (StopTime - StartTime)*1000
print("Tiempo de ejecución de:  " + str(ElapsedTime) + " mseg")

ufo_file = "UFOS//UFOS-utf8-large.csv"
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
        contados = lt.size(cont["ufos"])
        print("Ufos contados " + str(contados))
        print("")

        ufos = cont["ufos"]
        print("Primeros 5 elementos: ")
        print("")
        q = 0
        while q < 5:

            print(lt.getElement(ufos, q))
            print("")
            print("------------------------------------")
            print("")
            q +=  1

        print("")
        print("**********************************************")
        print("")

        print("Últimos 5 elementos")
        print("")
        y = 0
        z = lt.size(ufos) - 6
       
        while y < 5:

            print(lt.getElement(ufos, z))
            print("")
            print("-----------------------------------------")
            print("")

            z += 1
            y += 1
        
        

    elif int(inputs[0]) == 3:
        StartTime = time.process_time()
        cantidad_arbol_ciudad = om.size(cont["cityIndex"])
        print("Numero de ciudades: " + str(cantidad_arbol_ciudad))
        altura_arbol_ciudad = om.height(cont["cityIndex"])
        print("Altura del arbol ciudades: " + str(altura_arbol_ciudad))
        StopTime = time.process_time()
        ElapsedTime = (StopTime - StartTime)*1000
        print("Tiempo de ejecución de:  " + str(ElapsedTime) + " mseg")

    elif int(inputs[0]) == 4:
        """REQ1"""
        ciudad = input("Que ciudad desea revisar: ")
        print("")
        print("")
        StartTime = time.process_time()
        avistamientos = controller.Avistamientos_Ciudad(cont, ciudad)
        print("Total de avistamientos en la ciudad: " + str(lt.size(avistamientos)))
        print("")
        qqqq = 0
        for ufosss in lt.iterator(avistamientos):

            if qqqq < 3:
                print(ufosss["datetime"] + ("  ") + ufosss["city"] + ("  ") + ufosss["country"] + ("  ") + ufosss["duration (seconds)"] + ("  ") + ufosss["shape"])
                print("-----------------------------------------------------------")        
            qqqq += 1

        print("")
        print("**********************************************")
        print("")

        yyyy = 0
        zzzz = lt.size(avistamientos) - 4
        for ufoss in lt.iterator(avistamientos):

            if yyyy > zzzz:
                print(ufoss["datetime"] + ("  ") + ufoss["city"] + ("  ") + ufoss["country"] + ("  ") + ufoss["duration (seconds)"] + ("  ") + ufoss["shape"])
                print("-----------------------------------------------------------")        
            yyyy += 1
        StopTime = time.process_time()
        ElapsedTime = (StopTime - StartTime)*1000
        print("Tiempo de ejecución de:  " + str(ElapsedTime) + " mseg")
    

    elif int(inputs[0]) == 5:
        """REQ2"""
        menor = round(float((input("Ingrese el primer valor del rango (seg): "))),1)
        mayor = round(float((input("Ingrese el último valor del rango (seg): "))),1)

        StartTime = time.process_time()
        key_maxima = controller.keymaxima(cont["duracionIndex"])
        ufo_maximo =  controller.ufomaxima(cont["duracionIndex"],key_maxima)
        num_ufomax = controller.num_ufomax(ufo_maximo)

        avistamientos,num_avistamientos = controller.reqdos(menor, mayor,cont["duracionIndex"])
        fl = controller.req2fl(avistamientos)

        
        print("============== Req No.2 Datos ===============")
        print("Avistamientos con duración entre " + str(menor) + " y " + str(mayor))
        print(" ")

        print("============ Req No.2 Respuestas ============")
        print("La duración más larga en los avistamientos es de : " + str(key_maxima) + " segundos. Un total de: " + str(num_ufomax) + " avistamiento/s dura/n esto.")
        print(" ")

        print("====================================================================================")
        print("Se registran " + str(num_avistamientos) + " avsitamientos entre los " + str(menor) + " y " + str(mayor) + " segundos de duración.")
        print("Los primeros y últimos tres avistamientos de OVNIS en el rango de duración de segundos son:")
        print(" ")
        
        for i in lt.iterator(fl):
            print(i["datetime"] + " | " + i["city"] + " | " + i["state"] + " | " + i["country"] + " | " + i["shape"] + " | " + i["duration (seconds)"])
            print("====================================================================================")   
        
        StopTime = time.process_time()
        ElapsedTime = (StopTime - StartTime)*1000
        print("Tiempo de ejecución de:  " + str(ElapsedTime) + " mseg")
    
        
        

        

    elif int(inputs[0]) == 6:
        """REQ3"""
        print("")
        lim_inf = input("Ingrese la hora mas baja (mas temprana) que desea buscar: ")
        print("")
        lim_sup = input("Ingrese la hora mas alta (mas tardia) que desea buscar: ")
        print("")
        StartTime = time.process_time()
        lista_horas = controller.Ufos_Hora(lim_inf, lim_sup, cont)
        print("Total de avistamientos en el rango: " + str(lt.size(lista_horas)))
        print("")
        print("")
        
        qqq = 0
        for ufos in lt.iterator(lista_horas):

            if qqq < 3:
                print(ufos["datetime"] + ("  ") + ufos["city"] + ("  ") + ufos["country"] + ("  ") + ufos["duration (seconds)"] + ("  ") + ufos["shape"])
                print("-----------------------------------------------------------")        
            qqq += 1

        print("")
        print("**********************************************")
        print("")

        yyy = 0
        zzz = lt.size(lista_horas) - 4
        for ufos in lt.iterator(lista_horas):

            if yyy > zzz:
                print(ufos["datetime"] + ("  ") + ufos["city"] + ("  ") + ufos["country"] + ("  ") + ufos["duration (seconds)"] + ("  ") + ufos["shape"])
                print("-----------------------------------------------------------")        
            yyy += 1
        
        StopTime = time.process_time()
        ElapsedTime = (StopTime - StartTime)*1000
        print("Tiempo de ejecución de:  " + str(ElapsedTime) + " mseg")
        
    elif int(inputs[0]) == 7:
        """REQ4"""
        print("")
        lim_inf1 = input("Ingrese el día mas bajo (mas antiguo) que desea buscar: ")
        print("")
        lim_sup1 = input("Ingrese el día mas alto (mas moderno) que desea buscar: ")
        print("")
        StartTime = time.process_time()
        lista_fechas = controller.Ufos_Dia(lim_inf1, lim_sup1, cont)
        print("Total de avistamientos en el rango: " + str(lt.size(lista_fechas)))
        print("")
        print("")
        
        q = 0
        for ufos in lt.iterator(lista_fechas):

            if q < 3:
                print(ufos["datetime"] + ("  ") + ufos["city"] + ("  ") + ufos["country"] + ("  ") + ufos["duration (seconds)"] + ("  ") + ufos["shape"])
                print("-----------------------------------------------------------")        
            q += 1

        print("")
        print("**********************************************")
        print("")

        y = 0
        z = lt.size(lista_fechas) - 4
        for ufos in lt.iterator(lista_fechas):

            if y > z:
                print(ufos["datetime"] + ("  ") + ufos["city"] + ("  ") + ufos["country"] + ("  ") + ufos["duration (seconds)"] + ("  ") + ufos["shape"])
                print("-----------------------------------------------------------")        
            y += 1
        
        StopTime = time.process_time()
        ElapsedTime = (StopTime - StartTime)*1000
        print("Tiempo de ejecución de:  " + str(ElapsedTime) + " mseg")

    elif int(inputs[0]) == 8:
        """REQ5"""
        print("")
        print("Para los limites recordar que en cuanto a numeros negativos el menor es el negativo de mayor valor absoluto")
        print("")
        inf_long = float(input("Ingrese el limite inferior de la longitud geografica: "))
        max_long = float(input("Ingrese el limite superior de la longitud geografica: "))
        min_lat = float(input("Ingrese el limite inferior de la latitud geografica: "))
        max_lat = float(input("Ingrese el limite superior de la latitud geografica: "))
        print("")
        print("")
        StartTime = time.process_time()
        obtener_datos = controller.Ufos_Coordenadas(inf_long, max_long, min_lat, max_lat, cont)
        tamaño = lt.size(obtener_datos)
        print("El total de avistamientos dentro del area es: " + str(tamaño))
        print("")
        print("Los primeros 5 avistamientos ordenados por longitud de manera descendente son: ")
        print("")
        ii = 0
        for valores in lt.iterator(obtener_datos):
            if ii < 5:
                print(valores["datetime"] + ("  ") + valores["city"] + ("  ") +  valores["country"] + ("  ") +  valores["shape"] + ("  ") +  valores["duration (seconds)"] + ("  ") +  valores["longitude"] + ("  ") +  valores["latitude"])
                print("-----------------------------------------------------------")        
            else: 
                break
            ii += 1

        print("")
        print("Los ultimos 5 avistamientos ordenados por longitud de manera descendente son: ")
        print("")
        yy = 0
        zz = tamaño - 5
        for valores in lt.iterator(obtener_datos):

            if yy >= zz:
                print(valores["datetime"] + ("  ") + valores["city"] + ("  ") +  valores["country"] + ("  ") +  valores["shape"] + ("  ") +  valores["duration (seconds)"] + ("  ") +  valores["longitude"] + ("  ") +  valores["latitude"])
                print("-----------------------------------------------------------")        
            yy += 1
        
        StopTime = time.process_time()
        ElapsedTime = (StopTime - StartTime)*1000
        print("Tiempo de ejecución de:  " + str(ElapsedTime) + " mseg")




    elif int(inputs[0]) == 9:
        pass

    elif int(inputs[0]) == 0:
        pass

    else:
        sys.exit(0)

sys.exit(0)
