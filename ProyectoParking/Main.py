
from Model.Abonados import Abonados
from Menus_Main import menu_Principal, opciones_Usuario
from Model.Parking import *
from Model.Vehiculo import Vehiculo
from Services.ParkingService import ParkingService

parking = Parking(100)

parkingService = ParkingService(parking)


abonados = Abonados('1234A', 'Ana', 'Barba', '12345', 'Temporal', 'pilar')

menu_Principal()

opcionMenu = int(input())

while opcionMenu != 0:

    if opcionMenu == 1:

        opciones_Usuario(parkingService)

        opcion_Cliente = int(input())

        while opcion_Cliente != 0:

            if opcion_Cliente == 1:

                matricula = input("Por favor, introduzca la matrícula de su vehículo: ")

                tipo_vehiculo = input("Introduzca el tipo de vehiculo(coche, moto o pmr): ")

                vehiculo = Vehiculo(matricula, tipo_vehiculo)

                print(parkingService.depositar_vehiculo(vehiculo.matricula, vehiculo.tipo_vehiculo))

                print(parkingService.estado_plazas())

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

                print(abonados.depositar_abonado(vehiculo.matricula, abonados.dni))

            if opcion_Cliente == 4:

                matricula = input("Por favor, introduzca la matrícula de su vehículo: ")

                tipo_vehiculo = input("Introduzca el tipo de vehiculo(coche, moto o pmr): ")

                dni = input("Introduzca su dni por favor: ")

                vehiculo = Vehiculo(matricula, tipo_vehiculo)

                print(abonados.retirar_abonado(vehiculo.matricula, abonados.dni))

            if opcion_Cliente == 5:

                fecha_inicio = input("Ingrese fecha de inicio (yyyy-mm-dd hh:mm:ss): ")

                fecha_fin = input("Ingrese fecha de fin (yyyy-mm-dd hh:mm:ss): ")

                fecha_inicio_objeto = datetime.datetime.strptime(fecha_inicio, "%Y-%m-%d %H:%M:%S")

                fecha_fin_objeto = datetime.datetime.strptime(fecha_fin, "%Y-%m-%d %H:%M:%S")

                cobros = parkingService.facturacion_entre_fechas(fecha_inicio_objeto, fecha_fin_objeto)

                print(cobros)

            opciones_Usuario(parkingService)

            opcion_Cliente = int(input())




