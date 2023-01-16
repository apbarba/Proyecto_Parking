import sqlite3

#Para abrir la base de datos
conexion = sqlite3.connect('proyecto_parking')

#Vamos a crear un cursor
cursor = conexion.cursor()

#Aquí irian las consultas del proyecto, más que nada sobre
#los abonados

#Para cerrar la base de datos
conexion.close()