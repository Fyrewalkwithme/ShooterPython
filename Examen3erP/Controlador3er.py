from tkinter import messagebox
import sqlite3

class Controlador3er:
    def init(self):
        self
    
    #Preparar Conexion
    def conexionBD(self):
        try:
            conex= sqlite3.connect("C:/Users/AN515-57/Documents/GitHub/ShooterPython/Examen3erP/Ferreteria.db")
            print("Conexion exitosa")
            return conex
        #Catch de errores
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
    #Guardar Material
    def guardarMaterial(self, nom, cant):
        
        #1 Llamar a la conexión
        conx = self.conexionBD()
        #2 Revisar que los parámetros no estén vacíos
        if(nom=="" or cant==""):
            messagebox.showwarning("Atención!", "Revisa espacios vacíos.")
            conx.close()
        else:
            #Preparar los datos y el query de SQL
            cursor = conx.cursor()
            datos = (nom,cant)
            qryInsertar = "insert into MatConstruccion(Material,Cantidad) values(?,?)"
            
            #Insertar y cerrar la conexión
            cursor.execute(qryInsertar, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", "Material guardado exitosamente!")
    
    #Seleccionar todos
    def selectMateriales(self):
        conx = self.conexionBD()
        
        cursor = conx.cursor()
        sqlselect= "select * from MatConstruccion"
        cursor.execute(sqlselect)
        result = cursor.fetchall()
        
        conx.close()
        
        return result
    
    def ActualizaMaterial(self,ID2,Nom,Cant):
        conx = self.conexionBD()
        cursor = conx.cursor()
        update = 'UPDATE Matconstruccion set Material=?, Cantidad=? WHERE IDMat = '+ID2
                        
        if ID2 == "":
            messagebox.showwarning("Cuidado!", "El campo ID debe contener una ID válida!")
            conx.close
        else:
                cursor.execute(update, (Nom,Cant))
                conx.commit()
                conx.close()
                messagebox.showinfo("Material Actualizado", "El Material con la id "+str(ID2)+" ha sido actualizado.")
        
        