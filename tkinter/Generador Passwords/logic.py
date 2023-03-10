from tkinter import messagebox
import random
import string

class logica:
    
    def __init__(self):
        self.a = 1
    
    def generarPassFinal(self, valC, valS, largo):
        self.base = string.ascii_lowercase
        self.caps = string.ascii_letters
        self.specialnocap = string.ascii_lowercase + string.punctuation
        self.specialcap = string.printable
        
        if valC and valS == False:
            self.password = ''.join(random.sample(self.base, largo))
            self.passBox = messagebox.showinfo("Contraseña Generada", "Tu contraseña es "+ str(self.password))
        else:
            if valC == True and valS == False:
                self.password = ''.join(random.sample(self.caps, largo))
                self.passBox = messagebox.showinfo("Contraseña Generada", "Tu contraseña es "+ str(self.password))
            else:
                if valS == True and valC == False:
                    self.password = ''.join(random.sample(self.specialnocap, largo))
                    self.passBox = messagebox.showinfo("Contraseña Generada", "Tu contraseña es "+ str(self.password))
                else:
                    self.password =  ''.join(random.sample(self.specialcap, largo))
                    self.passBox = messagebox.showinfo("Contraseña Generada", "Tu contraseña es "+ str(self.password))
                    