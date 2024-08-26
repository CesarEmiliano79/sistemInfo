import mysql.connector
import os

nombre = input("Dame un nombre: ")
edad = input("Dame su edad: ")
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="miTarea"
)

fichero= open(nombre+".txt", "w")
fichero.write(nombre+"\t"+edad+"\n")
fichero.close()


cursor = conexion.cursor()
query="INSERT INTO nombres (nombre,edad) VALUES (%s,%s)"
valor=(nombre,edad)
cursor.execute(query,valor)
conexion.commit()
conexion.close()