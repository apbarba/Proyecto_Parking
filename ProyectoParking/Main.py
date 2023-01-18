import self as self

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

                print((Parking.))



