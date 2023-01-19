from Model.Parking import Parking
import random


class Abonados():

    def __init__(self, dni, nombre, apellidos, tarjeta_credito, tipo_abono, email):

        self.dni = dni

        self.nombre = nombre

        self.apellidos = apellidos

        self.tarjeta_credito = tarjeta_credito

        self.tipo_abono = tipo_abono

        self.email = email

        self.pin = random.randint(1,100)

        self.abonados = []

    parking = Parking(100)


    def depositar_abonado(self, matricula, dni):

        if self.dni in self.abonados:

            self.pin = self.abonados[self.dni]['pin']

            id_plaza = None

            if self.tipo_abono == "coche":

                if len(self.parking.lista_coches) < self.parking.plazas_coche:

                    id_plaza = len(self.parking.lista_coches)

                    self.parking.lista_coches.append(matricula)

                    return f"Plaza de coches asignada al abonado. Su número de ticket es {id_plaza}, matrícula {matricula}, pin asociado {self.pin}."

                else:

                    return "Lo siento, no hay plazas de coches disponibles para abonados."

            elif self.tipo_abono == "moto":

                if len(self.parking.lista_motos) < self.parking.plazas_moto:

                    id_plaza = len(self.parking.lista_motos)

                    self.parking.lista_motos.append(matricula)

                    return f"Plaza de motos asignada al abonado. Su número de ticket es {id_plaza}, matrícula {matricula}, pin asociado {self.pin}."

                else:

                    return "Lo siento, no hay plazas de motos disponibles para abonados."

            elif self.tipo_abono == "pmr":

                if len(self.parking.lista_pmr) < self.parking.plazas_pmr:

                    id_plaza = len(self.parking.plazas_pmr)

                    self.parking.lista_pmr.append(matricula)

                    return f"Plaza para PMR asignada al abonado. Su número de ticket es {id_plaza}, matrícula {matricula}, pin asociado {self.pin}."

                else:

                    return "Lo siento, no hay plazas para PMR disponibles para abonados."

            else:

                return "Tipo de abono no válido."

        else:

            return "No se encuentra su Dni, lo sentimos"

    def retirar_abonado(self, dni, matricula):

        if dni in self.parking.abonados:

            id_plaza = self.parking.abonados[dni]['id_plaza']

            if self.parking.lista_plazas[id_plaza]['matricula'] == matricula:

                self.parking.lista_plazas[id_plaza]['estado'] = 'libre'

                return f"Su vehículo con matrícula {matricula} ha sido retirado de la plaza {id_plaza}."

            else:

                return "La matrícula no coincide con la plaza asignada."

        else:

            return "El DNI introducido no está registrado como abonado, lo sentimos."