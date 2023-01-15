
#Misma explicación que en la clase Turismo pero con diferente
#precio de la tarifa
class PMR(Vehiculo):
    
    def __init__(self, matricula, fecha_entrada):
    
        super().__init__(matricula, fecha_entrada, tarifa=0.10)