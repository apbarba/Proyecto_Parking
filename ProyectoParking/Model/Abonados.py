import datetime

from Model.Parking import Parking
import random


class Abonados():

    def __init__(self, dni, nombre, apellidos, tarjeta_credito, email, matricula):

        self.__dni = dni

        self.__nombre = nombre

        self.__apellidos = apellidos

        self.__tarjeta_credito = tarjeta_credito

        self.__tipo_abono = []

        self.__email = email

        self.__pin = random.randint(1,100)

        self.__abonados = []

        self.__matricula = matricula


    @property
    def dni(self):

        return self.__dni

    @dni.setter
    def dni(self, value):

        self.__dni = value

    @property
    def nombre(self):

        return self.__nombre

    @nombre.setter
    def nombre(self, value):

        self.__nombre = value

    @property
    def apellidos(self):

        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):

        self.__apellidos = value

    @property
    def tarjeta_credito(self):

        return self.__tarjeta_credito

    @tarjeta_credito.setter
    def tarjeta_credito(self,value):

        self.__tarjeta_credito = value

    @property
    def tipo_abono(self):

        return self.__tipo_abono

    @tipo_abono.setter
    def tipo_abono(self, value):

        self.__tipo_abono = value

    @property
    def email(self):

        return self.__email

    @email.setter
    def email(self, value):

        self.__email = value

    @property
    def pin(self):

        return self.__pin

    @pin.setter
    def pin(self,value):

        self.__pin = value

    @property
    def abonados(self):

        return self.__abonados

    @abonados.setter
    def abonados(self,value):

        self.__abonados = value

    @property
    def matricula(self):

        return self.__matricula

    @matricula.setter
    def matricula(self, value):

        self.__matricula = value



