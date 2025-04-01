print("Simulación de desintegración orbital de un satélite")

# Obtener datos de entrada
altitud_actual = float(input("Ingrese la altitud inicial del satélite (km): "))
coeficiente_arrastre = float(input("Ingrese el coeficiente de arrastre inicial (ej. 0.01): "))
altitud_minima = float(input("Ingrese la altitud mínima de seguridad (km): "))

orbita = 0
estabilizado = False

print()
print("Iniciando simulación...")
print(f"Órbita {orbita}: Altitud = {altitud_actual:.2f} km")

while True:
    orbita += 1
    altitud_perdida = coeficiente_arrastre * altitud_actual
    altitud_actual -= altitud_perdida
    coeficiente_arrastre += 0.0001
    
    print(f"Órbita {orbita}: Altitud = {altitud_actual:.2f} km, Pérdida = {altitud_perdida:.4f} km")
    
    if altitud_actual <= altitud_minima:
        break
    
    if altitud_perdida < 0.001:
        estabilizado = True
        break

print()
print("Resultados")
if estabilizado:
    print(f"El satélite se ha estabilizado a {altitud_actual:.2f} km después de {orbita} órbitas.")
else:
    print(f"¡El satélite ha reingresado en la atmósfera después de {orbita} órbitas!")
print(f"Altitud final: {altitud_actual:.2f} km")