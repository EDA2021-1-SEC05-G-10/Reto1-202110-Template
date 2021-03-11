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
from DISClib.DataStructures import listiterator as it
import math


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




def n_videos_by_category(category_name, country, num_vids, lista, categorias)->list:
    resultado = []
    for i in categorias:
        if categorias[i] == category_name:
            numero_categoria = int(i)

    
    iterador = it.newIterator(lista)
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        menor = math.inf
        contador2 = 0
        if (str(elemento['country']) == country) and numero_categoria == int(elemento['category_id']): 
            if len(resultado) < num_vids:
                resultado.append({"trending_date": elemento["trending_date"], "title": elemento["title"], "channel title": elemento["channel_title"], 
                "publish time": elemento["publish_time"], "views": elemento["views"], "likes": elemento["likes"], "dislikes": elemento["dislikes"]})
            else:
                while contador2 < len(resultado):
                    if float(resultado[contador2]["views"]) < menor:
                        menor = float(resultado[contador2]["views"])
                        posicion = contador2
                    contador2 += 1
                if float(elemento['views']) > menor:
                    resultado.pop(posicion)
                    resultado.append({"trending_date": elemento["trending_date"], "title": elemento["title"], "channel title": elemento["channel_title"], 
                    "publish time": elemento["publish_time"], "views": elemento["views"], "likes": elemento["likes"], "dislikes": elemento["dislikes"]})
    return resultado

def n_videos_by_tag(tag, country, num_vids, lista)->list:
    resultado = []
    
    iterador = it.newIterator(lista)
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        menor = math.inf
        contador2 = 0
        if (str(elemento['country']) == country) and str(elemento["tags"]) == tag: 
            if len(resultado) < num_vids:
                resultado.append({"title": elemento["title"], "channel title": elemento["channel_title"], "publish time": elemento["publish_time"], 
                "views": elemento["views"], "likes": elemento["likes"], "dislikes": elemento["dislikes"], "tags": elemento["tags"]})
            else:
                while contador2 < len(resultado):
                    if float(resultado[contador2]["likes"]) < menor:
                        menor = float(resultado[contador2]["likes"])
                        posicion = contador2
                    contador2 += 1
                if float(elemento['likes']) > menor:
                    resultado.pop(posicion)
                    resultado.append({"title": elemento["title"], "channel title": elemento["channel_title"], "publish time": elemento["publish_time"],
                    "views": elemento["views"], "likes": elemento["likes"], "dislikes": elemento["dislikes"], "tags": elemento["tags"]})
    return resultado

def video_trending_pais(country, lista,)->dict:
    mayor = 0 
    aux =[] 
    dict_final = {}      
    iterador = it.newIterator(lista)
    contador2 = 0
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        centinela = True  
        contador = 0     

        if (str(elemento['country'])) == country:
            while contador < len(aux):
                if (elemento['video_id']== aux[contador]["video_id"]):
                    aux[contador]["numero de dias"] += 1
                    centinela = False
                contador +=1

            if centinela == True:
                aux.append({"title": elemento["title"], "channel_title": elemento["channel_title"], 
                "country": elemento["country"], "video_id": elemento["video_id"], "numero de dias": 1})

    while contador2 < len(aux):
        if int(aux[contador2]["numero de dias"]) >= mayor:
            dict_final["title"] = aux[contador2]["title"]
            dict_final["channel_title"] = aux[contador2]["channel_title"]
            dict_final["country"] = country
            dict_final["numero de dias"] = aux[contador2]["numero de dias"]
            mayor = aux[contador2]["numero de dias"]

        contador2 +=1
    return dict_final 

def video_trending_categoria(category_name, lista, categorias)->dict:
    for i in categorias:
        if categorias[i] == category_name:
            numero_categoria = int(i)

    mayor = 0 
    aux =[] 
    dict_final = {}      
    iterador = it.newIterator(lista)
    contador2 = 0
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        centinela = True  
        contador = 0     

        if numero_categoria == int(elemento['category_id']):
            while contador < len(aux):
                if (elemento['title']== aux[contador]["title"]):
                    aux[contador]["numero de dias"] += 1
                    centinela = False
                contador +=1

            if centinela == True:
                aux.append({"title": elemento["title"], "channel_title": elemento["channel_title"], 
                "category_id": elemento["category_id"], "numero de dias": 1, "dates": str(elemento["trending_date"])})

    while contador2 < len(aux):
        if int(aux[contador2]["numero de dias"]) > mayor:
            dict_final["title"] = aux[contador2]["title"]
            dict_final["channel_title"] = aux[contador2]["channel_title"]
            dict_final["category_id"] = numero_categoria
            dict_final["numero de dias"] = aux[contador2]["numero de dias"]
            mayor = int(aux[contador2]["numero de dias"])

        contador2 +=1
    return dict_final








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








