from tkinter import *
from tkinter import messagebox
from logica import *

ventana = Tk()
ventana.title("Generador Matrícula")
ventana.geometry("400x500")
ventana.configure(bg="#ededeb")

sec1 = Frame(ventana, bg="#ededeb")
sec1.pack(fill='both',expand=True)

def genPass():
    nombre = entryNom.get()
    paterno = entryAP.get()
    materno = entryAM.get()
    nace = entryNace.get()
    encurso = entryACurso.get()
    carrera = entryCarr.get()
    
    generador = controlador(nombre, paterno, materno, nace, encurso, carrera)
    
    generador.generarPass()

textTitulo = Label(sec1, fg="Black", font="Lucida 20 bold", text="Datos Matrícula.")
textTitulo.pack(pady=40)

textoNom = Label(sec1, fg="Black", font="Lucida 10", text="Nombre:")
textoNom.place(x="90", y="120")
entryNom = Entry(sec1, bg="white")
entryNom.place(x="155", y="120")

textoAP = Label(sec1, fg="Black", font="Lucida 10", text="Apellido Paterno:")
textoAP.place(x="45", y="160")
entryAP = Entry(sec1, bg="white")
entryAP.place(x="155", y="160")

textoAM = Label(sec1, fg="Black", font="Lucida 10", text="Apellido Materno:")
textoAM.place(x="40", y="200")
entryAM = Entry(sec1, bg="white")
entryAM.place(x="155", y="200")

textoNace = Label(sec1, fg="Black", font="Lucida 10", text="Año de Nacimiento:")
textoNace.place(x="30", y="240")
entryNace = Entry(sec1, bg="white")
entryNace.place(x="155", y="240")

textoACurso = Label(sec1, fg="Black", font="Lucida 10", text="Año en Curso:")
textoACurso.place(x="60", y="280")
entryACurso = Entry(sec1, bg="white")
entryACurso.place(x="155", y="280")

textoCarr = Label(sec1, fg="Black", font="Lucida 10", text="Carrera:")
textoCarr.place(x="90", y="320")
entryCarr = Entry(sec1, bg="white")
entryCarr.place(x="155", y="320")

btnConfirmar = Button(sec1, bg="white", fg="black",text="Confirmar", command=genPass)
btnConfirmar.place(x= 175, y= 380) 

ventana.mainloop()