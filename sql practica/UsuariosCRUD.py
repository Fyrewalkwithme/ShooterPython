from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorBD import *

# Instanciamos el objeto del controlador
controlador = controladorBD()

#Guardar usando el método del objeto controlador
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(), varCor.get(), varCon.get())

def ejecutaSelectU():
    textBus.delete("1.0",END)
    rsUsuario = controlador.consultaUsuario(varBus.get())
    
    for usu in rsUsuario:
        cadena = str(usu[0]) + "  " + usu[1] + "  " +  usu[2] + "  " + str(usu[3])
        
    if(rsUsuario):
        textBus.insert(tk.END, cadena)
    else:
        messagebox.showwarning("El usuario no existe en la base de datos")

def ejecutaselectT():
    for i in tabla.get_children():
        tabla.delete(i)
        
    rsTotal = (controlador.selectUsuarios())
    for dato in rsTotal:
        tabla.insert('', tk.END, values= dato)
        
def ActualizaReg():
    IDen = varIDA.get()
    Nom = varNomA.get()
    Cor = varCorA.get()
    Con = varConA.get()
    controlador.ActualizaU(IDen,Nom,Cor,Con)
    
def EliminaReg():
    IDen = varIDE.get()
    controlador.EliminarU(IDen)
  
ventana = Tk()
ventana.title("CRUD Usuarios")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand="yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)

#Formulario de Usuarios
titulo = Label(pestana1, text="Registro Usuarios", fg="Blue", font="Lucida 18 bold").pack()

varNom = tk.StringVar()
lblNom = Label(pestana1, text="Nombre: ").pack()
txtNom = Entry(pestana1, textvariable=varNom).pack()

varCor = tk.StringVar()
lblCor = Label(pestana1, text="Correo: ").pack()
txtCor = Entry(pestana1, textvariable=varCor).pack()

varCon = tk.StringVar()
lblCon = Label(pestana1, text="Contraseña: ").pack()
txtCon = Entry(pestana1, textvariable=varCon).pack()

btnGuardar = Button(pestana1, text="Guardar Usuario", command=ejecutaInsert).pack()
#Pestaña 2: Buscar Usuario
titulo2 = Label(pestana2, text="Buscar Usuario", fg="green", font="Lucida 18 bold").pack()

varBus = tk.StringVar()
lblid = Label(pestana2, text="Identificador de Usuario: ").pack()
txtid = Entry(pestana2, textvariable=varBus).pack()

subBus = Label(pestana2, text="Registrado:", fg="blue", font="Lucida 16").pack()
textBus = Text(pestana2, height=2, width=52)
textBus.pack()
btnBusqueda = Button(pestana2, text="Buscar", command=ejecutaSelectU).pack()

#3 Select de todos los usuarios en la tercera pestaña
columnas = ('id','nombre','correo','contra')

tabla = ttk.Treeview(pestana3, columns=columnas, show='headings')
#definir los encabezados

tabla.heading('id', text='Identificador')
tabla.heading('nombre', text='Nombre')
tabla.heading('correo', text='Correo')
tabla.heading('contra',text='Contaseña')
tabla.pack()

btnshow = Button(pestana3, text="Mostrar Registros", command=ejecutaselectT)
btnshow.pack()

#Actualizar un usuario
tituloactu = Label(pestana4,text="Actualizar Registros", fg="Black", font="Lucida 18 bold")
tituloactu.pack()

varIDA = tk.StringVar()
lblIDA = Label(pestana4, text="ID: ").pack()
txtIDA = Entry(pestana4, textvariable=varIDA).pack()

varNomA = tk.StringVar()
lblNomA = Label(pestana4, text="Nombre: ").pack()
txtNomA = Entry(pestana4, textvariable=varNomA).pack()

varCorA = tk.StringVar()
lblCorA = Label(pestana4, text="Correo: ").pack()
txtCorA = Entry(pestana4, textvariable=varCorA).pack()

varConA = tk.StringVar()
lblConA = Label(pestana4, text="Contraseña: ").pack()
txtConA = Entry(pestana4, textvariable=varConA).pack()

btnConfA = Button(pestana4, fg="Black", text="Actualizar", command=ActualizaReg)
btnConfA.pack(pady=8)

#Pestaña para eliminar registros

LblElim = Label(pestana5, text="Eliminar Registros", fg="Black", font="Lucida 18 bold").pack(pady=10)

varIDE = tk.StringVar()
lblIDE = Label(pestana5, text="ID: ").pack(pady=10)
txtIDE = Entry(pestana5, textvariable=varIDE).pack(pady=10)

btnConfE = Button(pestana5, fg="Black", text="Eliminar", command=EliminaReg)
btnConfE.pack(pady=8)

panel.add(pestana1, text="Formulario de Usuarios")
panel.add(pestana2, text="Buscar Usuario")
panel.add(pestana3, text="Consultar Usuarios")
panel.add(pestana4, text="Actualizar Usuario")
panel.add(pestana5, text="Eliminar Registro")

ventana.mainloop()
