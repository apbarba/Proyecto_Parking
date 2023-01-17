
import datetime
from sqlite3 import Cursor


class Ticket:
    
    def __init__(self, matricula, id_plaza, pin):
    
        self.matricula = matricula
    
        self.id_plaza = id_plaza
    
        self.pin = pin
    
        self.fecha_entrada = datetime.datetime.now()
    
        self.fecha_salida = None
    
        self.coste = None
    
        Cursor.execute(f"SELECT * FROM plazas WHERE id = {id_plaza}")
    
        plaza = _Cursor.fetchone()
    
        if plaza:
    
            self.tipo_vehiculo = plaza[1]
    
        else:
    
            raise ValueError("No existe plaza con ese id")


    def calcular_coste(self):


        self.fecha_salida = datetime.datetime.now()

        tiempo_estacionado = self.fecha_salida - self.fecha_entrada

        tiempo_estacionado_minutos = int(tiempo_estacionado.total_seconds() / 60)

        if self.tipo_vehiculo == "coche":

            tarifa = 0.12

        elif self.tipo_vehiculo == "moto":

            tarifa = 0.08

        elif self.tipo_vehiculo == "pmr":

            tarifa = 0.10

        else:

            raise ValueError("Tipo de vehículo no válido.")

        self.coste = tarifa * tiempo_estacionado_minutos
        