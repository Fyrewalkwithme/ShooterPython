from tkinter import messagebox
import random
import string

class logica:
    
    def __init__(self):
        self
    def generarPassFinal(self, valC, valS, largo):
        self.specialnocap = string.ascii_lowercase + string.punctuation
        self.specialcap = string.printable
        
        if valC == True and valS == True:
            self.password = ''.join(random.sample(string.ascii_lowercase, k=largo))
            self.passBox = messagebox.showinfo("Contraseña Generada", "Tu contraseña es "+ str(self.password))
            return
        else:
            if valC == True and valS == False:
                self.password = ''.join(random.sample(string.ascii_letters, k=largo))
                self.passBox = messagebox.showinfo("Contraseña Generada", "Tu contraseña es "+ str(self.password))
            else:
                if valS == True and valC == False:
                    self.password = ''.join(random.sample(self.specialnocap, k=largo))
                    self.passBox = messagebox.showinfo("Contraseña Generada", "Tu contraseña es "+ str(self.password))
                else:
                    self.password =  ''.join(random.sample(self.specialcap, k=largo))
                    self.passBox = messagebox.showinfo("Contraseña Generada", "Tu contraseña es "+ str(self.password))
                    