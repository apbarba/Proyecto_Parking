
from Model.Abonados import Abonados
from Menus_Main import menu_Principal, opciones_Usuario, opciones_Administrador
from Model.Parking import *
from Model.Vehiculo import Vehiculo
from Services.ParkingService import ParkingService

parking = Parking(100)

parkingService = ParkingService(parking)

abonado = Abonados("12345678A", "Juan", "Pérez", "1234567812345678", "pilarbarba", "1234")

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

                matricula = input("Por favor, introduzca la matrícula de su vehículo: ")

                tipo_vehiculo = input("Introduzca el tipo de vehiculo(coche, moto o pmr): ")

                dni = input("Introduzca su dni: ")

                vehiculo = Vehiculo(matricula, tipo_vehiculo)

                print(parkingService.depositar_abonado(vehiculo.matricula, dni))

            if opcion_Cliente == 4:

                matricula = input("Por favor, introduzca la matrícula de su vehículo: ")

                tipo_vehiculo = input("Introduzca el tipo de vehiculo(coche, moto o pmr): ")

                dni = input("Introduzca su dni por favor: ")

                vehiculo = Vehiculo(matricula, tipo_vehiculo)

                print(parkingService.retirar_abonado(vehiculo.matricula,dni))


            opciones_Usuario(parkingService)

            opcion_Cliente = int(input())

        print("Ha salido correctamente de la opción cliente")

    if opcionMenu == 2:

        opciones_Administrador(parkingService)

        opcionAdministrador = int(input())

        while opcionAdministrador != 9:

            if opcionAdministrador == 1:

                print("El estado de las plazas es: ")

                print(parkingService.estado_plazas())

                pass


            if opcionAdministrador == 2:

                fecha_inicio = input("Ingrese fecha de inicio (yyyy-mm-dd hh:mm:ss): ")

                fecha_fin = input("Ingrese fecha de fin (yyyy-mm-dd hh:mm:ss): ")

                fecha_inicio_objeto = datetime.datetime.strptime(fecha_inicio, "%Y-%m-%d %H:%M:%S")

                fecha_fin_objeto = datetime.datetime.strptime(fecha_fin, "%Y-%m-%d %H:%M:%S")

                cobros = parkingService.facturacion_entre_fechas(fecha_inicio_objeto, fecha_fin_objeto)

                print(cobros)




