from tkinter import Tk,Button,Frame,messagebox,Entry,Label,font

correoLog = "121037788@upq.edu.mx"
passLog = "mirage"

def mensajeExito():
    messagebox.showinfo("Exito", "Login Exitoso, bienvenido.")
def mensajeError():
    messagebox.showerror("Error", "Error en la autenticacion.")
    
def checkLogin():
    if correoLog == campoCorreo.get() and passLog == campoPass.get():
        return mensajeExito()
    else:
        return mensajeError()

#Instancia ventana principal
ventana = Tk()
ventana.title("Login Empresarial")
ventana.geometry("800x600")
ventana.configure(background="#F3F3F3")

#Agregar Frame
sec1 = Frame(ventana, bg="#DFDFDF")
sec1.pack(expand=True, fill='both')

sec2 = Frame(ventana)
sec2.pack(expand=True, fill="both")

sec3 = Frame(ventana)
sec3.pack(expand=True, fill="both")

#Label de Título
Titulo = Label(sec1,text="Identificate.", fg="Black",bg="#DFDFDF")
Titulo.configure(font=("Verdana",30,"bold"))
Titulo.place(x=250,y=80)

#Agregar Boton
btnLogin = Button(sec3,text="Log In", fg="black", bg="#c0c0c0", command=checkLogin)
btnLogin.place(width=80, height=30, x=350, y=0)

#Agregar campos y texto de campos
txtCorreo = Label(sec2,text="Correo:", fg="Black")
txtCorreo.configure(font=("Verdana"))
txtCorreo.place(x=80,y=77)

campoCorreo = Entry(sec2, bg="#F3F3F3")
campoCorreo.place(x=150, y=80)

txtPass = Label(sec2,text="Contraseña:", fg="Black")
txtPass.configure(font=("Verdana"))
txtPass.place(x=465,y=77)

campoPass = Entry(sec2, bg="#F3F3F3")
campoPass.place(x=575, y=80)
campoPass.configure(show="*")

#Llamar a la ventana principal
ventana.mainloop()