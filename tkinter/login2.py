from tkinter import Tk,Button,Frame,Entry,Label,font,messagebox
from validador import *

def getCorreo():
    return __campoCorreo.get()
def getPass():
    return __campoPass.get()
    #Instancia ventana principal
    
    
def check():
    log = validador()
    correo = __campoCorreo.get()
    pass1 = __campoPass.get()
    log.checkfinal(correo,pass1)
    

        
__ventana = Tk()
__ventana.title("Login Empresarial")
__ventana.geometry("800x600")
__ventana.configure(background="#F3F3F3")

    #Agregar Frame
__sec1 = Frame(__ventana, bg="#DFDFDF")
__sec1.pack(expand=True, fill='both')

__sec2 = Frame(__ventana)
__sec2.pack(expand=True, fill="both")

__sec3 = Frame(__ventana)
__sec3.pack(expand=True, fill="both")

    #Label de Título
__Titulo = Label(__sec1,text="Identificate.", fg="Black",bg="#DFDFDF")
__Titulo.configure(font=("Verdana",30,"bold"))
__Titulo.place(x=250,y=80)

    #Agregar Boton
__btnLogin = Button(__sec3,text="Log In", fg="black", bg="#c0c0c0", command=check)
__btnLogin.place(width=80, height=30, x=350, y=0)

    #Agregar campos y texto de campos
__txtCorreo = Label(__sec2,text="Correo:", fg="Black")
__txtCorreo.configure(font=("Verdana"))
__txtCorreo.place(x=80,y=77)

__campoCorreo = Entry(__sec2, bg="#F3F3F3")
__campoCorreo.place(x=150, y=80)

__txtPass = Label(__sec2,text="Contraseña:", fg="Black")
__txtPass.configure(font=("Verdana"))
__txtPass.place(x=465,y=77)

__campoPass = Entry(__sec2, bg="#F3F3F3")
__campoPass.place(x=575, y=80)
__campoPass.configure(show="*")


    #Llamar a la ventana principal
__ventana.mainloop()