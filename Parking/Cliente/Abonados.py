
class Abonados(Parking):
    
     def __init__(self):
       
        self.abonados = {}

    def depositar_abonado(self, matricula, dni, nombre, apellidos, num_tarjeta, tipo_abono, email, tipo_vehiculo):
        
        if dni in self.abonados:
        
            raise ValueError("Ya existe un abonado con ese DNI")
        
        if matricula in [v.matricula for v in self.vehiculos]:
        
            raise ValueError("Ya existe un vehiculo con esa matrícula")
        
        if tipo_vehiculo not in ["turismo", "moto", "movilidad_reducida"]:
        
            raise ValueError("Tipo de vehículo no válido")
        
        plaza = self.asignar_plaza(tipo_vehiculo)
        
        self.abonados[dni] = ClienteAbonado(dni, nombre, apellidos, num_tarjeta, tipo_abono, email)
        
        self.vehiculos.append(Vehiculo(matricula, tipo_vehiculo, plaza))

        return 'Se registró correctamente'