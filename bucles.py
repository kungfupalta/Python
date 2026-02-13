# Ejercicio 7: Números del 1 al 10 con while
contador = 1
while contador <= 10:
    print(contador)
    contador += 1

print("---")

# Ejercicio 8: Números pares del 0 al 20 con for
for i in range(0, 21, 2):  # range(inicio, fin, paso)
    print(i)

# O también se puede hacer así:
# for i in range(11):  # 0 al 10
#     print(i * 2)

print("---")

# Ejercicio 9: Suma de números desde 1 hasta el número ingresado
numero = int(input("Ingresá un número: "))
suma = 0

for i in range(1, numero + 1):
    suma += i  # suma = suma + i

print(f"La suma de los números del 1 al {numero} es: {suma}")

#Ejercicio 10: Creá un programa que le pida al usuario una contraseña. Si la contraseña es "python123", mostrá "Acceso permitido". Si no, mostrá "Acceso denegado".
password_correcta = "python123"
password_ingresada = ""
while password_ingresada != password_correcta:
    password_ingresada= input("Ingrese contraseña: ")

    if password_ingresada == password_correcta:
        print("Acceso permitido")
    else:
        print("Acceso denegado")

#Ejercicio 11: Pedile al usuario un número y mostrá su tabla de multiplicar del 1 al 10. Por ejemplo, si ingresa 5:
numero = int(input("Ingrese un numero: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")

#Ejercicio 12: Creá un programa que cuente cuántos números positivos y cuántos negativos ingresó el usuario. El programa debe seguir pidiendo números hasta que el usuario ingrese 0 (el 0 termina el programa y no cuenta como positivo ni negativo).
positivos = 0
negativos = 0

print("Ingresá números (0 para terminar):")

while True:
    numero = int(input("Número: "))
    if numero == 0:
        break
    if numero > 0:
        positivos += 1
    else:
        negativos += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

#Ejercicio 13 