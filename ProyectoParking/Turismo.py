
from Vehiculo import Vehiculo


class Turismo(Vehiculo):

    def __init__(self, matricula, numero_ticket):

        super().__init__(matricula, numero_ticket)

        self.tarifa = 0.12