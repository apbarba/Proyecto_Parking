import pickle

import schedule
import time

from Model.Parking import *

from Model.Abonados import  *

class ParkingService():

    def __init__(self, parking):

        self.parking = parking

        self.intervalo_guardado = 300

        self.ultimo_guardado = time.time()

    def save_to_pickle(self, proyectoP):

        with open(proyectoP, "wb") as file:

            pickle.dump(self, file)

    @classmethod
    def load_from_pickle(cls, proyectoP):

        with open(proyectoP, "rb") as file:

            return pickle.load(file)

    def almacenamiento_automatico(self):

        schedule.every(5).minutes.do(self.guardar_datos)

    def iniciar_almacenamiento_automatico(self):

        while True:

            schedule.run_pending()

            time.sleep(1)

    def guardar_datos(self):

        if time.time() - self.ultimo_guardado > self.intervalo_guardado:

            with open("datos_parking.pickle", "wb") as f:

                pickle.dump(self.parking, f)

        self.ultimo_guardado = time.time()

    print(f"Datos guardados en {datetime.datetime.now()}")

    def generate_pin(self):

        return random.randint(1, 100)

    def asignar_plaza(self, abonado, tipo_vehiculo):

        pin = self.generate_pin()

        id_plaza = None

        if tipo_vehiculo == "coche":

            if len(self.parking.lista_coches) < self.parking.plazas_coche:

                id_plaza = len(self.parking.lista_coches)

                self.parking.lista_coches.append(abonado.matricula)

                id_plaza += 1

                self.parking.abonados.append({"matricula":abonado.matricula, "id_plaza":id_plaza, "dni":abonado.dni, "tipo_vehiculo":tipo_vehiculo, "pin":pin})

                return id_plaza

            else:

                return "No hay plazas de coches disponibles"

        elif tipo_vehiculo == "moto":

            if len(self.parking.lista_motos) < self.parking.plazas_moto:

                id_plaza = len(self.parking.lista_motos)

                self.parking.lista_motos.append(abonado.matricula)

                id_plaza += 1

                self.parking.abonados.append({"matricula":abonado.matricula, "id_plaza":id_plaza, "dni":abonado.dni, "tipo_vehiculo":tipo_vehiculo, "pin":pin})

                return id_plaza

            else:

                return "No hay plazas de motos disponibles"

        elif tipo_vehiculo == "pmr":

            if len(self.parking.lista_pmr) < self.parking.plazas_pmr:

                id_plaza = len(self.parking.lista_pmr)

                self.parking.lista_pmr.append(abonado.matricula)

                id_plaza += 1

                self.parking.abonados.append({"matricula":abonado.matricula, "id_plaza":id_plaza, "dni":abonado.dni, "tipo_vehiculo":tipo_vehiculo, "pin":pin})

                return id_plaza

            else:

                return "No hay plazas para PMR disponibles"
        else:

            return "Tipo de vehículo no válido"


    def depositar_vehiculo(self, matricula, tipo_vehiculo):

        pin = self.generate_pin()

        id_plaza = None

        fecha_entrada = datetime.datetime.now()

        if tipo_vehiculo == "coche":

            if len(self.parking.lista_coches) < self.parking.plazas_coche:

                id_plaza = len(self.parking.lista_coches)

                self.parking.lista_coches.append(matricula)

                id_plaza += 1

                print("Id plaza asignado: ", id_plaza)  # agregado para verificar id_plaza asignado

                self.parking.lista_ticket.append({"matricula":matricula, "id_plaza":id_plaza, "pin":pin, "fecha_entrada":fecha_entrada, "tipo_vehiculo":tipo_vehiculo})

                return f"Plaza de coches asignada. Su número de plaza es {id_plaza}, matricula {matricula}, fecha de entrada {fecha_entrada}, y su pin es {pin}."

            else:

                return "No hay plazas de coches disponibles"

        elif tipo_vehiculo == "moto":

            if len(self.parking.lista_motos) < self.parking.plazas_moto:

                id_plaza = len(self.parking.lista_motos)

                self.parking.lista_motos.append(matricula)

                id_plaza += 1

                print("Id plaza asignado: ", id_plaza)  # agregado para verificar id_plaza asignado

                self.parking.lista_ticket.append(
                    {"matricula": matricula, "id_plaza": id_plaza, "pin": pin, "fecha_entrada": fecha_entrada,
                     "tipo_vehiculo": tipo_vehiculo})


                return f"Plaza de motos asignada. Su número de plaza es {id_plaza}, matricula {matricula}, fecha de entrada {fecha_entrada}, y su pin es {pin}."

            else:

                return "No hay plazas de motos disponibles."

        elif tipo_vehiculo == "pmr":

            if len(self.parking.lista_pmr and self.parking.lista_plazas) < self.parking.plazas_pmr:

                id_plaza = len(self.parking.lista_pmr)

                self.parking.lista_pmr.append(matricula)

                id_plaza += 1

                print("Id plaza asignado: ", id_plaza)  # agregado para verificar id_plaza asignado

                self.parking.lista_ticket.append({"matricula":matricula, "id_plaza":id_plaza, "pin":pin, "fecha_entrada":fecha_entrada, "tipo_vehiculo":tipo_vehiculo})

                return f"Plaza para PMR asignada. Su número de plaza es {id_plaza}, matricula {matricula}, fecha de entrada {fecha_entrada}, y su pin es {pin}."

            else:

                return "No hay plazas para PMR disponibles."

        else:

            return "Tipo de vehículo no válido."

    def retirar_vehiculo(self,matricula, id_plaza, pin):

        fecha_salida = None

        for ticket in self.parking.lista_ticket:

            if ticket["matricula"] == matricula and ticket["id_plaza"] == id_plaza and ticket["pin"] == pin:

                fecha_salida = datetime.datetime.now()

                tiempo_estacionado = fecha_salida - ticket["fecha_entrada"]

                tiempo_estacionado_minutos = int(tiempo_estacionado.total_seconds() / 60)

                if ticket["tipo_vehiculo"] == "coche":

                    tarifa = 0.12

                elif ticket["tipo_vehiculo"] == "moto":

                    tarifa = 0.08

                elif ticket["tipo_vehiculo"] == "pmr":

                    tarifa = 0.10

                else:

                    raise ValueError("Tipo de vehículo no válido.")

                coste = tarifa * tiempo_estacionado_minutos

                self.parking.cobros.append(

                    {"matricula": matricula, "fecha_entrada": ticket["fecha_entrada"], "fecha_salida": fecha_salida,

                     "coste": coste})

                self.parking.lista_ticket.remove(ticket)

                if ticket["tipo_vehiculo"] == "coche":

                    self.parking.lista_coches.remove(matricula)

                elif ticket["tipo_vehiculo"] == "moto":


                    self.parking.lista_motos.remove(matricula)

                elif ticket["tipo_vehiculo"] == "pmr":

                    self.parking.lista_pmr.remove(matricula)

                else:

                    raise ValueError("Tipo de vehículo no válido.")

                return f"Retirado con éxito. El coste de su estancia ha sido {coste} €"

        if fecha_salida is None:

            return "No se ha encontrado el vehículo con esos datos."

        else:

            return "Error desconocido"

    def estado_plazas(self):

        estado = []

        for i in range(self.parking.plazas_coche):

            if i in self.parking.lista_coches:

                if self.parking.lista_coches[i] in self.parking.abonados:

                    estado.append(f"Plaza {i + 1} (coche): Abono ocupado")

                else:

                    estado.append(f"Plaza {i + 1} (coche): Ocupado")

            else:

                if i in self.parking.abonados:

                    estado.append(f"Plaza {i + 1} (coche): Abono libre")

                else:

                    estado.append(f"Plaza {i + 1} (coche): Libre")

        for i in range(self.parking.plazas_moto):

            if i in self.parking.lista_motos:

                if self.parking.lista_motos[i] in self.parking.abonados:

                    estado.append(f"Plaza {i + 1} (moto): Abono ocupado")

                else:

                    estado.append(f"Plaza {i + 1} (moto): Ocupado")

            else:

                if i in self.parking.abonados:

                    estado.append(f"Plaza {i + 1} (moto): Abono libre")

                else:

                    estado.append(f"Plaza {i + 1} (moto): Libre")

            for i in range(self.parking.plazas_pmr):

                if i in self.parking.lista_pmr:

                    if self.parking.lista_pmr[i] in self.parking.abonados: estado.append(f"Plaza {i + 1} (pmr): Abono ocupado")

                else:

                    estado.append(f"Plaza {i + 1} (pmr): Ocupado")

            else:

                if i in self.parking.abonados:

                    estado.append(f"Plaza {i + 1} (pmr): Abono libre")

                else:

                    estado.append(f"Plaza {i + 1} (pmr): Libre")

            return estado

    def facturacion_entre_fechas(self, fecha_entrada, fecha_salida):

        facturacion = 0

        for cobro in self.parking.cobros:

            if fecha_entrada <= cobro['fecha_entrada'] <= fecha_salida:

                facturacion += cobro['coste']

        return f"La facturación entre las fechas {fecha_entrada} y {fecha_salida} es de {facturacion} euros."


    def buscar_abonado(self, dni):

        for abonado in self.parking.abonados:

            if abonado["dni"] == dni:

                return abonado

        return None


    def retirar_abonado(self, matricula, dni, pin):

        if dni in self.parking.abonados:

            id_plaza = self.parking.abonados[dni]["id_plaza"]

            if self.parking.lista_plazas[id_plaza]["matricula"] == matricula:

                self.parking.lista_plazas[id_plaza]["estado"] = "Libre"

                return f"Su vehícula con matricula {matricula} ha sido retirado correctamente de la plaza {id_plaza}"

            else:

                return "La matricula no coincide con la plaza asignada"

        else:

            return "El Dni introducido no coincide con un abonado, lo siento"

    def consulta_abonados(self):

        abonos_temporales = []

        for abonado in self.parking.abonados:

            if hasattr(abonado, "tipo_abono") and abonado.tipo_abono == "temporal":

                cobros_realizados = 0

                for cobro in self.parking.cobros:

                    if hasattr(abonado, "dni") and abonado.dni == cobro.dni:

                        cobros_realizados += self.parking.cobros

                abonos_temporales.append({"nombre": abonado.nombre, "apellidos": abonado.apellidos, "dni": abonado.dni, "cobros": cobros_realizados})

        return abonos_temporales

    def alta_abono(self, dni, nombre, apellidos, num_tarjeta, tipo_abono, email):

        fecha_activacion = datetime.datetime.now()

        fecha_cancelacion = None

        importe = None


        if tipo_abono == "mensual":

            fecha_cancelacion = fecha_activacion + datetime.timedelta(days=30)

            importe = 25

        elif tipo_abono == "trimestral":

            fecha_cancelacion = fecha_activacion + datetime.timedelta(days=90)

            importe = 70

        elif tipo_abono == "semestral":

            fecha_cancelacion = fecha_activacion + datetime.timedelta(days=180)

            importe = 130

        elif tipo_abono == "anual":

            fecha_cancelacion = fecha_activacion + datetime.timedelta(days=365)

            importe = 200

        else:

            return "Tipo de abono no válido."


        self.parking.lista_abonos.append({"dni": dni, "nombre": nombre, "apellidos": apellidos, "num_tarjeta": num_tarjeta,

                                      "tipo_abono": tipo_abono, "fecha_activacion": fecha_activacion,

                                      "fecha_cancelacion": fecha_cancelacion, "importe": importe, "email": email})

        return f"Abono creado con éxito. Fecha de activación: {fecha_activacion}, fecha de cancelación: {fecha_cancelacion}, importe: {importe} €"

    def modificar_abono(self, dni, nombre=None, apellidos=None, num_tarjeta=None, fecha_cancelacion=None):

        for abono in self.parking.lista_abonos:

            if abono["dni"] == dni:

                if nombre:

                    abono["nombre"] = nombre

                if apellidos:

                    abono["apellidos"] = apellidos

                if num_tarjeta:

                    abono["num_tarjeta"] = num_tarjeta

                if fecha_cancelacion:

                    abono["fecha_cancelacion"] = fecha_cancelacion

                return "Abono modificado con éxito."

        return "No se ha encontrado un abono con ese DNI."

    def eliminar_abono(self, dni):

        for i, abono in enumerate(self.parking.lista_abonos):

            if abono["dni"] == dni:

                del self.parking.lista_abonos[i]

                return "Abono eliminado con éxito."

        return "No se ha encontrado un abono con ese DNI."

    def caducidad_abonos_mes(self, mes):

        abonos_caducados = []

        for abono in self.parking.lista_abonos:

            fecha_cancelacion = datetime.datetime.strptime(abono["fecha_cancelacion"], "%Y-%m-%d %H:%M:%S.%f")

            if fecha_cancelacion.month == mes:

                abonos_caducados.append(abono)

        return abonos_caducados

    def caducidad_abonos_ultimos_10dias(self, dias = 10):

        fecha_actual = datetime.datetime.now()

        fecha_limite = fecha_actual + datetime.timedelta(days=dias)

        abonos_caducando = []

        for abonado in self.parking.abonados:

            if abonado['fecha_limite'] <= fecha_limite:

                abonos_caducando.append({"nombre": abonado.nombre, "apellidos": abonado.apellidos, "dni": abonado.dni,
                                         "fecha_cancelacion": abonado['fecha_fin']})
        return abonos_caducando

        return print("Abono aducidad últimos 10 días")


