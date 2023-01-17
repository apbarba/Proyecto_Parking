
#Inicializamos la clase Padre(Vehículo)

class Vehiculo:

    def __init__(self, matricula, fecha_entrada, tarifa, tipo_vehiculo, plaza):
        
        self.matricula = matricula
        
        self.fecha_entrada = fecha_entrada
        
        self.fecha_salida = None
        
        self.tarifa = tarifa

        self.tipo_vehiculo = tipo_vehiculo

        self.plaza = plaza

        self.estado = 'Ocupado'

        self.cliente = None


        
        self.costo_total = 0

#Mismo método que declaré en la clase de Ticker
        def calcular_costo(self, tiempo_estacionado):
        
            self.costo_total = tiempo_estacionado * self.tarifa
        
            return self.costo_total

#He generado un diccionario con la información que debe de contener
#el vehículo y como se vería en la factura
        def generar_factura(self):
       
            factura = {
       
                "matricula": self.matricula,
        
                "tipo_vehiculo": self.tipo,
        
                "fecha_entrada": self.fecha_entrada,
        
                "fecha_salida": self.fecha_salida,
        
                "tiempo_estacionado": self.tiempo_estacionado,
        
                "costo_total": self.costo_total,
        
                "plaza": self.plaza
            }
       
            return factura