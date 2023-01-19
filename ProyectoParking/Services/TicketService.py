from Model.Ticket import *

class TicketService():

    def __init__(self, ticket):

        self.ticket = ticket


    def calcular_coste(self):


        self.ticket.fecha_salida = datetime.datetime.now()

        tiempo_estacionado = self.ticket.fecha_salida - self.ticket.fecha_entrada

        tiempo_estacionado_minutos = int(tiempo_estacionado.total_seconds() / 60)

        if self.ticket.tipo_vehiculo == "coche":

            tarifa = 0.12

        elif self.ticket.tipo_vehiculo == "moto":

            tarifa = 0.08

        elif self.ticket.tipo_vehiculo == "pmr":

            tarifa = 0.10

        else:

            raise ValueError("Tipo de vehículo no válido.")

        self.ticket.coste = tarifa * tiempo_estacionado_minutos