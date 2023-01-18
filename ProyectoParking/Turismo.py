
from Vehiculo import Vehiculo


class Turismo(Vehiculo):

    def __init__(self, matricula, tipo_vehiculo):

        super().__init__(matricula, tipo_vehiculo)

        self.tarifa = 0.12