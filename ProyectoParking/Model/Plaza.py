class Plaza:

    def __init__(self, num_plaza, ocupado, reservada, vehiculo):

        self.__num_plaza = num_plaza

        self.__ocupado = ocupado

        self.__abonado = reservada

        self.__vehiculo = vehiculo

    @property
    def num_plaza(self):

        return self.__num_plaza

    @num_plaza.setter
    def num_plazas(self,value):

        self.__num_plaza = value

    @property
    def ocupado(self):

        return self.__ocupado

    @ocupado.setter
    def ocupado(self,value):

        self.__ocupado = value

    @property
    def abonado(self):

        return self.__abonado

    @abonado.setter
    def abonado(self,value):

        self.__abonado = value

    @property
    def vehiculo(self):

        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self,value):

        self.__vehiculo = value

