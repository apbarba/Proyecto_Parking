import pickle

from Model.Abonados import Abonados
from Model.Parking import Parking
from Services.ParkingService import ParkingService

if __name__ == "__main__":


    parking = Parking(100)

    parking_service = ParkingService(parking)

    # Crear un abonado
    abonado = Abonados("12345678A", "Juan", "Pérez", "1234567812345678", "pilarbarba", "1234")

    with open('parking_service.pickle', 'wb') as handle:
        pickle.dump(parking_service, handle, protocol=pickle.HIGHEST_PROTOCOL)

        # Cargar la instancia desde el archivo usando pickle
    with open('parking_service.pickle', 'rb') as handle:
        parking_service_loaded = pickle.load(handle)

    # Asignar plaza al abonado
    id_plaza = parking_service.asignar_plaza(abonado, "coche")
    print(
        f"Plaza asignada al abonado con matrícula {abonado.matricula} y DNI {abonado.dni}, con el número de plaza {id_plaza}")

    # Depositar un vehículo no abonado
    result = parking_service.depositar_vehiculo("1234ABC", "coche")
    print(result)

    # Retirar un vehículo
    result = parking_service.retirar_vehiculo("1234ABC", 1, 1234)
    print(result)

    # Buscar un abonado
    result = parking_service.buscar_abonado("12345678A")
    print(result)

    # Consultar abonos
    result = parking_service.consulta_abonados()
    print(result)

    # Alta abono
    abonado = parking_service.alta_abono("12345678A", "Ana", "Barba", "1234567812345678", "mensual",
                                         "aba@mail.com")
    print(abonado)

    # Modificar abono
    result = parking_service.modificar_abono("12345678A", "Ana", "Barba", "1234567812345678", "semestral")
    print(result)

    # Baja abono
    result = parking_service.eliminar_abono("12345678A")
    print(result)

    # Caducidad de abonos
    result = parking_service.caducidad_abonos_mes("Enero")
    print(result)
    result = parking_service_loaded.caducidad_abonos_ultimos_10dias(10)
    print(result)

    #Estado de las plazas disponibles
    print(parking_service.estado_plazas())



