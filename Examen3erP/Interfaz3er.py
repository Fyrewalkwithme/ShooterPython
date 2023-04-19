from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador3er import *

control = Controlador3er()

def ejecutarInsert():
    control.guardarMaterial(vNom.get(), vCant.get())

def ejecutaselectT():
    for i in tabla.get_children():
        tabla.delete(i)
        
    result = (control.selectMateriales())
    for dato in result:
        tabla.insert('', tk.END, values= dato)
        
def ActualizaReg():
    ID2 = vID2.get()
    Nom = vNom2.get()
    Cant = vCant2.get()
    control.ActualizaMaterial(ID2,Nom,Cant)

ventana = Tk()
ventana.title("Registro de Materiales - Ferretería")
ventana.geometry("600x350")

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand="yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)

#Interfaz 1 - Insertar

titulop1 = Label(pestana1, text="Insertar Materiales", fg="Black", font="Lucida 18 bold").pack(pady=15)

vNom = tk.StringVar()
labelNom = Label(pestana1, text="Nombre de Material: ").pack()
txtNom = Entry(pestana1, textvariable=vNom).pack()

vCant = tk.StringVar()
labelCor = Label(pestana1, text="Cantidad: ").pack()
txtCor = Entry(pestana1, textvariable=vCant).pack()

btnGuardar = Button(pestana1, text="Guardar Material",command=ejecutarInsert).pack(pady=15)

#Interfaz 2: Consultar todos

columnas = ('id','nombre','cantidad')

titulop2 = Label(pestana2, text="Consultar materiales", fg="Black", font="Lucida 18 bold").pack(pady=10)

tabla = ttk.Treeview(pestana2, columns=columnas, show='headings')

tabla.heading('id', text='Identificador')
tabla.heading('nombre', text='Nombre')
tabla.heading('cantidad', text='Cantidad')
tabla.pack()

btnshow = Button(pestana2, text="Mostrar Materiales",command=ejecutaselectT)
btnshow.pack(pady=15)

#Interfaz 3: Actualizar Material

tituloactu = Label(pestana3,text="Actualizar Registros", fg="Black", font="Lucida 18 bold")
tituloactu.pack()

vID2 = tk.StringVar()
labelID2 = Label(pestana3, text="ID: ").pack()
txtID2 = Entry(pestana3, textvariable=vID2).pack()

vNom2 = tk.StringVar()
labelNom2 = Label(pestana3, text="Nombre de Material: ").pack()
txtNom2 = Entry(pestana3, textvariable=vNom2).pack()

vCant2 = tk.StringVar()
labelCant2 = Label(pestana3, text="Existencia: ").pack()
txtCant2 = Entry(pestana3, textvariable=vCant2).pack()

btnConf = Button(pestana3, fg="Black", text="Actualizar",command=ActualizaReg)
btnConf.pack(pady=10)

panel.add(pestana1, text="Formulario de Materiales")
panel.add(pestana2, text="Consultar Materiales")
panel.add(pestana3, text="Actualizar Registro")

ventana.mainloop()