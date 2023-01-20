from datetime import datetime

from Model.Abonados import Abonados


class Abonos(Abonados):

    def __int__(self,  dni, nombre, apellidos, tarjeta_credito, email, matricula):

        super().__init__(self, dni, nombre, apellidos, tarjeta_credito, email, matricula)

        self.__fecha_cancelacion = datetime.now()

        self.__fecha_activacion = datetime.datetime.now()

        self.__mes = self.__fecha_cancelacion.month

    @property
    def fecha_cancelacion(self):

        return self.__fecha_cancelación

    @fecha_cancelacion.setter
    def fecha_cancelacion(self, value):

        self.__fecha_cancelación = value

    @property
    def fecha_activacion(self):

        return self.__fecha_activacion

    @fecha_activacion.setter
    def fecha_activacion(self, value):

        self.__fecha_activacion = value