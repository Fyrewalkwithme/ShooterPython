from Personaje import *

#1 Solicitar datos
print("")
print("##### Datos Heroe #####")
especieH = input("Especie: ")
nombreH = input("Nombre: ")
alturaH = float(input("Altura: "))
recargaH = int(input("Cuantas balas a recargar: "))

print("")
print("##### Datos Villano #####")
especieV = input("Especie: ")
nombreV = input("Nombre: ")
alturaV = float(input("Altura: "))
recargaV = int(input("Cuantas balas a recargar: "))

heroe = Personaje(especieH,nombreH,alturaH)
villano = Personaje(especieV,nombreV,alturaV)

print("")
print("##### Datos Heroe #####")
print("El personaje se llama "+ heroe.nombre)
print("El personaje es "+ heroe.especie)
print("El personaje tiene una altura de "+ str(heroe.altura))

print("")
print("##### Datos Villano #####")
print("El personaje se llama "+ villano.nombre)
print("El personaje es "+ villano.especie)
print("El personaje tiene una altura de "+ str(villano.altura))

heroe.correr(True)
heroe.lanzarGranadas()
heroe.recarga(recargaH)

villano.correr(False)
villano.lanzarGranadas()
villano.recarga(recargaV)