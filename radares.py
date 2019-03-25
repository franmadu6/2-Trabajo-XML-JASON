#A Partir del fichero XML radares.xml obtener la siguiente información:

from lxml import etree
doc = etree.parse('radares.xml')

#1. Listar información: Mostrar el nombre de las provincias de las que tenemos información sobre radares.
print("\n 1. Listar información: Mostrar el nombre de las provincias de las que tenemos información sobre radares.")

def nombreradar(doc):
    lista = doc.xpath('//NOMBRE/text()')
    return lista

for prov in nombreradar(doc):
    print(prov)
    
input("\nPulse Enter para continuar.")

#2.  Contar información: Mostrar la cantidad de radares de los que tenemos información.
print("\n 2.  Contar información: Mostrar la cantidad de radares de los que tenemos información.")

def contar_radares(doc):
    count = doc.xpath('count(//CARRETERA[DENOMINACION/text()])')
    return int(count)

print("Hay",contar_radares(doc),"radares.")

input("\nPulse Enter para continuar.")

#3.  Buscar o filtrar información: Pedir por teclado una provincia y mostrar el nombre de las carreteras que tiene y la cantidad de radares.
print("\n 3.  Buscar o filtrar información: Pedir por teclado una provincia y mostrar el nombre de las carreteras que tiene y la cantidad de radares.")

def buscarprovincia(doc,radar):
    carr = doc.xpath('//PROVINCIA[NOMBRE/text() = "%s"]/CARRETERA/DENOMINACION/text()'%radar)
    return carr

radar=str(input("\n Dime la Provincia: "))
radar=radar.capitalize()
print("\n Nombre: ",buscarprovincia(doc,radar))

input("\nPulse Enter para continuar.")

#4.  Buscar información relacionada: Pedir por teclado una carretera, muestra las provincias por la que pasa y sus respectivos radares.
print("\n 4.  Buscar información relacionada: Pedir por teclado una carretera, muestra las provincias por la que pasa y sus respectivos radares.")

def buscar_info(doc,denominacion):
    search = doc.xpath('//PROVINCIA[CARRETERA/DENOMINACION/text() = "%s"]/NOMBRE/text()'%denominacion)
    return search

denominacion=str(input("\n Dime una denominación: "))
denominacion=denominacion.upper()
print(buscar_info(doc,denominacion))

input("\nPulse Enter para continuar.")

#5.  Ejercicio libre: Pedir por teclado una carretera, cuenta los radares que tiene y muestra las coordenadas de los radares.(Se puede obtener la URL de OpenStraeetMap para ver donde está el radar).
print("\n5.  Ejercicio libre: Pedir por teclado una carretera, cuenta los radares que tiene y muestra las coordenadas de los radares.(Se puede obtener la URL de OpenStraeetMap para ver donde está el radar).")

print("\nListado de radares\n")
def coordenadas(doc,carretera):
	lista=doc.xpath("//CARRETERA/DENOMINACION/text()")
	indicador=False
	for carreteras in lista:
		if carretera.upper()==carreteras.upper():
			 indicador=True
	if indicador:
		print("Carretera detectada.")
		input("Pulse Enter para continuar.")
		radares=doc.xpath("count(//CARRETERA[DENOMINACION='%s']/RADAR)"%(carretera.upper()))
		print("Hay",int(radares),"radares.")
		LatitudesI=doc.xpath("//CARRETERA[DENOMINACION='%s']/RADAR/PUNTO_INICIAL/LATITUD/text()"%(carretera.upper()))
		LongitudesI=doc.xpath("//CARRETERA[DENOMINACION='%s']/RADAR/PUNTO_INICIAL/LONGITUD/text()"%(carretera.upper()))
		LatitudesF=doc.xpath("//CARRETERA[DENOMINACION='%s']/RADAR/PUNTO_FINAL/LATITUD/text()"%(carretera.upper()))
		LongitudesF=doc.xpath("//CARRETERA[DENOMINACION='%s']/RADAR/PUNTO_FINAL/LONGITUD/text()"%(carretera.upper()))
		for radar in range(0,int(radares)):
			print("Radar",radar,":")
			print("Latitud Inicial:",LatitudesI[radar])
			print("Longitud Inicial:",LongitudesI[radar])
			print("Latitud Final:",LatitudesF[radar])
			print("Longitud Final:",LongitudesF[radar])
			url='https://www.openstreetmap.org/directions?engine=graphhopper_car&route='+LatitudesI[radar]+'%2C'+LongitudesI[radar]+'%3B'+LatitudesF[radar]+'%2C'+LongitudesF[radar]+'#map=12/39.0407/-1.8079&layers=N'
			print(url)

	else:
            print("Esta carretera no esta registrada en la base de datos.")


lista=doc.xpath("//CARRETERA/DENOMINACION/text()")
for carreteras in lista:
    print(carreteras)
carretera=str(input("¿Que carretera buscas? "))
coordenadas(doc,carretera)
