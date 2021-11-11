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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import addLast
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
from datetime import datetime as dt
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newAnalyzer():

    analyzer = {"ufos": None,
                "dateIndex": None,
                "cityIndex": None,
                "hourIndex": None,
                "placeIndex": None
                }
    
    analyzer["ufos"] = lt.newList("SINGLE_LINKED")
    analyzer["dateIndex"] = om.newMap(omaptype = "RBT",
                                        comparefunction=CmpDates)
    analyzer["cityIndex"] = om.newMap(omaptype = "RBT",
                                        comparefunction=CmpCity)
    analyzer["hourIndex"] = om.newMap(omaptype = "RBT",
                                        comparefunction=CmpHour)
    analyzer["duracionIndex"] = om.newMap(omaptype = "RBT",
                                        comparefunction=CmpHour)
    analyzer["placeIndex"] = om.newMap(omaptype = "RBT",
                                        comparefunction=CmpPlace)

    return analyzer
# Funciones para agregar informacion al catalogo

def addUfo(analyzer, ufo):

    lt.addLast(analyzer["ufos"], ufo)
    updateDateIndex(analyzer["dateIndex"], ufo)
    updateCityIndex(analyzer["cityIndex"], ufo)
    updateHourIndex(analyzer["hourIndex"], ufo)
    updateDuracionIndex(analyzer["duracionIndex"],ufo)
    updatePlaceIndex(analyzer["placeIndex"], ufo)

    return analyzer

def updateDateIndex(map, ufo):

    ocurred_date = ufo["datetime"]
    ufo_date = dt.strptime(ocurred_date, "%Y-%m-%d %H:%M:%S")
    entry = om.get(map, ufo_date.date())

    if entry is None:
        lista_ufos = lt.newList("ARRAY_LIST")
        lt.addLast(lista_ufos, ufo)
        date_entry = lista_ufos
        om.put(map, ufo_date.date(), date_entry)
    else:
        date_entry = me.getValue(entry)
        lt.addLast(date_entry, ufo)
        me.setValue(entry, date_entry)

    return map

def updateCityIndex(map, ufo):

    ocurred_city = ufo["city"]
    entry = om.get(map, ocurred_city)

    if entry is None:
        lista_ufos = lt.newList("ARRAY_LIST")
        lt.addLast(lista_ufos, ufo)
        city_entry = lista_ufos
        om.put(map, ocurred_city, city_entry)
    else:
        city_entry = me.getValue(entry)
        lt.addLast(city_entry, ufo)
        me.setValue(entry, city_entry)

    return map

def updateHourIndex(map, ufo):

    ocurred_date = ufo["datetime"]
    ocurred_date = ocurred_date[0: 16]
    ufo_date = dt.strptime(ocurred_date, "%Y-%m-%d %H:%M")
    entry = om.get(map, ufo_date.time())

    if entry is None:
        lista_ufos = lt.newList("ARRAY_LIST")
        lt.addLast(lista_ufos, ufo)
        date_entry = lista_ufos
        om.put(map, ufo_date.time(), date_entry)
    else:
        date_entry = me.getValue(entry)
        lt.addLast(date_entry, ufo)
        me.setValue(entry, date_entry)

    return map
def updateDuracionIndex(map, ufo):

    duracion = round((float(ufo["duration (seconds)"])),1)
    entry = om.get(map, duracion)

    if entry is None:
        lista_ufos = lt.newList("ARRAY_LIST")
        lt.addLast(lista_ufos, ufo)
        city_entry = lista_ufos
        om.put(map, duracion, city_entry)
    else:
        city_entry = me.getValue(entry)
        lt.addLast(city_entry, ufo)
        me.setValue(entry, city_entry)

def updatePlaceIndex(map, ufo):

    ocurred_place = ufo["longitude"]
    ufo_place = round(float(ocurred_place), 2) 
    entry = om.get(map, ufo_place)

    if entry is None:
        lista_ufos = lt.newList("ARRAY_LIST")
        lt.addLast(lista_ufos, ufo)
        place_entry = lista_ufos
        om.put(map, ufo_place, place_entry)
    else:
        place_entry = me.getValue(entry)
        lt.addLast(place_entry, ufo)
        me.setValue(entry, place_entry)

"""

"""
# Funciones para creacion de datos

# Funciones de consulta

def Avistamientos_Ciudad(cont, ciudad):

    mapa_ciudad = cont["cityIndex"]
    avistamientos = om.get(mapa_ciudad, ciudad)["value"]
    
    r = ms.sort(avistamientos, CmpFechaHoraInvertido)

    

    return avistamientos

