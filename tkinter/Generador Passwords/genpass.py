from tkinter import messagebox
import random
import string

class interfaz:
    
    def __init__(self,largo):
        self.caps = True
        self.special = True
        self.length = 10
        self.largo= largo
    
    def generarPassFinal(self):
        self.base = string.ascii_lowercase
        self.caps = string.ascii_letters
        self.specialnocap = string.ascii_lowercase + string.punctuation
        self.specialcap = string.printable
        
        if self.checkValC and self.checkValS == True:
            self.password =  ''.join(random.sample(self.specialcap, self.largo))
            self.passBox = messagebox("Contraseña Generada", "Tu contraseña es "+ str(self.password))
        else:
            if self.checkValC == True:
                self.password = ''.join(random.sample(self.caps, self.largo))
                self.passBox = messagebox("Contraseña Generada", "Tu contraseña es "+ str(self.password))
            else:
                if self.checkValS == True:
                    self.password = ''.join(random.sample(self.specialnocap, self.largo))
                    self.passBox = messagebox("Contraseña Generada", "Tu contraseña es "+ str(self.password))
                else:
                    self.password = ''.join(random.sample(self.base, self.largo))
                    self.passBox = messagebox("Contraseña Generada", "Tu contraseña es "+ str(self.password))