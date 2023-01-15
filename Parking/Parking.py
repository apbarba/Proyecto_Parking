
import random

from datetime import datetime

class Parking:

#Este primer método creado son los atributos inicializados de la clase necesarioa
    def __init__(self, num_plazas, plazas_turismo, plazas_moto, plazas_pmr):

        self.num_plazas = num_plazas

        self.plazas_turismo = plazas_turismo

        self.plazas_moto = plazas_moto

        self.plazas_pmr = plazas_pmr

        self.plazas_fecha_deposito = []

        self.plazas = []

        self.abonados = {}

        self.cobros = []


#Después de inicializar los atributos de la clase, voy a crear un método que 
#realice el costo de cada vehículo por el tiempo que esté en la plaza correspondiete
#para ello, he utilizado el datetime.now para saber la hora y el tiempo actual y calcularlo.

def calcular_coste_plaza(self, matricula):

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
    def asignar_plaza(self, matricula, tipo_vehiculo):

        if tipo_vehiculo == "turismo":

            for plaza in self.plazas_turismo:

            #vehículo = Turismo(matricula, fecha_entrada = datetime.now())
                
                if not plaza.ocupada:

                    plaza.ocupada = True

                    plaza.matricula = matricula

                    return plaza

        elif tipo_vehiculo == "moto":

            for plaza in self.plazas_moto:
            
            #vehículo = Moto(matricula, fecha_entrada = datetime.now())
             
                if not plaza.ocupada:

                    plaza.ocupada = True

                    plaza.matricula = matricula

                    return plaza

        elif tipo_vehiculo == "pmr":

            for plaza in self.plazas_pmr:
            
            #vehículo = PMR(matricula, fecha_entrada = datetime.now())
                
                if not plaza.ocupada:

                    plaza.ocupada = True

                    plaza.matricula = matricula

                    return plaza
        else:

            return None


#Este método lo utilizaremos en el método de imprimir el ticker (depositar_vehículo)
#Debemos de importar la librería de Python 'random' para el aleatorio
#y lo hemos definido que se generen los seis dígitos entre
#el 1 y el 100, número pequeños.

    def generate_pin():

        return random.randint(1, 100)

#En el segundo método que se nos pide de la clase, debemos de imprimir un ticker al cliente
#que a aparcado en la plaza, para ello necesitamos saber el tipo de vehículo, su matricula,
#y la fecha en la que se depositó en la plaza. 
#Se generará un pin aleatoriamente de 6 dígitos que servirá para luego sascar el vehículo
#del lugar asignado. No utiliza la herencia
    def depositar_vehiculo(self, matricula, tipo_vehiculo, plazas_fecha_deposito):

        plaza = self.asignar_plaza(matricula, tipo_vehiculo, plazas_fecha_deposito)

        if plaza:

            pin = generate_pin()

            self.abonados[matricula] = Ticket(matricula, plaza.id, pin, plazas_fecha_deposito)

            return self.abonados[matricula]

        else:

            return None

#RETIRAR VEHÍCULO

#En este método que he creado, se necesitará la matricula el pin y el id de la plaza
#donde se muestra el precio final a pagar con la tarifa, para ello
#hemos implementado un método a parte donde se especifica las tarifas de cada uno y que
#hemos utilizado para que resulte más simple el código y fácil de entender
#Este método no se utiliza la herencia
    def liberar_plaza(self, matricula, pin, plaza_id):

        if matricula in self.abonados:

            if self.abonados[matricula].pin == pin and 
            
            self.abonados[matricula].plaza_id == plaza_id:

                coste, tarifa = self.calcular_coste_plaza(matricula)

                print(f'El precio final es {coste}€ con una tarifa de {tarifa}€ por minuto')

                for plaza in self.plazas:

                    if plaza.id == plaza_id:

                        plaza.ocupada = False

                        plaza.matricula = None

                        del self.abonados[matricula]

                        return True
            else:

                return False
        else:

            return False

    #def liberar_plaza(self, matricula):
        
     #   for vehiculo in self.vehiculos:
        
     #       if vehiculo.matricula == matricula:
        
      #          vehiculo.fecha_salida = datetime.now()
        
       #         tiempo_estacionado = vehiculo.fecha_salida - vehiculo.fecha_entrada
        
        #        minutos_estacionado = tiempo_estacionado.total_seconds() / 60
        
         #       costo_total = vehiculo.calcular_costo(minutos_estacionado)
        
          #      factura = vehiculo.generar_factura()
                
           #     pass
