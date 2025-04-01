

# 1. Información del usuario
# Se pide al usuario que ingrese su título (Sr. o Sra.), nombre y apellido.
# Se valida que el título sea correcto antes de continuar.
while True:
    titulo = input("Ingrese su título (Sr. o Sra.): ")
    if titulo == "Sr." or titulo == "Sra.":
        break
    print("Título no válido. Intente de nuevo.")

# Se solicita el nombre y apellido del usuario y se le da la bienvenida.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print(f"{titulo} {nombre} {apellido}, ¡Bienvenido a FastFast Airlines!")

# 2. Selección de vuelo
# Se definen las ciudades disponibles y las distancias entre ellas.
ciudades = ["Medellín", "Bogotá", "Cartagena"]
distancias = {
    ("Medellín", "Bogotá"): 240,
    ("Medellín", "Cartagena"): 461,
    ("Bogotá", "Cartagena"): 657
}

# Se pide la ciudad de origen y se valida que sea una opción válida.
print("Ciudades disponibles: Medellín, Bogotá, Cartagena")
while True:
    origen = input("Ingrese ciudad de origen: ")
    if origen == "Medellín" or origen == "Bogotá" or origen == "Cartagena":
        break
    print("Ciudad no válida. Intente de nuevo.")

# Se pide la ciudad de destino y se valida que sea distinta de la ciudad de origen.
while True:
    destino = input("Ingrese ciudad de destino: ")
    if (destino == "Medellín" or destino == "Bogotá" or destino == "Cartagena") and destino != origen:
        break
    print("Ciudad no válida o igual al origen. Intente de nuevo.")

# Se solicita el día de la semana y se valida que sea un día válido.
while True:
    dia_semana = input("Ingrese el día de la semana (lunes a domingo): ")
    if dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "miércoles" or dia_semana == "jueves" or dia_semana == "viernes" or dia_semana == "sábado" or dia_semana == "domingo":
        break
    print("Día de la semana no válido. Intente de nuevo.")

# Se solicita el día del mes y se valida que esté en el rango de 1 a 30 sin usar 'try'.
while True:
    dia_mes = input("Ingrese el día del mes (1-30): ")
    if dia_mes.isdigit():
        dia_mes = int(dia_mes)
        if 1 <= dia_mes <= 30:
            break
    print("Día fuera de rango o no válido. Intente de nuevo.")

# Se obtiene la distancia entre las ciudades seleccionadas.
distancia = 0
if (origen == "Medellín" and destino == "Bogotá") or (origen == "Bogotá" and destino == "Medellín"):
    distancia = 240
elif (origen == "Medellín" and destino == "Cartagena") or (origen == "Cartagena" and destino == "Medellín"):
    distancia = 461
elif (origen == "Bogotá" and destino == "Cartagena") or (origen == "Cartagena" and destino == "Bogotá"):
    distancia = 657

# Se calcula el precio del billete según la distancia y el día de la semana.
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
# Se pregunta al usuario su preferencia de asiento.
while True:
    preferencia = input("¿Prefiere asiento en el pasillo, ventana o sin preferencia? ")
    if preferencia == "pasillo" or preferencia == "ventana" or preferencia == "sin preferencia":
        break
    print("Opción no válida. Intente de nuevo.")

# Se asigna la letra del asiento según la preferencia del usuario.
if preferencia == "pasillo":
    letra_asiento = "C"
elif preferencia == "ventana":
    letra_asiento = "A"
else:
    letra_asiento = "B"

# Se asigna un número de asiento de manera secuencial, partiendo del 1 y aumentando con cada pasajero.
numero_asiento = 1  # Para el primer pasajero

# 4. Salida
# Se muestra la información completa de la reserva al usuario.
print("\n--- RESERVA CONFIRMADA ---")
print(f"Pasajero: {titulo} {nombre} {apellido}")
print(f"Origen: {origen}")
print(f"Destino: {destino}")
print(f"Fecha de vuelo: {dia_semana.capitalize()} {dia_mes}")
print(f"Precio del boleto: ${precio:,.0f}")
print(f"Asiento asignado: {numero_asiento}{letra_asiento}")
