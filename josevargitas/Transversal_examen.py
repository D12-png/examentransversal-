import json
import random

# Nombres de los empleados
empleados = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Hernandez"]

# Función para asignar sueldos aleatorios
def asignar_sueldos():
    sueldos = {}
    for empleado in empleados:
        sueldo = int(random.uniform(300000, 2500000))
        sueldos[empleado] = sueldo
    return sueldos

# Función para clasificar sueldos
def clasificar_sueldos(sueldos):
    print("Lista de empleados con su sueldo:")
    for empleado, sueldo in sueldos.items():
        print(f"{empleado}: ${sueldo:.2f}")

# Función para ver estadísticas
def ver_estadisticas(sueldos):
    sueldos_ordenados = sorted(sueldos.values())
    sueldo_mas_alto = sueldos_ordenados[-1]
    sueldo_mas_bajo = sueldos_ordenados[0]
    promedio_sueldos = sum(sueldos.values()) / len(sueldos)
    print("Estadísticas:")
    print(f"Sueldo más alto: ${sueldo_mas_alto:.2f}")
    print(f"Sueldo más bajo: ${sueldo_mas_bajo:.2f}")
    print(f"Promedio de sueldos: ${promedio_sueldos:.2f}")

# Función para reporte de sueldos
def reporte_sueldos(sueldos):
    print("Reporte de sueldos:")
    for empleado, sueldo in sueldos.items():
        descuento_salud = sueldo * 0.07
        descuento_afp = sueldo * 0.12
        sueldo_liquido = sueldo - descuento_salud - descuento_afp
        print(f"{empleado}:")
        print(f"  Sueldo bruto: ${sueldo:.2f}")
        print(f"  Descuento salud: ${descuento_salud:.2f}")
        print(f"  Descuento AFP: ${descuento_afp:.2f}")
        print(f"  Sueldo líquido: ${sueldo_liquido:.2f}")

# Función para salir del programa
def salir_del_programa():
    print("Gracias por utilizar el programa.")
    print("JoseVargas - 21320374-6")

# Programa principal
sueldos = asignar_sueldos()