def Ufos_Hora(lim_inf, lim_sup, cont):

    hora_inf = dt.strptime(lim_inf, "%H:%M")
    hora_sup = dt.strptime(lim_sup, "%H:%M")
    mapa_hora = cont["hourIndex"]

    valores = om.values(mapa_hora, hora_inf.time(), hora_sup.time())

    lista_horas = lt.newList("ARRAY_LIST")

    for valor in lt.iterator(valores):

        for val in lt.iterator(valor):

            lt.addLast(lista_horas, val)
    

    return lista_horas

def Ufos_Dia(lim_inf1, lim_sup1, cont):

    fecha_inf = dt.strptime(lim_inf1, "%Y-%m-%d")
    fecha_sup = dt.strptime(lim_sup1, "%Y-%m-%d")
    mapa_fecha = cont["dateIndex"]

    valores = om.values(mapa_fecha, fecha_inf.date(), fecha_sup.date())

    lista_fechas = lt.newList("ARRAY_LIST")

    for valor in lt.iterator(valores):

        for val in lt.iterator(valor):

            lt.addLast(lista_fechas, val)
            


    return lista_fechas

def reqdos(minimo,mayor,cont):

    rango = om.values(cont,minimo,mayor)
    num = 0
    lista = lt.newList("ARRAY_LIST")
    for i in lt.iterator(rango):
        tamaño = lt.size(i)
        num += tamaño
        for ufo in lt.iterator(i):
            lt.addLast(lista,ufo)
    lista_ord = sa.sort(lista,CmpUfoByDuration)
    return lista_ord,num

def req2fl(lista):
    contador = 0
    contador_dos = lt.size(lista) - 3
    nueva_lista = lt.newList("ARRAY_LIST")

    for i in lt.iterator(lista):
        if contador < 3:
            lt.addFirst(nueva_lista,i)
        if contador >= contador_dos:
            lt.addLast(nueva_lista,i)
        contador += 1
    return nueva_lista

def keymaxima(arbol):

    return om.maxKey(arbol)

def ufomaxima(arbol,llave):

    return om.get(arbol,llave)

def num_ufomax(lista):

    return lt.size(lista["value"])

def Ufos_Coordenadas(inf_long, max_long, min_lat, max_lat, cont):

    mapa_lugar = cont["placeIndex"]
    #print(mapa_lugar)
    #print(inf_long, max_long)
    valores = om.values(mapa_lugar, inf_long, max_long)
    #value = om.get(mapa_lugar, inf_long)
    lista_lugares_1 = lt.newList("ARRAY_LIST")

    for valor in lt.iterator(valores):

        for val in lt.iterator(valor):

            lt.addLast(lista_lugares_1, val)
    
    #print(valores)
    r = ms.sort(lista_lugares_1, CmpLat)

    lista_lugares2 = lt.newList("ARRAY_LIST")

    for ufos in lt.iterator(lista_lugares_1):
        latitud = round(float(ufos["latitude"]), 2)
        if latitud <= max_lat and latitud >= min_lat:
            lt.addLast(lista_lugares2, ufos)
    
    return lista_lugares2
    
    

# Funciones utilizadas para comparar elementos dentro de una lista

def CmpDates(date1, date2):

    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def CmpCity(city1, city2):

    if (city1 == city2):
        return 0
    elif (city1 > city2):
        return 1
    else:
        return -1

def CmpFechaHora(ufo1, ufo2):

    
    ufo_date = dt.strptime(ufo1["datetime"], "%Y-%m-%d %H:%M")

    return dt.fromisoformat(ufo1["datetime"]) < dt.fromisoformat(ufo2["datetime"])

def CmpFechaHoraInvertido(ufo1, ufo2):

    return dt.fromisoformat(ufo1["datetime"]) < dt.fromisoformat(ufo2["datetime"])

def CmpHour(hour1, hour2):

    if (hour1 == hour2):
        return 0
    elif (hour1 > hour2):
        return 1
    else:
        return -1

def CmpUfoByDuration(ufo1, ufo2):
    """
    Devuelve verdadero (True) si el 'Date' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    return float(ufo1["duration (seconds)"]) < float(ufo2["duration (seconds)"])

def CmpPlace(ufo1, ufo2):

    hour1 = round(float(ufo1), 2)
    hour2 = round(float(ufo2), 2)

    if (hour1 == hour2):
        return 0
    elif (hour1 > hour2):
        return 1
    else:
        return -1

def CmpLat(ufo1, ufo2):

    hour1  = round(float(ufo1["latitude"]), 2)
    hour2 = round(float(ufo2["latitude"]), 2)

    if (hour1 == hour2):
        return 0
    elif (hour1 > hour2):
        return 1
    else:
        return -1

# Funciones de ordenamiento


