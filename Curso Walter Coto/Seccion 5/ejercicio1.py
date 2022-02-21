# Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:
# • Imprima los dos primeros caracteres.
# • Imprima los tres últimos caracteres.
# • Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca
# • Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh
# • Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.

from typing import Text


Texto = "Te quiero solo como amigo"
print(Texto[0:2])
print(Texto[-3:])

Cada2 = str()
for index, char in enumerate(Texto):
    if index % 2 == 0:
        Cada2 = Cada2 + char
print(Cada2)

volteado = str()
for char in Texto:
    volteado = char + volteado
print(volteado)

print(Texto + volteado)
