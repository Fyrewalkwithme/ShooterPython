from tkinter import *
from tkinter import messagebox
from cuenta import *

ventana = Tk()
ventana.title("Caja Popular")
ventana.geometry("400x500")
ventana.configure(bg="#d2fcfc")

def regUsuario():
    s = entrySaldo.get()
    n = entryNumCuenta.get()
    t = entryTitular.get()
    e = entryEdad.get()
    usu = cuenta(s,n,t,e)
    msg = messagebox.showinfo("Registro exitoso", "Te has registrado con exito.")
    
usu1 = cuenta(440, 110, "Mauricio H", 20)
usu2 = cuenta(950, 120, "Daniela C", 21)
usu3 = cuenta(1120, 130, "Sara G", 19)
usu4 = cuenta(865, 140, "Sofia R", 21)

listausu = [usu1,usu2,usu3,usu4]

def consultarSaldo():
    usu.consulSaldo()
    
def ingresarEfectivo():
    ing = entryIng.get()
    usu.ingEfec(ing)
    
def retirarEfectivo():
    ret = entryRet.get()
    usu.retEfec(ret)
    
def depositarOtro():
    cant = int(entryOtro.get())
    dest = int(entryDestino.get())
    
    for i in range(0, len(listausu)):
        if i == dest:
            listausu[i].ingEfec(cant)
            msg = messagebox.showinfo("Deposito Exitoso", "Se deposito con exito a la cuenta numero " +str(i))
             
    
sec1 = Frame(ventana, bg="#d2fcfc")
sec1.pack(fill='both',expand=True)
    
textoTop = Label(sec1,bg="#d2fcfc", fg="Black", font="Lucida 18 bold", text="Cuenta - Caja Popular")
textoTop.pack(pady=40)
    
textoDepositar = Label(sec1,bg="#d2fcfc", fg="Black", font="Lucida 10", text="Depositar efectivo:")
textoDepositar.place(x="50", y="115")
    
entryIng = Entry(sec1, bg="#d2fcfc")
entryIng.place(x="165", y="116")                  

btnConsultar = Button(sec1, bg="white", fg="Black",text="Consultar Saldo", command=consultarSaldo)
btnConsultar.configure(width="16", height="2")
btnConsultar.place(x=140,y=400)

btnIngresarEfec = Button(sec1, bg="white", fg="black",text="Depositar", command=ingresarEfectivo)
btnIngresarEfec.place(x= 300, y= 112)

textoRetirar = Label(sec1,bg="#d2fcfc", fg="Black", font="Lucida 10", text="Retirar efectivo:")
textoRetirar.place(x="65", y="155")

entryRet = Entry(sec1, bg="#d2fcfc")
entryRet.place(x="165", y="160")    

btnRetirar = Button(sec1, bg="white", fg="black",text="Retirar", command=retirarEfectivo)
btnRetirar.place(x= 300, y= 160)

textoDepositarOtro = Label(sec1,bg="#d2fcfc", fg="Black", font="Lucida 10", text="Depositar:")
textoDepositarOtro.place(x="95", y="197")

entryOtro = Entry(sec1, bg="#d2fcfc")
entryOtro.place(x="165", y="200") 

textoDestino = Label(sec1,bg="#d2fcfc", fg="Black", font="Lucida 10", text="A la cuenta:")
textoDestino.place(x="85", y="220")

entryDestino = Entry(sec1, bg="#d2fcfc")
entryDestino.place(x="165", y="225")

btnConfirmar = Button(sec1, bg="white", fg="black",text="Confirmar", command=depositarOtro)
btnConfirmar.place(x= 300, y= 225) 

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