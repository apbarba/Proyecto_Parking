
import random

class ClienteAbonado:
   
    def __init__(self, dni, nombre, apellidos, num_tarjeta, tipo_abono, email):
   
        self.dni = dni
   
        self.nombre = nombre
   
        self.apellidos = apellidos
   
        self.num_tarjeta = num_tarjeta
   
        self.tipo_abono = tipo_abono
   
        self.email = email

        self.pinAbonado = self.generate_pin() 

    
    def generate_pin(self):

        return random.sample(self.pin, 6)