from tkinter import *
from tkinter import messagebox
import random
import string
from logic import *

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

def generarPass():
    log = logica()
    largo = int(entryLargo.get())
    log.generarPassFinal(ValC, ValS, largo)                  
 
ValC = BooleanVar
checkboxCaps = Checkbutton(sec1,variable=ValC, onvalue=True, offvalue=False, text="Mayúsculas?",bg="#feff9c",fg="Black",font="Lucida 13")
checkboxCaps.place(x=140,y=190)

ValS = BooleanVar
checkboxSpecial = Checkbutton(sec1,variable=ValS, onvalue=True, offvalue=False, text="Car. Especiales?",bg="#feff9c",fg="Black",font="Lucida 13")
checkboxSpecial.place(x=127,y=220)
    
btnGenerar = Button(sec1, bg="#cdff9c", fg="Black",text="Generar", command=generarPass)
btnGenerar.configure(width="13", height="2")

btnGenerar.place(x=155,y=290)
ventana.mainloop()

       

 
        
