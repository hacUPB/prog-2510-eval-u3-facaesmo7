print("Simulacion de desintegracion orbital de un satelite")

# Entrada de datos
altitud_actual = input("Ingrese la altitud inicial del satelite (km): ")
coeficiente_arrastre = input("Ingrese el coeficiente de arrastre inicial (ej. 0.01): ")
altitud_minima = input("Ingrese la altitud minima de seguridad (km): ")

# Conversión a float (sin try-except asumimos que el usuario lo hace bien)
altitud_actual = float(altitud_actual)
coeficiente_arrastre = float(coeficiente_arrastre)
altitud_minima = float(altitud_minima)

orbita = 0
estabilizado = False

print()
print("Iniciando simulacion...")
print("Orbita " + str(orbita) + ": Altitud = " + str(round(altitud_actual, 2)) + " km")

while True:
    orbita = orbita + 1
    altitud_perdida = coeficiente_arrastre * altitud_actual
    altitud_actual = altitud_actual - altitud_perdida
    coeficiente_arrastre = coeficiente_arrastre + 0.0001

    print("Orbita " + str(orbita) + ": Altitud = " + str(round(altitud_actual, 2)) +
          " km, Perdida = " + str(round(altitud_perdida, 4)) + " km")

    if altitud_actual <= altitud_minima:
        break

    if altitud_perdida < 0.001:
        estabilizado = True
        break

# Resultados
print()
print("Resultados")
if estabilizado:
    print("El satelite se ha estabilizado a " + str(round(altitud_actual, 2)) +
          " km despues de " + str(orbita) + " orbitas.")
else:
    print("¡El satelite ha reingresado en la atmosfera despues de " +
          str(orbita) + " orbitas!")
print("Altitud final: " + str(round(altitud_actual, 2)) + " km")
