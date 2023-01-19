
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

        self.pin = random.randint(1,100)

        self.cobros = []

        self.lista_ticket = []

        self.abonados = []

        self.lista_plazas = [self.lista_motos, self.lista_coches, self.lista_pmr]

