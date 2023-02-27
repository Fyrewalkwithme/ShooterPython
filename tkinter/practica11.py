from tkinter import Tk,Button,Frame,messagebox

def mostrarMensajes():
    messagebox.showinfo("shwoinfo", "Presionaste el boton azul")

#1. Instanciamos la ventana wao
ventana = Tk()
ventana.title("Ejemplo de tres Frames")
ventana.geometry("600x400")

# Agregar los frames:
seccion1 = Frame(ventana, bg="crimson")
seccion1.pack(expand = True, fill='both')

seccion2 = Frame(ventana, bg="lavender")
seccion2.pack(expand = True, fill='both')

seccion3 = Frame(ventana, bg = 'orange')
seccion3.pack(expand = True, fill='both')

# Agregamos botones
btnAzul = Button(seccion1,text="Boton Azul",fg="blue",command=mostrarMensajes)
btnAzul.place(x=60,y=60)

btnAmarillo = Button(seccion2, text="Boton Amarillo", fg="white",bg="#ffcf66")
btnAmarillo.grid(row=0, column = 0)

btnNegro= Button(seccion2, text="Boton Negro", fg="white", bg="#242424")
btnNegro.grid(row=1, column=0)

btnVerde= Button(seccion3, text="Boton Verde", fg="white", bg="#49cc54")
btnVerde.configure(width="10", height="5")
btnVerde.pack()


# Llamar al main
ventana.mainloop()