from Vehiculo import Vehiculo


class PMR(Vehiculo):

    def __init__(self, matricula, tipo_vehiculo):

        super().__init__(matricula, tipo_vehiculo)

        self.tarifa = 0.10

    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa
    def tarifa(self, value):
        self.__tarifa = value