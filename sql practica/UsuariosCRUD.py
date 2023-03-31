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
    
ventana = Tk()
ventana.title("CRUD Usuarios")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand="yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)

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

panel.add(pestana1, text="Formulario de Usuarios")
panel.add(pestana2, text="Buscar Usuario")
panel.add(pestana3, text="Consultar Usuarios")
panel.add(pestana4, text="Actualizar Usuario")

ventana.mainloop()
