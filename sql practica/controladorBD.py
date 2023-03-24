from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def __init__(self):
        pass
    
    def conexionBD(self):
        #1 Preparar la conexión para usarla cuando se necesite
        try:
            conexion= sqlite3.connect("C:/Users/AN515-57/Documents/GitHub/ShooterPython/sql practica/DBUsuarios.db")
            print("Conexion exitosa")
            return conexion
        #2 O notificar que se falló
        except sqlite3.OperationalError:
            print("No se pudo conectar")
    
    def guardarUsuario(self, nom, cor, con):
        
        #1 Llamar a la conexión
        conx = self.conexionBD()
        #2 Revisar que los parámetros no estén vacíos
        if(nom=="" or cor=="" or con==""):
            messagebox.showwarning("Cuidado!", "Revisa tu formulario")
            conx.close()
        else:
            #Preparar los datos y el query de SQL
            cursor = conx.cursor()
            conH = self.encriptarCont(con)
            datos = (nom,cor,conH)
            qryInsert = "insert into DBRegistrados(nombre,correo,contra) values(?,?,?)"
            
            #Insertar y cerrar la conexión
            cursor.execute(qryInsert, datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Exito", "Se guardó el Usuario")
            
    def encriptarCont(self,con):
        plainpass = con
        plainpass = plainpass.encode() #Convierte la contraseña a bytes
        sal = bcrypt.gensalt()
        conHa = bcrypt.hashpw(plainpass, sal)
        print(conHa)
        return conHa