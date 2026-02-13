#ejercicio 4
edad = int(input("Cuantos años tenes? "))
if edad >=18:
        print("Ya puedes votar")
else:
        print("Aun no podes votar")


#ejercicio 5

numero = int(input("Introduci un numero:"))

if numero >0:
        print("Positivo")
elif numero <0:
        print("Negativo")
else:
        print("Cero")
        
#ejercicio 6
edad = int(input("Introduci tu edad: "))

if edad <= 12:
    print("Debes pagar: $300")
elif edad <= 64:  # Si llegó acá, ya sabemos que es > 12
    print("Debes pagar: $500")
else:  # Si llegó acá, es >= 65
    print("Debes pagar: $350")