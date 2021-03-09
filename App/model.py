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
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.Algorithms.Sorting import quicksort as qui
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog(tipo_list):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'category': None,
               }

    catalog['videos'] = lt.newList(tipo_list,cmpfunction=comparevideos)
    catalog['category'] = lt.newList(tipo_list,cmpfunction=comparecategories)
    return catalog



def comparevideos(id1, id2):
    if (id1.lower() in id2['video_id'].lower()):
        return 0
    return -1

def comparecategories(category1, category):
    if (category1.lower() in category['category_id'].lower()):
        return 0
    return -1



def addVideos(catalog, video):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['videos'], video)

def cmpVideosByViews(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    """
    if (float(video1['views']) > float(video2['views'])):
        return True
    else:
        return False

def n_videos(category_name, country, num_vids, lista):
    contador = 0
    while contador < len(lista):
        elemento = lt.getElement(lista, contador)
        if elemento['country'] == country: 
            contador += 1


def catalogo_shellsort(catalog):
    listas = catalog.copy()
    sa.sort(listas,cmpVideosByViews)


def catalogo_insertionsort(catalog):
    listas = catalog.copy()
    ins.sort(listas, cmpVideosByViews)

def catalogo_selectionsort(catalog):
    listas = catalog.copy()
    sel.sort(listas, cmpVideosByViews)

def catalogo_mergesort(catalog):
    listas = catalog.copy()
    mer.sort(listas, cmpVideosByViews)

def catalogo_quicksort(catalog):
    listas = catalog.copy()
    qui.sort(listas, cmpVideosByViews)








