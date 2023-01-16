
import random

from datetime import datetime
from Parking.Vehiculo.Moto import Moto
from Parking.Vehiculo.Pmr import PMR
from Parking.Vehiculo.Turismo import Turismo

class Parking:

#Este primer método creado son los atributos inicializados de la clase necesarioa
    def __init__(self, num_plazas, plazas_turismo, plazas_moto, plazas_pmr):

        self.__num_plazas = num_plazas

        self.__plazas_turismo = plazas_turismo

        self.__plazas_moto = plazas_moto

        self.__plazas_pmr = plazas_pmr

        self.plazas = []

        self.abonados = {}

        self.cobros = []

        self.vehiculos = []

        self.pin = [1,2,3,4,5,6,7,8,9,10]


    #vehiculo = Turismo(matricula, fecha_entrada=datetime.now()) //DECLARAR LA MATRÍCULA
    #vehiculo = Moto(matricula, fecha_entrada=datetime.now()) //DECLARAR LA MATRÍCULA
    #vehiculo = PMR(matricula, fecha_entrada=datetime.now()) //DECLARAR LA MATRÍCULA





#Después de inicializar los atributos de la clase, voy a crear un método que 
#realice el costo de cada vehículo por el tiempo que esté en la plaza correspondiete
#para ello, he utilizado el datetime.now para saber la hora y el tiempo actual y calcularlo.

    def calcular_costo_plaza(self, matricula):

        tiempo_estacionado = datetime.now() - self.abonados[matricula].fecha_entrada

        minutos_estacionado = tiempo_estacionado.total_seconds() / 60

    #self.abonados[matricula].calcular_costo(minutos_estacionado)

   # return self.abonados[matricula].costo_total, self.abonados[matricula].tarifa
    
        tipo_vehiculo = self.abonados[matricula].tipo_vehiculo

        if tipo_vehiculo == "turismo":

            tarifa = 0.12
    
        elif tipo_vehiculo == "moto":

            tarifa = 0.08

        elif tipo_vehiculo == "pmr":

            tarifa = 0.10
    
        else:

            tarifa = 0

        coste = minutos_estacionado * tarifa

        return coste, tarifa

#DEPOSITAR VEHÍCULO

#El primer método que se nos pide del proyecto es asignar una plaza depende del tipo
#de vehículo que utilice, por lo que llamamos almétodo 'Asignar plazas'
#y depende del tipo de vehículo que introduzca el cliente, se ocupará la plaza
#de ese vehículo restando las plazas libres por cada uno.
    def asignar_plaza(self, vehiculo):

        if vehiculo.tipo == "turismo":
           
            plazas = self.plazas_turismo
        
        elif vehiculo.tipo == "moto":
        
            plazas = self.plazas_moto
        
        elif vehiculo.tipo == "pmr":
        
            plazas = self.plazas_pmr
        
        else:
        
            raise ValueError("Tipo de vehículo no válido")

        if plazas:
        
            plaza = plazas.pop(0)
        
            vehiculo.plaza = plaza
        
            self.vehiculos.append(vehiculo)
        
        else:
        
            raise ValueError("No hay plazas disponibles para este tipo de vehículo")
        

#Este método lo utilizaremos para generar aleatoriamente un pin de seis dígitos
#que hemos declarado como atributo de la clase inicializado en una lista del 1 al 10
#por lo que utilizamos la función sample para poder utilizar nuestra lista de numeros declaradas
#y el número de elementos aleatorios que queremos, que en este caso son 6

    def generate_pin(self):

        return random.sample(self.pin, 6)

#En el segundo método que se nos pide de la clase, debemos de imprimir un ticker al cliente
#que a aparcado en la plaza, para ello necesitamos saber el tipo de vehículo, su matricula,
#y la fecha en la que se depositó en la plaza. 
#Se generará un pin aleatoriamente de 6 dígitos que servirá para luego sascar el vehículo
#del lugar asignado. No utiliza la herencia
    def depositar_vehiculo(self, matricula, tipo_vehiculo, abonado=False):
    
        if tipo_vehiculo == "turismo":
    
            vehiculo = Turismo(matricula, fecha_entrada=datetime.now())
    
        elif tipo_vehiculo == "moto":
    
            vehiculo = Moto(matricula, fecha_entrada=datetime.now())
    
        elif tipo_vehiculo == "pmr":
    
            vehiculo = PMR(matricula, fecha_entrada=datetime.now())
    
        else:
    
            raise ValueError("Tipo de vehículo no válido")

        if abonado:
    
            pin = self.generate_pin()
    
            self.abonados[matricula] = pin
    
            vehiculo.pin = pin
    
            vehiculo.abonado = abonado
        
    
        vehiculo.fecha_deposito = datetime.now()
    
        self.asignar_plaza(vehiculo)

#Imprimimos el ticker con la información necesaria y requerida
        print("Ticket de estacionamiento:")
       
        print("Matricula: ", vehiculo.matricula)
       
        print("Fecha de deposito: ", vehiculo.fecha_deposito)
       
        print("Plaza asignada: ", vehiculo.plaza)
       
        if abonado:
       
            print("Pin de retirada: ", pin)


#RETIRAR VEHÍCULO

#En este método que he creado, se necesitará la matricula el pin y el id de la plaza
#donde se muestra el precio final a pagar con la tarifa, para ello
#hemos implementado un método a parte donde se especifica las tarifas de cada uno y que
#hemos utilizado para que resulte más simple el código y fácil de entender
#Este método no se utiliza la herencia
    def liberar_plaza(self, matricula, pin):
       
        for vehiculo in self.vehiculos:
       
            if vehiculo.matricula == matricula:
       
                if vehiculo.pin != pin:
       
                    raise ValueError("Pin incorrecto")
       
                vehiculo.fecha_salida = datetime.now()
       
                tiempo_estacionado = vehiculo.fecha_salida - vehiculo.fecha_entrada
       
                minutos_estacionado = tiempo_estacionado.total_seconds() / 60
       
                costo_total = vehiculo.calcular_costo(minutos_estacionado)
       
                print(f"Costo total: {costo_total} €")
       
                factura = vehiculo.generar_factura()
       
                self.plazas_libres.append(vehiculo.plaza)
       
                self.vehiculos.remove(vehiculo)
       
                self.cobros.append(factura)
       
                return costo_total
        
    def guardar_cobro(self, factura):
        
        self.coleccion_cobros.append(factura)

    #def liberar_plaza(self, matricula):
        
     #   for vehiculo in self.vehiculos:
        
     #       if vehiculo.matricula == matricula:
        
      #          vehiculo.fecha_salida = datetime.now()
        
       #         tiempo_estacionado = vehiculo.fecha_salida - vehiculo.fecha_entrada
        
        #        minutos_estacionado = tiempo_estacionado.total_seconds() / 60
        
         #       costo_total = vehiculo.calcular_costo(minutos_estacionado)
        
          #      factura = vehiculo.generar_factura()
                
           #     pass
