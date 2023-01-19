
import datetime
import random


class Ticket:
    
    def __init__(self, matricula, id_plaza, pin, tipo_vehiculo):
    
        self.matricula = matricula
    
        self.id_plaza = id_plaza
    
        self.pin = random.sample(pin, 6)
    
        self.fecha_entrada = datetime.datetime.now()
    
        self.fecha_salida = None
    
        self.coste = None

        self.tipo_vehiculo = tipo_vehiculo


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
        