from Model.Parking import *

parking = Parking(100)

def generate_pin(self):

    return random.randint(1, 100)


def depositar_vehiculo(self, matricula, tipo_vehiculo):

    pin = self.generate_pin()

    id_plaza = None

    fecha_entrada = datetime.datetime.now()

    if tipo_vehiculo == "coche":

        if len(parking.lista_coches) < parking.plazas_coche:

            id_plaza = len(parking.lista_coches)

            parking.lista_coches.append(matricula)

            return f"Plaza de coches asignada. Su número de plaza es {id_plaza}, matricula {matricula}, fecha de entrada {fecha_entrada}, y su pin es {pin}."

        else:

            return "No hay plazas de coches disponibles"

    elif tipo_vehiculo == "moto":

        if len(parking.lista_motos) < parking.plazas_moto:

            id_plaza = len(parking.lista_motos)

            parking.lista_motos.append(matricula)

            return f"Plaza de motos asignada. Su número de plaza es {id_plaza}, matricula {matricula}, fecha de entrada {fecha_entrada}, y su pin es {pin}."

        else:

            return "No hay plazas de motos disponibles."

    elif tipo_vehiculo == "pmr":

        if len(parking.lista_pmr and parking.lista_plazas) < parking.plazas_pmr:

            id_plaza = len(parking.lista_pmr)

            parking.lista_pmr.append(matricula)

            return f"Plaza para PMR asignada. Su número de plaza es {id_plaza}, matricula {matricula}, fecha de entrada {fecha_entrada}, y su pin es {pin}."

        else:

            return "No hay plazas para PMR disponibles."

    else:

        return "Tipo de vehículo no válido."


def retirar_vehiculo(matricula, id_plaza, pin):

    for ticket in parking.lista_ticket:

        if ticket["matricula"] == matricula and ticket["id_plaza"] == id_plaza and ticket["pin"] == pin:

            ticket.fecha_salida = datetime.datetime.now()

            ticket.tiempo_estacionado = ticket.fecha_salida - ticket["fecha_entrada"]

            tiempo_estacionado_minutos = int(ticket.tiempo_estacionado.total_seconds() / 60)

            if ticket["tipo_vehiculo"] == "coche":

                tarifa = 0.12

            elif ticket["tipo_vehiculo"] == "moto":

                tarifa = 0.08

            elif ticket["tipo_vehiculo"] == "pmr":

                tarifa = 0.10

            else:

                raise ValueError("Tipo de vehículo no válido.")

            coste = tarifa * tiempo_estacionado_minutos

            parking.cobros.append(

                {'matricula': matricula, 'fecha_entrada': ticket["fecha_entrada"], 'fecha_salida': ticket.fecha_salida,
                 'coste': coste})

            parking.lista_plazas.remove(ticket)

            return f"El coste total a pagar es de {coste} euros. El tipo de vehículo es {ticket['tipo_vehiculo']}.El vehículo con matrícula {matricula} ha sido retirado del parking."

    return "Matricula, plaza o pin incorrecto"