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

#Ejemplo de set para un atributo
heroe.setNombre("Pepe Pecas")

print("")
print("##### Datos Heroe #####")
print("El personaje se llama "+ heroe.getNombre())
print("El personaje es "+ heroe.getEspecie())
print("El personaje tiene una altura de "+ str(heroe.getAltura()))

print("")
print("##### Datos Villano #####")
print("El personaje se llama "+ villano.getNombre())
print("El personaje es "+ villano.getEspecie())
print("El personaje tiene una altura de "+ str(villano.getAltura()))

heroe.correr(True)
heroe.lanzarGranadas()
heroe.recarga(recargaH)

villano.correr(False)
villano.lanzarGranadas()
villano.recarga(recargaV)