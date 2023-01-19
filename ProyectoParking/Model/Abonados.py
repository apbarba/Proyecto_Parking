import datetime

from Model.Parking import Parking
import random


class Abonados():

    def __init__(self, dni, nombre, apellidos, tarjeta_credito, email, matricula):

        self.dni = dni

        self.nombre = nombre

        self.apellidos = apellidos

        self.tarjeta_credito = tarjeta_credito

        self.tipo_abono = []

        self.email = email

        self.pin = random.randint(1,100)

        self.abonados = []

        self.matricula = matricula

        self.fecha_cancelación = None

        self.fecha_activacion = datetime.datetime.now()


