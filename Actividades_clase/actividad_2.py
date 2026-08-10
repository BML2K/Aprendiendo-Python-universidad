# ==========================================================
# SOLUCIÓN DE EJERCICIOS DE PRÁCTICA EN PYTHON
# ==========================================================

# 01. Suma de dos números
print("--- Ejercicio 01 ---")
num1 = 15
num2 = 4

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")


# 02. Concatenación de cadenas
print("\n--- Ejercicio 02 ---")
nombre = "luis"
apellido = "andres"
nombre_completo = nombre + " " + apellido
print(f"Nombre completo: {nombre_completo}")


# 03. Módulo par o impar
print("\n--- Ejercicio 03 ---")
numero = 7
es_par = (numero % 2 == 0)
print(f"¿El número {numero} es par?: {es_par}")


# 04. Comparaciones lógicas
print("\n--- Ejercicio 04 ---")
edad1 = 20
edad2 = 18

print(f"¿Son iguales?: {edad1 == edad2}")
print(f"¿La primera es mayor?: {edad1 > edad2}")
print(f"¿Ambas son mayores de 18?: {edad1 > 18 and edad2 > 18}")


# 05. Repetir una cadena
print("\n--- Ejercicio 05 ---")
linea_decorativa = "=" * 40
print(linea_decorativa)


# 06. Constantes físicas
print("\n--- Ejercicio 06 ---")
PI = 3.14159  # MAYÚSCULAS para constantes
radio = 5.0
area_circulo = PI * (radio ** 2)

print(f"Radio: {radio}")
print(f"Área del círculo: {area_circulo}")
