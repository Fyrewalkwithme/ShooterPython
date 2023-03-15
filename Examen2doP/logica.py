from tkinter import *
from tkinter import messagebox
import random
import string

class controlador:
    def __init__(self, nombre, paterno, materno, nacimiento, encurso, carrera):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.nacimiento = nacimiento
        self.encurso = encurso
        self.carrera = carrera
    
    def generarPass(self):
        #formato es 3 letras carrera, ultimos 2 nums curso, ultimos 2 nums nacimiento, 1 letra del nombre, 3 primeras letras de ambos apellidos, 3 numeros random
        self.nombreup = str(self.nombre).upper()
        self.paternoup = str(self.paterno).upper()
        self.maternoup = str(self.materno).upper()
        self.carreraup = str(self.carrera).upper()
        
        self.paternogen = self.paternoup[0:3]
        self.maternogen = self.maternoup[0:3]
        self.encursogen = self.encurso[-2:]
        self.nacimientogen = self.nacimiento[-2:] 
        self.carreragen = self.carreraup[0:3]
        self.nombregen = self.nombreup[0]
        
        self.random = random.randint(100,999)
        self.randomgen = str(self.random)
        
        passgenerado = str(self.carreragen +  self.encursogen + self.nacimientogen + self.nombregen + self.paternogen + self.maternogen + self.randomgen)
        msg = messagebox.showinfo("Generación exitosa", "Tu contraseña es: "+ passgenerado)