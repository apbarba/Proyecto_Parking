import self as self

from Abonados import Abonados
from Menus_Main import menu_Principal, opciones_Usuario
from Parking import Parking
from Vehiculo import Vehiculo


parking = Parking(100)

menu_Principal()

opcionMenu = int(input())

while opcionMenu != 0:

    if opcionMenu == 1:

        opciones_Usuario(self)

        opcion_Cliente = int(input())

        while opcion_Cliente != 0:

            if opcion_Cliente == 1:

                matricula = input("Por favor, introduzca la matrícula de su vehículo: ")

                Vehiculo.tipo_vehiculo = input("Introduzca el tipo de vehiculo(coche, moto o pmr): ")

                print(Parking.depositar_vehiculo(matricula, Vehiculo.tipo_vehiculo)) #No pilla el tipo_vehiculo

            if opcion_Cliente == 2:

                matricula = input("Por favor, introduzca la matrícula de su vehículo: ")

                id_plaza = input("Pot favor, introduce el id de su plaza asignada: ")

                pin = input("Por favor, introduzca el pin que se le generó antes: ")

                print(Parking.retirar_vehiculo(matricula, id_plaza, pin)) #Arreglar ese método para que me lo pille

            if opcion_Cliente == 3:

                matricula = input("Por favor, introduzca la matrícula de su vehículo: ")

                dni = input("Introduzca su dni por favor: ")

                nombre = input("Por favor, su nombre: ")

                apellidos = input("Por favor sus apellidos: ")

                tarjeta_credito = input("Por favor su número de tarjeta de crédito: ")

                tipo_abono = input("Por favor, indique su tipo de abono: ")

                email = input("Por favor su email: ")

                tipo_vehiculo = input("Introduzca el tipo de vehiculo(coche, moto o pmr): ")

                abonados = Abonados(dni, nombre, apellidos, tarjeta_credito, tipo_abono, email)

                print(Abonados.depositar_abonado(matricula, parking))

            if opcion_Cliente == 4:

                Abonados.matricula = input("Por favor, introduzca la matrícula de su vehículo: ")

                dni = input("Introduzca su dni por favor: ")

                print(Abonados.retirar_abonado(Abonados.matricula, dni))

            menu_Principal()

            opcionMenu = int(input())

        print("Salió correctamente")


