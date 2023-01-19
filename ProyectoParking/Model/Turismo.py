
from Vehiculo import Vehiculo


class Turismo(Vehiculo):

    def __init__(self, matricula, tipo_vehiculo):

        super().__init__(matricula, tipo_vehiculo)

        self.tarifa = 0.12

    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa
    def tarifa(self, value):
        self.__tarifa = value