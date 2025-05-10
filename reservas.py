# 1. Información del usuario
while True:
    titulo = input("Ingrese su título (Sr. o Sra.): ")
    if titulo == "Sr." or titulo == "Sra.":
        break
    print("Título no válido. Intente de nuevo.")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print(titulo + " " + nombre + " " + apellido + ", ¡Bienvenido a FastFast Airlines!")

# 2. Selección de vuelo
ciudades = ["Medellín", "Bogotá", "Cartagena"]

print("Ciudades disponibles: Medellín, Bogotá, Cartagena")
while True:
    origen = input("Ingrese ciudad de origen: ")
    if origen == "Medellín" or origen == "Bogotá" or origen == "Cartagena":
        break
    print("Ciudad no válida. Intente de nuevo.")

while True:
    destino = input("Ingrese ciudad de destino: ")
    if (destino == "Medellín" or destino == "Bogotá" or destino == "Cartagena") and destino != origen:
        break
    print("Ciudad no válida o igual al origen. Intente de nuevo.")

dias_validos = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
while True:
    dia_semana = input("Ingrese el día de la semana (lunes a domingo): ")
    if dia_semana in dias_validos:
        break
    print("Día de la semana no válido. Intente de nuevo.")

# Validar día del mes sin .isdigit() y sin try-except
while True:
    dia_mes = input("Ingrese el día del mes (1-30): ")
    caracteres_validos = "0123456789"
    es_numero = True
    for caracter in dia_mes:
        if caracter not in caracteres_validos:
            es_numero = False
            break
    if es_numero:
        dia_mes = int(dia_mes)
        if 1 <= dia_mes <= 30:
            break
    print("Día fuera de rango o no válido. Intente de nuevo.")

# Determinar la distancia
if (origen == "Medellín" and destino == "Bogotá") or (origen == "Bogotá" and destino == "Medellín"):
    distancia = 240
elif (origen == "Medellín" and destino == "Cartagena") or (origen == "Cartagena" and destino == "Medellín"):
    distancia = 461
else:
    distancia = 657  # Bogotá <-> Cartagena

# Calcular el precio
if distancia < 400:
    if dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "miércoles" or dia_semana == "jueves":
        precio = 79900
    else:
        precio = 119900
else:
    if dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "miércoles" or dia_semana == "jueves":
        precio = 156900
    else:
        precio = 213000

# 3. Asignación de asiento
while True:
    preferencia = input("¿Prefiere asiento en el pasillo, ventana o sin preferencia? ")
    if preferencia == "pasillo" or preferencia == "ventana" or preferencia == "sin preferencia":
        break
    print("Opción no válida. Intente de nuevo.")

if preferencia == "pasillo":
    letra_asiento = "C"
elif preferencia == "ventana":
    letra_asiento = "A"
else:
    letra_asiento = "B"

numero_asiento = 1  # fijo, sin random

# 4. Salida
print("")
print("--- RESERVA CONFIRMADA ---")
print("Pasajero: " + titulo + " " + nombre + " " + apellido)
print("Origen: " + origen)
print("Destino: " + destino)
print("Fecha de vuelo: " + dia_semana.capitalize() + " " + str(dia_mes))
print("Precio del boleto: $" + str(precio))
print("Asiento asignado: " + str(numero_asiento) + letra_asiento)
