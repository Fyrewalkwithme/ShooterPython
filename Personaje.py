class Personaje:
    
    #Definir constructor de clase
    def __init__(self,esp,nom,alt): 
        self.especie = esp
        self.nombre = nom
        self.altura = alt
    
    #Métodos de clase
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
