from tkinter import *
from tkinter import messagebox
class cuenta:
    def __init__(self, s, n, t, e):
        self.saldo = s
        self.numCuenta = n
        self.titular = t
        self.edad = e
    
    saldo = 300
    def consulSaldo(self):
        self.msgSaldo = messagebox.showinfo("Saldo Actual", "Su saldo es de: "+str(self.saldo)+" pesos.")
        
    def ingEfec(self, deposito):
        self.depo = int(deposito)
        self.saldo += self.depo
        self.msgSaldo = messagebox.showinfo("Ingreso Exitoso", "Su saldo es de: "+str(self.saldo)+" pesos.")
        
    def retEfec(self, retiro):
        self.reti = int(retiro)
        self.saldo -= self.reti
        self.msgSaldo = messagebox.showinfo("Ingreso Exitoso", "Su saldo es de: "+str(self.saldo)+" pesos.")