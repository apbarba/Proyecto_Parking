import pickle

from Model.Abonados import Abonados
from Menus_Main import menu_Principal, opciones_Usuario, opciones_Administrador
from Model.Parking import *
from Model.Vehiculo import Vehiculo
from Services.ParkingService import ParkingService

parking = Parking(100)

parkingService = ParkingService(parking)

abonado = Abonados("12345678A", "Ana", "Barba", "1234567812345678", "pilarbarba", "1234")

with open('parkingService.pickle', 'wb') as handle:
    pickle.dump(parkingService, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('parkingService.pickle', 'rb') as handle:
    parking_service_loaded = pickle.load(handle)

menu_Principal()

opcionMenu = int(input())

while opcionMenu != 0:

    if opcionMenu == 1:

        opciones_Usuario(parkingService)

        opcion_Cliente = int(input())

        while opcion_Cliente != 5:

            if opcion_Cliente == 1:

                matricula = input("Por favor, introduzca la matrícula de su vehículo: ")

                tipo_vehiculo = input("Introduzca el tipo de vehiculo(coche, moto o pmr): ")

                vehiculo = Vehiculo(matricula, tipo_vehiculo)

                print(parkingService.estado_plazas())

                print(parkingService.depositar_vehiculo(vehiculo.matricula, vehiculo.tipo_vehiculo))

            if opcion_Cliente == 2:

                matricula = input("Por favor, introduzca la matrícula de su vehículo: ")

                id_plaza = input("Pot favor, introduce el id de su plaza asignada: ")

                pin = input("Por favor, introduzca el pin que se le generó antes: ")

                print(parkingService.retirar_vehiculo(matricula, id_plaza, pin))

            if opcion_Cliente == 3:

                result = parkingService.asignar_plaza(abonado, "coche")

                print(f"Plaza asignada al abonado con matrícula {abonado.matricula} y DNI {abonado.dni}, con el número de plaza {id_plaza}")

            if opcion_Cliente == 4:

                matricula = input("Por favor, introduzca la matrícula de su vehículo: ")

                tipo_vehiculo = input("Introduzca el tipo de vehiculo(coche, moto o pmr): ")

                dni = input("Introduzca su dni por favor: ")

                vehiculo = Vehiculo(matricula, tipo_vehiculo)

                print(parkingService.retirar_abonado(vehiculo.matricula,dni))


            opciones_Usuario(parkingService)

            opcion_Cliente = int(input())

        print("Ha salido correctamente de la opción cliente")

    elif opcionMenu == 2:

        opciones_Administrador(parkingService)

        opcionAdministrador = int(input())

        while opcionAdministrador != 9:

            if opcionAdministrador == 1:

                print("El estado de las plazas es: ")

                print(parkingService.estado_plazas())


            elif opcionAdministrador == 2:

                fecha_inicio = "2023-01-23 12:23:10"

                fecha_fin = "2023-01-23 13:00:11"

                fecha_inicio_objeto = datetime.datetime.strptime(fecha_inicio, "%Y-%m-%d %H:%M:%S")

                fecha_fin_objeto = datetime.datetime.strptime(fecha_fin, "%Y-%m-%d %H:%M:%S")

                cobros = parkingService.facturacion_entre_fechas(fecha_inicio_objeto, fecha_fin_objeto)

                print(cobros)

            elif opcionAdministrador == 3:

                result = parkingService.consulta_abonados()

                print(result)

            elif opcionAdministrador == 4:

                dni = input("Introduzca su dni por favor: ")

                nombre = input("Introduzca su nombre por favor: ")

                apellido = input("Introduzca su apellido por favor: ")

                num_tarjeta = input("Introduzca su número de tarjeta: ")

                tipo_abono = input("Introduzca el tipo de abono que desea (mensual, trimestral, semestral o anual): ")

                email = input("Introduzca su email por favor: ")

                abonado = parkingService.alta_abono(dni, nombre, apellido, num_tarjeta, tipo_abono, email)

                print(abonado)

            elif opcionAdministrador == 5:

                dni = input("Introduzca su dni a cambiar: ")

                nombre = input("Introduzca su nombre a cambiar: ")

                apellido = input("Introduzca su apellido a cambiar:")

                num_tarjeta = input("Introduzca su número de tarjeta")

                tipo_abono = input("Introduzca su tipo de abono a cambiar: ")

                modificado = parkingService.modificar_abono(dni, nombre, apellido, num_tarjeta, tipo_abono)

                print(modificado)

            elif opcionAdministrador == 6:


                dniBaja = input("Introduzca su dni para darse de baja")

                result = parkingService.eliminar_abono(dniBaja)

                print(result)

            elif opcionAdministrador == 7:

                mes = input("Introduzca el mes: ")

                result = parkingService.caducidad_abonos_mes(mes)

                print(result)

            elif opcionAdministrador == 8:

                result = parking_service_loaded.caducidad_abonos_ultimos_10dias(10)

                print(result)

            else:

                print("Opción incorrecta")

            opciones_Administrador(parkingService)

            opcionAdministrador = int(input())

        print("Atrá al menú Principal")

    else:

        print("Opción incorrecta")

    menu_Principal()

    opcionMenu = int(input())

print("Espero que le haya servido y disfrute")


