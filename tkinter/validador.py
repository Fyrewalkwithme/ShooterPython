from tkinter import messagebox

class validador:
    def __init__(self):
        self.__correE= "123@gmail.com"
        self.__passE= "123"

    def mensajeExito(self):
        messagebox.showinfo("Exito", "Login Exitos, bienvenido.")
    
    def mensajeError(self):
        messagebox.showerror("Error", "Error en la autenticacion.")
    
    def checkfinal(self,c,p):
        if self.__correE == c and self.__passE == p:
            return self.mensajeExito()
        else:
            return self.mensajeError()        
