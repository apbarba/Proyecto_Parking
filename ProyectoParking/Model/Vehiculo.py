
class Vehiculo:
    
    def __init__(self, matricula, tipo_vehiculo):
    
        self.__matricula = matricula

        self.__tipo_vehiculo = tipo_vehiculo

    @property
    def matricula(self):

        return self.__matricula

    @matricula.setter
    def matricula(self,value):

        self.__matricula = value

    @property
    def tipo_vehiculo(self):

        return self.__tipo_vehiculo

    @tipo_vehiculo.setter
    def tipo_vehiculo(self,value):

        self.__tipo_vehiculo = value