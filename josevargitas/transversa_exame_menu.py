import random 
from Transversal_examen import *

while True:
    print("Menú:")

    print("1. Clasificacion de sueldos y asignacion aleatoria de sueldos")
    print("2. Ver estadísticas")
    print("3. Reporte de sueldos")
    print("4. Salir del programa")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        clasificar_sueldos(sueldos)
    elif opcion == "2":
        ver_estadisticas(sueldos)
    elif opcion == "3":
        reporte_sueldos(sueldos)
    elif opcion == "4":
        salir_del_programa()
        break
    else:
        print("Opción inválida. Intente nuevamente.")

# Guardar sueldos en archivo JSON
with open("sueldos.json", "w") as f:
    json.dump(sueldos, f)