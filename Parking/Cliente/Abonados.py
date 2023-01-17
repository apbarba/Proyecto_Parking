

from Parking.Cliente.ClienteAbonado import ClienteAbonado
from Parking.Cliente.Parking import Parking
from Parking.Vehiculo.Vehiculo import Vehiculo


class Abonados(Parking):
    
    def __init__(self,  num_plazas, plazas_turismo, plazas_moto, plazas_pmr):
       
       super.__init__(self, num_plazas, plazas_turismo, plazas_moto, plazas_pmr)
       
       self.abonados = []

       self.vehiculos = []


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
            
            #Utilizamos el método de generar pin de la clase ClienteAbonado
            #para generar el pin de seis dígitos necesario para poder retirar el vehículo del
            #abonado
        if self.abonados:
                
            pin = ClienteAbonado.generate_pin()
                
            self.abonados[dni] = pin
                
            tipo_vehiculo.pin = pin
        

        return 'Se registró correctamente'
        
    def retirar_abonados(self, matricula, plaza_id, pin):
            
        for v in self.vehiculos:

            if v.matricula == matricula and v.plaza_id == plaza_id

                if v.cliente.pin != pin:

                    raise ValueError('Pin introducido es incorrecto')
                
                v.estado = 'Reservada'

                v.cliente = None

                return 'Retirado correctamente'
            
        raise ValueError('Vehículo no encontrado')
                