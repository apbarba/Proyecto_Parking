
import sqlite3

conexion = sqlite3.connect('Parking.db')

cursor = conexion.cursor()

#Creamos una tabla de plazas para almacenar la información sobre las plazas ocupadas
cursor.execute("""
                
                CREATE TABLE plazas (id INTENGER PRIMARY KEY,
                tipo TEXT, matricula TEXT)
                
                """)

#También creamos una tabla de tikext para almacenar y poder consultar los ticket recopilados
cursor.execute("""

                CREATE TABLE tickets
                (id INTEGER PRIMARY KEY, matricula TEXT, fecha_entrada TIMESTAMP, 
                id_plaza INTEGER, pin INTEGER)
                
                """)

conexion.close()