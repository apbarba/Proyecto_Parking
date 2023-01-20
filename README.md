# Proyecto_Parking
## Entorno de desarrollo y ejecución:

Para el desarrollo del proyecto, se ha utilizado el entorno de desarrollo **PyCharm*. Para su ejecución en dicho entorno, abrimos el proyecto y,
en la barra superior, en la parte derecha, en los primeros iconos, seleccionamos la flecha de ejecutar. Pero para ello necesitamos estar antes dentro del archivo "Main.py" o bien si queremos mostrar rápidamente que el proyecto va, se ejecutará el archivo llamado "MainMenetira.py" el cual tiene datos ya inicializados de forma más feilla a vista.

## Organización del proyecto:
En este proyecto se muestran dos carpetas, el proyecto final se encuentra en la carpeta llamada **ProyectoParking**, la carpeta Parking fue con la que lo comencé, pero decidí a empezar de nuevo y hacerlo mejor

Se ha utilizado en este proyecto:

- **pickle**: Hemos utilizado la base de datos de pickle para que se nos guarde los datos introducidos.

## Zonas de la aplicación:
### Cliente:
- **Depositar_Vehiculo**: Deposita el vehiculo sin ser de un abonado
- **Retirar_Vehiculo**: Retira el vehiculo sin ser de un abonado
- **Depositar_Abonados(asignar_plaza)**: Se deposita un vehiculo de un abonado
- **Retirar_abonado**: Se retira un vehiculo de un abonado

### Administrador:
- **Estado_parking**: Se muestra las plazas libres, ocupadas de abonados y no abonados
- **Facturarización**: Saber los cobros realizados entre dos fechas
- **Consultar_Abonados**: Se muestra la lista de abonados
- **Alta_abono**: Se crea un abono(mensual, trimestral, semanal o anual)
- **Modificar_abono**: Se modifica un abono a base de buscarlo a través del dni
- **Baja_abono**: Se da de baja un abono buscado por dni
- **Caducidad_mes**: El sistema solicita un mes y nos informa de los abonos que caducan en ese mes.
- **Caducidad_10Dias**: El programa informa por consola de los abonos que caducan en los siguientes 10 días a la fecha actual.

