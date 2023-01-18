
import random

import datetime

class Parking:

    def __init__(self, total_plazas):
        
        self.total_plazas = total_plazas
        
        self.plazas_coche = int(0.7 * total_plazas)
        
        self.plazas_moto = int(0.15 * total_plazas)
        
        self.plazas_pmr = int(0.15 * total_plazas)
        
        self.lista_coches = []
        
        self.lista_motos = []
        
        self.lista_pmr = []

        self.pin = [1,2,3,4,5,6,7,8,9,10] 

        self.cobros = []

        self.lista_ticket = []

        self.abonados = []

        self.lista_plazas = []


    
    def depositar_vehiculo(self, matricula, tipo_vehiculo):
        
        pin = random.sample(self.pin, 6)
        
        id_plaza = None
        
        fecha_entrada = datetime.datetime.now()
        
        if tipo_vehiculo == "coche":
        
            if len(self.lista_coches) < self.plazas_coche: #Si es menor que la lista de las plazas de coches, entra
        
                id_plaza = len(self.lista_coches)
        
                self.lista_coches.append(matricula)
        
                return f"Plaza de coches asignada. Su número de ticket es {id_plaza}, matricula {matricula}, fecha de entrada {fecha_entrada}, y su pin es {pin}."
        
            else:
        
                return "No hay plazas de coches disponibles"

        elif tipo_vehiculo == "moto":
            
            if len(self.lista_motos) < self.plazas_moto:
            
                id_plaza = len(self.lista_motos)
            
                self.lista_motos.append(matricula)
            
                return f"Plaza de motos asignada. Su número de ticket es {id_plaza}, matricula {matricula}, fecha de entrada {fecha_entrada}, y su pin es {pin}."
            
            else:
            
                return "No hay plazas de motos disponibles."
        
        elif tipo_vehiculo == "pmr":
        
            if len(self.lista_pmr) < self.plazas_pmr:
        
                id_plaza = len(self.lista_pmr)
        
                self.lista_pmr.append(matricula)
        
                return f"Plaza para PMR asignada. Su número de ticket es {id_plaza}, matricula {matricula}, fecha de entrada {fecha_entrada}, y su pin es {pin}."
        
            else:
        
                return "No hay plazas para PMR disponibles."
        
        else:
        
            return "Tipo de vehículo no válido."

        def retirar_vehiculo(self, matricula, id_plaza, pin):

            for ticket in self.lista_tickets:

                if ticket["matricula"] == matricula and ticket["id_plaza"] == id_plaza and ticket["pin"] == pin:

                    fecha_salida = datetime.datetime.now()

                    tiempo_estacionado = fecha_salida - ticket["fecha_entrada"]

                    tiempo_estacionado_minutos = int(tiempo_estacionado.total_seconds() / 60)

                    if ticket["tipo_vehiculo"] == "coche":

                        tarifa = 0.12

                    elif ticket["tipo_vehiculo"] == "moto":

                        tarifa = 0.08

                    elif ticket["tipo_vehiculo"] == "pmr":

                        tarifa = 0.10

                    else:

                        raise ValueError("Tipo de vehículo no válido.")
                    coste = tarifa * tiempo_estacionado_minutos
                    self.cobros.append(
                        {'matricula': matricula, 'fecha_entrada': ticket["fecha_entrada"], 'fecha_salida': fecha_salida,
                         'coste': coste})
                    self.lista_tickets.remove(ticket)
                    return f"El coste total a pagar es de {coste} euros. El tipo de vehículo es {ticket['tipo_vehiculo']}.El vehículo con matrícula {matricula} ha sido retirado del parking."

        return "Matricula, plaza o pin incorrecto"