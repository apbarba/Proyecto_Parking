
import datetime
import random


class Ticket:
    
    def __init__(self, matricula, id_plaza, pin, tipo_vehiculo):
    
        self.__matricula = matricula
    
        self.__id_plaza = id_plaza
    
        self.__pin = random.sample(pin, 6)
    
        self.__fecha_entrada = datetime.datetime.now()
    
        self.__fecha_salida = None
    
        self.__coste = None

        self.__tipo_vehiculo = tipo_vehiculo

    @property
    def matricula(self):

        return self.__matricula

    @matricula.setter
    def matricula(self, value):

        self.__matricula = value

    @property
    def id_plaza(self):

        return self.__id_plaza

    @id_plaza.setter
    def id_plaza(self, value):

        self.__id_plaza

    @property
    def pin(self):

        return self.__pin

    @pin.setter
    def pin(self, value):

        self.__pin = value

    @property
    def fecha_entrada(self):

        return self.__fecha_entrada

    @fecha_entrada.setter
    def fecha_entrada(self, value):

        self.__fecha_entrada = value

    @property
    def fecha_salida(self):

        return self.__fecha_salida

    @fecha_salida
    def fecha_salida(self,value):

        self.__fecha_salida = value

    @property
    def coste(self):

        return self.__coste

    @coste.setter
    def coste(self,value):

        self.__coste = value

    @property
    def tipo_vehiculo(self):

        return self.__tipo_vehiculo

    @tipo_vehiculo.setter
    def tipo_vehiculo(self,value):

        self.__tipo_vehiculo = value






        