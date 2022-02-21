# Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

palabra1 = input("Ingrese primera palabra: ")
palabra2 = input("Ingrese segunda palabra: ")

terminacion1 = palabra1[-3:]
terminacion2 = palabra2[-3:]

if terminacion1 == terminacion2:
    print("Riman")
else:
    terminacion1 = terminacion1[1:]
    terminacion2 = terminacion2[1:]
    if terminacion1 == terminacion2:
        print("Riman un poco")
    else:
        print("no riman")
