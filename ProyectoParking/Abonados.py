from Parking import Parking
from Vehiculo import Vehiculo
from random import random


class Abonados():

    def __init__(self, dni, nombre, apellidos, tarjeta_credito, tipo_abono, email):

        self.dni = dni

        self.nombre = nombre

        self.apellidos = apellidos

        self.tarjeta_credito = tarjeta_credito

        self.tipo_abono = tipo_abono

        self.email = email

        self.pin = None

    parking = Parking(100)
    def depositar_abonado(self, matricula, parking):

        if self.dni in parking.abonados:

            self.pin = parking.abonados[self.dni]['pin']

            id_plaza = None

            if self.tipo_abono == "coche":

                if len(parking.lista_coches) < parking.plazas_coche:

                    id_plaza = len(parking.lista_coches)

                    parking.lista_coches.append(matricula)

                    return f"Plaza de coches asignada al abonado. Su número de ticket es {id_plaza}, matrícula {matricula}, pin asociado {self.pin}."

                else:

                    return "Lo siento, no hay plazas de coches disponibles para abonados."

            elif self.tipo_abono == "moto":

                if len(parking.lista_motos) < parking.plazas_moto:

                    id_plaza = len(parking.lista_motos)

                    parking.lista_motos.append(matricula)

                    return f"Plaza de motos asignada al abonado. Su número de ticket es {id_plaza}, matrícula {matricula}, pin asociado {self.pin}."

                else:

                    return "Lo siento, no hay plazas de motos disponibles para abonados."

            elif self.tipo_abono == "pmr":

                if len(parking.lista_pmr) < parking.plazas_pmr:

                    id_plaza = len(parking.lista_pmr)

                    parking.lista_pmr.append(matricula)

                    return f"Plaza para PMR asignada al abonado. Su número de ticket es {id_plaza}, matrícula {matricula}, pin asociado {self.pin}."

                else:

                    return "Lo siento, no hay plazas para PMR disponibles para abonados."

            else:

                return "Tipo de abono no válido."

        else:

            return "No se encuentra su Dni, lo sentimos"

    def retirar_abonado(self, dni, matricula, parking):

        if dni in parking.abonados:

            id_plaza = parking.abonados[dni]['id_plaza']

            if parking.lista_plazas[id_plaza]['matricula'] == matricula:

                parking.lista_plazas[id_plaza]['estado'] = 'libre'

                return f"Su vehículo con matrícula {matricula} ha sido retirado de la plaza {id_plaza}."

            else:

                return "La matrícula no coincide con la plaza asignada."

        else:

            return "El DNI introducido no está registrado como abonado, lo sentimos."