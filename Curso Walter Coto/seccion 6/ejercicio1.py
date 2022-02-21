# Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”``

import math


a = float(input("Ingrese valor de a: "))
b = float(input("Ingrese valor de b: "))
c = float(input("Ingrese valor de c: "))

valor1 = (-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a
valor2 = (-b - math.sqrt(b**2 - 4 * a * c)) / 2 * a

print("las soluciones son", str(valor1), "y", str(valor2))
