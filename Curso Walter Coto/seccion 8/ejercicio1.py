# Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal

import re


letra = input("ingrese letra a revisar :")
if re.match("[aeiou]", letra):
    print("Letra ingresada es una vocal")
else:
    print("letra ingresada no es una vocal")
2
