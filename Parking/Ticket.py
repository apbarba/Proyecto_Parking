class Ticket:
    
    def __init__(self, matricula, plaza_id, pin, tipo_vehiculo):
       
        self.matricula = matricula
       
        self.plaza_id = plaza_id
       
        self.pin = pin
       
        self.tipo_vehiculo = tipo_vehiculo
       
        self.fecha_entrada = datetime.now()
       
        self.fecha_salida = None
       
        self.tarifa = tarifa
       
        self.costo_total = 0

#En este método que he creado calcula el costo de lo que tiene que 
#pagar el cliente por el tiemp transcurrido por la tarifa dependiendo
#del tipo de vehículo para poder utilizar en la clase Cliente en el
#método de calcular_costo_plaza (En estos momento no se utiliza est método)

    def calcular_costo(self, tiempo_estacionado):

        self.costo_total = tiempo_estacionado * self.tarifa

        return self.costo_total