﻿"""
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
import time
import string


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar tiempo de carga de videos")
    print("3 - Consultar n videos con mas views (requerimiento 1)")
    print("4 - Consultar los videos por categoria")


def initCatalog(b):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(b)

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def loadCategories():
    return controller.loadCategories()

catalog = None

def tamanio_muestra(lst, pos, numelem):
    return lt.subList(lst, pos, numelem)




"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        a = str(input("Elija -CARGAR TODO- o -CARGAR UNA PARTE-"))
        if a == "CARGAR TODO":
            t1 = time.process_time()
            print("Cargando información de los archivos ....")
            b = str(input("elija si quiere LINKED_LIST O ARRAY_LIST"))
            catalog = initCatalog(b)
            loadData(catalog)
            video = lt.firstElement(catalog['videos'])
            print("Videos cargados: ", lt.size(catalog['videos']))
            print("primer video: ", "titulo: ", video["title"]) 
            print("channel_title: ", video['channel_title'])
            print("trending_date: ", video["trending_date"]) 
            print("country: ", video["country"]) 
            print("views: ", video["views"]) 
            print("likes: ", video["likes"]) 
            print("dislikes: ", video["dislikes"])
            print("categorias cargadas: ")
            loadCategories()
            t2 = time.process_time()
            print("El tiempo para ejecutar esta operacion fue de: " +str(t2-t1) + " segundos")

        elif a == "CARGAR UNA PARTE":
            t1 = time.process_time()
            b = str(input("elija si quiere LINKED_LIST O ARRAY_LIST"))
            numero_datos = int(input("Ingrese la cantidad de datos que desea cargar"))
            catalog = initCatalog(b)
            loadData(catalog)

            if numero_datos > lt.size(catalog['videos']):
                print("El número de elementos superó el tamaño de la lista")
            else:
                lista_nueva = tamanio_muestra(catalog['videos'], 1, numero_datos)
                print("Videos cargados: ", lt.size(lista_nueva))
                t2 = time.process_time()
                print("El tiempo para ejecutar esta operacion fue de: " +str(t2-t1) + " segundos")

        else:
            print("Ingrese una opcion valida")


    elif int(inputs[0]) == 2:
        t1 = time.process_time()
        tipo_ordenamiento = str(input("Desea -MERGE- o -QUICK-"))
        if tipo_ordenamiento == 'MERGE':
            controller.mergesort(lista_nueva)

        elif tipo_ordenamiento == 'QUICK':
            controller.quicksort(lista_nueva)

        else: 
            print("Ingrese el nombre de un algoritmo de ordenamiento v")

        t2 = time.process_time()
        print("El tiempo para ejecutar esta operacion fue de: " +str(t2-t1) + " segundos")

    elif int(inputs[0]) == 3:
        t1 = time.process_time()
        catalog = initCatalog("LINKED_LIST")
        loadData(catalog)
        category_name = str(input("ingrese el nombre de la categoria que desea buscar")).translate({ord(c): None for c in string.whitespace})
        country = str(input("ingrese el nombre del pais por el que desea buscar"))
        num_vids = int(input("ingrese el numero de videos que desea listar"))
        requerimiento1 = controller.req1(category_name, country, num_vids, catalog['videos'], loadCategories())
        print(requerimiento1)
        t2 = time.process_time()
        print(t2-t1)

    elif int(inputs[0]) == 4:
        t1 = time.process_time()
        print("aca se ejecutará el requerimiento4")
        t2 = time.process_time()
        print(t2-t1)

    else:
        sys.exit(0)
sys.exit(0)
