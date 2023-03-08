from tkinter import *
from tkinter import messagebox
import random
import string
class interfaz:
    
    def __init__(self):
        self.caps = True
        self.special = True
        self.length = 10
        
    def getLargo(self):
        return self.largo
    
    largo2 = int(getLargo())
    
    def generarPass(self):
        self.base = string.ascii_lowercase
        self.caps = string.ascii_letters
        self.specialnocap = string.ascii_lowercase + string.punctuation
        self.specialcap = string.printable
        
        if self.checkValC and self.checkValS == True:
            self.password =  ''.join(random.sample(self.specialcap, self.largo2))
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
                    
    
    ventana = Tk()
    ventana.title("")
    ventana.geometry("400x400")
    ventana.configure(bg="#feff9c")
    
    sec1 = Frame(ventana, bg="#feff9c")
    sec1.pack(fill='both',expand=True)
    
    textoTop = Label(sec1,bg="#feff9c", fg="Black", font="Lucida 20 bold", text="Generador de Contraseñas")
    textoTop.pack(pady=50)
    
    textoLargo = Label(sec1,bg="#feff9c", fg="Black", font="Lucida 12", text="Largo:")
    textoLargo.place(x="175", y="115")
    
    entryLargo = Entry(sec1, bg="#cdff9c")
    entryLargo.place(x="142", y="145")
    largo = entryLargo.get()
    
    checkboxCaps = Checkbutton(sec1,text="Mayúsculas?",bg="#feff9c",fg="Black",font="Lucida 13")
    checkValC = BooleanVar(checkboxCaps)
    checkboxCaps.place(x=140,y=190)
    
    checkboxSpecial = Checkbutton(sec1,text="Car. Especiales?",bg="#feff9c",fg="Black",font="Lucida 13")
    checkValS = BooleanVar(checkboxSpecial)
    checkboxSpecial.place(x=127,y=220)
    
    btnGenerar = Button(sec1, bg="#cdff9c", fg="Black",text="Generar", command=generarPass)
    btnGenerar.configure(width="13", height="2")
    btnGenerar.place(x=155,y=290)
    ventana.mainloop()
        
