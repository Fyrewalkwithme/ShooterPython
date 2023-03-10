from tkinter import *
from tkinter import messagebox
from cuenta import *
ventana = Tk()
ventana.title("Caja Popular")
ventana.geometry("300x400")
ventana.configure(bg="#d2fcfc")


def regUsuario():
    s = entrySaldo.get()
    n = entryNumCuenta.get()
    t = entryTitular.get()
    e = entryEdad.get()
    usu = cuenta(s,n,t,e)
    msg = messagebox.showinfo("Registro exitoso", "Te has registrado con exito.")
    
    

sec1 = Frame(ventana, bg="#d2fcfc")
sec1.pack(fill='both',expand=True)
    
    
textoSaldo = Label(sec1,bg="#d2fcfc", fg="Black", font="Lucida 10", text="Saldo Inicial: ")
textoSaldo.place(x="50", y="115")
    
entrySaldo = Entry(sec1, bg="#d2fcfc")
entrySaldo.place(x="135", y="116")   

textoNumCuenta = Label(sec1,bg="#d2fcfc", fg="Black", font="Lucida 10", text="Núm Cuenta: ")
textoNumCuenta.place(x="50", y="135")
    
entryNumCuenta = Entry(sec1, bg="#d2fcfc")
entryNumCuenta.place(x="135", y="136")  

textoTitular = Label(sec1,bg="#d2fcfc", fg="Black", font="Lucida 10", text="Titular: ")
textoTitular.place(x="50", y="155")
    
entryTitular = Entry(sec1, bg="#d2fcfc")
entryTitular.place(x="135", y="156")  

textoEdad = Label(sec1,bg="#d2fcfc", fg="Black", font="Lucida 10", text="Edad: ")
textoEdad.place(x="50", y="175")
    
entryEdad = Entry(sec1, bg="#d2fcfc")
entryEdad.place(x="135", y="176")  

btnConsultar = Button(sec1, bg="white", fg="Black",text="Registrar", command=regUsuario)
btnConsultar.configure(width="16", height="2")
btnConsultar.place(x=140,y=300)

ventana.mainloop()