
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