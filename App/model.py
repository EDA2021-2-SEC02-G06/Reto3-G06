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
                "hourIndex": None
                }
    
    analyzer["ufos"] = lt.newList("SINGLE_LINKED")
    analyzer["dateIndex"] = om.newMap(omaptype = "RBT",
                                        comparefunction=CmpDates)
    analyzer["cityIndex"] = om.newMap(omaptype = "RBT",
                                        comparefunction=CmpCity)
    analyzer["hourIndex"] = om.newMap(omaptype = "RBT",
                                        comparefunction=CmpCity)
    return analyzer
# Funciones para agregar informacion al catalogo

def addUfo(analyzer, ufo):

    lt.addLast(analyzer["ufos"], ufo)
    updateDateIndex(analyzer["dateIndex"], ufo)
    updateCityIndex(analyzer["cityIndex"], ufo)

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

"""

"""
# Funciones para creacion de datos

# Funciones de consulta

def Avistamientos_Ciudad(cont, ciudad):

    mapa_ciudad = cont["cityIndex"]
    avistamientos = om.get(mapa_ciudad, ciudad)["value"]
    
    r = ms.sort(avistamientos, CmpFechaHoraInvertido)

    q = 0
    for ufos in lt.iterator(avistamientos):

        if q < 3:
            print(ufos["datetime"] + ("  ") + ufos["city"] + ("  ") + ufos["country"] + ("  ") + ufos["duration (seconds)"] + ("  ") + ufos["shape"])
            print("-----------------------------------------------------------")        
        q += 1

    print("")
    print("**********************************************")
    print("")

    y = 0
    z = lt.size(avistamientos) - 4
    for ufos in lt.iterator(avistamientos):

        if y > z:
            print(ufos["datetime"] + ("  ") + ufos["city"] + ("  ") + ufos["country"] + ("  ") + ufos["duration (seconds)"] + ("  ") + ufos["shape"])
            print("-----------------------------------------------------------")        
        y += 1
    

    
    

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
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

    return dt.fromisoformat(ufo1["datetime"]) > dt.fromisoformat(ufo2["datetime"])

def CmpFechaHoraInvertido(ufo1, ufo2):

    return dt.fromisoformat(ufo1["datetime"]) < dt.fromisoformat(ufo2["datetime"])