class Personaje:
    especie = "Humano"
    nombre = "Master Chief"
    altura = "2.70"
    
    def correr(self, sprint):
        if(sprint):
            print("Sprint activado para " + self.nombre)
        else:
            print("Sprint desactivado para " + self.nombre)  
              
    def lanzarGranadas(self):
        print(self.nombre + " lanzo una granada.")
         
    def recarga(self, ammo):
        mag = 10
        mag = mag+ammo
        print(self.nombre + " cargó "+str(ammo)+" balas.")
        print("Municion actual: "+str(mag)+" balas.")
