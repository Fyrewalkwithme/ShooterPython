class Personaje:
    
    #Definir constructor de clase
    def __init__(self,esp,nom,alt): 
        self.__especie = esp
        self.__nombre = nom
        self.__altura = alt
    
    #Métodos de clase
    def correr(self, sprint):
        if(sprint):
            print("Sprint activado para " + self.__nombre)
        else:
            print("Sprint desactivado para " + self.__nombre)  
              
    def lanzarGranadas(self):
        print(self.__nombre + " lanzo una granada.")
         
    def recarga(self, ammo):
        mag = 10
        mag = mag+ammo
        print(self.__nombre + " cargó "+str(ammo)+" balas.")
        print("Municion actual: "+str(mag)+" balas.")
        
    def pensar(self):
        print("Toy pensando.....")
        
    #definir get y set
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nom):
        self.__nombre = nom
        
    def getEspecie(self):
        return self.__especie
    def setEspecie(self, espe):
        self.__especie = espe
        
    def getAltura(self):
        return self.__altura
    def setAltura(self, altu):
        self.__altura = altu
