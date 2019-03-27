#A Partir del fichero JSON movies.json obtener la siguiente información:
import json

#1. Listar información: Listar el título, año y duración de todas las películas.
def listar_info(datos):
    lista = []
    for i in range(0,99):
        lista.append(datos[i]["title"])
        lista.append(datos[i]["year"])
        lista.append(datos[i]["duration"])
        
    info = "\nLista de peliculas: "
    for listapelis in range(0,len(lista),3):
        info = info + "Title: " + str(lista[listapelis]) + "\nAño: " + str(lista[listapelis + 1]) + "\nDuración: " + str(lista[listapelis + 2]).replace("PT","").replace("M"," Min.") + "\n\n"
    return info

#2. Contar información: Mostrar los títulos de las películas y el número de actores/actrices que tiene cada una.s
def contar_info(datos):
    lista = []
    for actor in range(0,99):
        lista.append(datos[actor]["title"])
        
        lista_actor = []
        for actor in datos[actor]["actors"]:
            lista_actor.append(actor)
        lista.append(len(lista_actor))
        
    cad = "--Número de actores en cada pelicula: --\n\n"
    for actor in range(0,len(lista),2):
        cad = cad + str(lista[actor]) + " tiene " + str(lista[actor + 1]) + " actores/actrices. " + "\n\n"
    return cad

#3. Buscar o filtrar información: Mostrar las películas que contengan en la sinopsis dos palabras dadas.
def filtro_info(datos,p1,p2):
    lista = []
    for palabra in range(0,99):
        if str(datos[palabra]["storyline"]).find(p1) != -1 and str(datos[palabra]["storyline"]).find(p2) != -1:
            lista.append(datos[palabra]["title"])
            
    cad =  "Palabras claves [" + p1 + "] [" + p2 + "] de busqueda en la sinopsis :\n\n"
    for palabra in lista:
        cad = cad + "Película realionada -> " + palabra + "\n"
    return cad    
    
with open("movies.json","r") as fichero:
    datos = json.load(fichero)

print ("\n1. Listar información: Listar el título, año y duración de todas las películas. \n")
input("\nPulse Enter para continuar.")
print(listar_info(datos))

print ("\n2. Contar información: Mostrar los títulos de las películas y el número de actores/actrices que tiene cada una. \n")
input("\nPulse Enter para continuar.")
print(contar_info(datos))

print ("\n3. Buscar o filtrar información: Mostrar las películas que contengan en la sinopsis dos palabras dadas. \n")
p1 = str(input("Primera palabra a buscar: "))
p2 = str(input("Segunda palabra a buscar: "))
print(filtro_info(datos,p1,p2))

print ("\n4. Buscar información relacionada: Mostrar las películas en las que ha trabajado un actor dado. \n")

print ("\n5. Ejercicio libre: Mostrar el título y la url del póster de las tres películas con una media de puntuaciones más alta y lanzadas entre dos fechas dadas. \n")
