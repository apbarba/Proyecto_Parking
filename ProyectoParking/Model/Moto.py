
from Vehiculo import Vehiculo


class Moto(Vehiculo):

    def __init__(self, matricula, tipo_vehiculo):

        super().__init__(matricula, tipo_vehiculo)

        self.__tarifa = 0.08

    @property
    def tarifa(self):

        return self.__tarifa

    @tarifa
    def tarifa(self, value):

        self.__tarifa = value
