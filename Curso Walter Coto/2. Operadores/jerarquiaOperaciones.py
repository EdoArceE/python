num1 = 100
num2 = 50
num3 = 25
num4 = 10
print(num1 + num2)
print(num1 + num2 * num3)  # se  realiza primero la multiplicacione
print((num1 + num2) * num3)  # se  realiza primero la suma
print((num1 + num2) * num3 - num4)  # se  realiza al final la resta
print((num1 + num2) * (num3 - num4))  # se  realiza al final la multiplicacion
print(
    (num1 + num2) * (num3 - num4) / (num1 - num4)
)  # se  realiza al final la multiplicacion
