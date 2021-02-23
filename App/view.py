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
import time


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar views entre dos videos")
    print("3 - Consultar videos por pais")
    print("4 - Consultar los videos por categoria")


def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

catalog = None





"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        t1 = time.process_time()
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print("Videos cargados: ", lt.size(catalog['videos']))
        t2 = time.process_time()
        print("El tiempo para ejecutar esta operacion fue de: " +str(t2-t1) + " segundos")

    elif int(inputs[0]) == 2:
        t1 = time.process_time()
        video1 = ("Ingrese el primer video")
        video2 = ("Ingrese el segundo video")
        print(controller.compararvideos(video1, video2))
        t2 = time.process_time()
        print(t2-t1)

    elif int(inputs[0]) == 3:
        t1 = time.process_time()
        print("aca se ejecutará el requerimiento3")
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
