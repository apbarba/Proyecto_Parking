
#He utilizado la herencia de la clase padre(Vehículo) para
#utilizar los atributos necesarios en cada clase hija.
#En caada clase hija tengo pensado hacer el método distintivo
#de cada una de sus diferentes tarifas
from Parking.Vehiculo.Vehiculo import Vehiculo

class Turismo(Vehiculo):
    
    def __init__(self, matricula, fecha_entrada):
    
        super().__init__(matricula, fecha_entrada, tarifa=0.12)