
import random

import datetime


class Parking:

    def __init__(self, total_plazas):
        
        self.__total_plazas = total_plazas
        
        self.__plazas_coche = int(0.7 * total_plazas)
        
        self.__plazas_moto = int(0.15 * total_plazas)
        
        self.__plazas_pmr = int(0.15 * total_plazas)
        
        self.__lista_coches = []
        
        self.__lista_motos = []
        
        self.__lista_pmr = []

        self.__pin = random.randint(1,100)

        self.__cobros = []

        self.__lista_ticket = []

        self.__abonados = []

        self.__lista_abonos = []

        self.__lista_plazas = [self.lista_motos, self.lista_coches, self.lista_pmr]


    @property
    def total_plazas(self):

        return self.__lista_plazas

    @total_plazas.setter
    def total_plazas(self,value):

        self.__total_plazas = value

    @property
    def plazas_coche(self):

        return self.__plazas_coche

    @plazas_coche.setter
    def plazas_coche(self,value):

        self.__plazas_coche = value

    @property
    def plazas_moto(self):

        return self.__plazas_moto

    @plazas_moto.setter
    def plazas_moto(self,value):

        self.__plazas_moto = value

    @property
    def plazas_pmr(self):

        return self.__plazas_pmr

    @plazas_pmr.setter
    def plazas_pmr(self,value):

        self.__plazas_pmr = value

    @property
    def lista_coches(self):

        return self.__lista_coches

    @lista_coches.setter
    def lista_coches(self, value):

        self.__lista_coches = value

    @property
    def lista_motos(self):

        return self.__lista_motos

    @lista_motos.setter
    def lista_motos(self,value):

        self.__lista_motos = value

    @property
    def lista_pmr(self):

        return self.__lista_pmr

    @lista_pmr.setter
    def lista_pmr(self,value):

        self.__lista_pmr = value

    @property
    def cobros(self):

        return self.__cobros

    @cobros.setter
    def cobros(self,value):

        self.__cobros = value

    @property
    def pin(self):

        return self.__pin

    @pin.setter
    def pin(self,value):

        self.__pin = value

    @property
    def lista_ticket(self):

        return self.__lista_ticket

    @lista_ticket.setter
    def lista_ticker(self,value):

        self.__lista_ticket = value

    @property
    def abonados(self):

        return self.__abonados

    @abonados.setter
    def abonados(self,value):

        self.__abonados = value

    @property
    def lista_plazas(self):

        return self.__lista_plazas

    @lista_plazas.setter
    def lista_plazas(self,value):

        self.__lista_plazas = value

    @property
    def lista_abonos(self):

        return self.__lista_abonos

    @lista_abonos.setter
    def lista_abonos(self,value):

        self.__lista_abonos = value
