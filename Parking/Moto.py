
#Misma explicación que en la clase de Turismo pero con
#diferen precio de tarifa
class Moto(Vehiculo):
    
    def __init__(self, matricula, fecha_entrada):
    
        super().__init__(matricula, fecha_entrada, tarifa=0.08)