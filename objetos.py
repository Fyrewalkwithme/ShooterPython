from Personaje import *

heroe = Personaje()

print("El personaje se llama "+ heroe.nombre)
print("El personaje es "+ heroe.especie)
print("El personaje tiene una altura de "+ heroe.altura)

heroe.correr(True)
heroe.lanzarGranadas()
heroe.recarga(15) 