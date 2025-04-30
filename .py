

ACTIVIDAD PYTHON


#1. EJERCICIO 1 CLASIFICADOR DE NÚMEROS
Numero_entero = (int(input("Escribe un numero:"))) #SE SOLICITA ENTRADA AL USUARIO
if Numero_entero >0:                           #SE DETERMINA SI  ES POSITIVO
    print("El numero es positivo ")
elif Numero_entero <0:
    print ("El numero es negativo")            #SE DETERMINA SI  ES NEGATIVO
else:
    print ("El numero es 0 ")                  # SI ES CERO


#2.EJERCICIO 2  APROBADO Y REPROBADO
calificacion = int(input("Ingresa tu calificacion de 0 a 100: "))
if calificacion >=60 and calificacion <=100:
    print("Aprobado")
else:
    if calificacion < 60:
      print("Reprobado")

#3. EJERCICIO 3 TABLA DE MULTIPLICAR
# Pedir al usuario que ingrese el número que quiere multiplicar
multiplica = int( input("Escribe un numero que quieras multiplicar: "))
# Realizar la multiplicación con los números del 1 al 10
for Numero_multiplica in range (1, 11):
    resultado = multiplica * Numero_multiplica #Se crea una multiplicación que va desde 1 a 10
    print (f"{multiplica}  X  {Numero_multiplica}  =  {resultado}")




#4. EJERCICIO 4 CONTADOR REGRESIVO 
# Pedir al usuario que ingrese el número que quiere multiplicar
multiplica = int( input("Escribe el número que deseas multiplicar: "))
# Realizar la multiplicación con los números del 1 al 10
for Numero_multiplica in range (1, 11):
    resultado = multiplica* Numero_multiplica #Se crea una multiplicación que va desde 1 a 10
    print (f"{multiplica}  X  {Numero_multiplica}  =  {resultado}")

#5. EJERCICIO 5 ADIVINA EL NUMERO
import random  # Importamos la librería que nos permite generar números aleatorios

numero_secreto = random.randint(1, 10)  # Generamos un número aleatorio entre 1 y 10
# Este será el número que el usuario debe adivinar

intentos_maximos = 3  # Definimos cuántos intentos tendrá el usuario

for intento in range(1, intentos_maximos + 1):  # Un bucle que se repetirá 3 veces
    # range(1, 4) generará los números 1, 2 y 3

    entrada = input(f"Intento {intento}: Adivina el número (entre 1 y 10): ")
    intento_usuario = int(entrada)  # Convertimos lo que el usuario escribió a número

    # Comparamos el intento del usuario con el número secreto
    if intento_usuario == numero_secreto:
        print("¡Correcto! Adivinaste el número.")
        break  # Salimos del bucle porque ya adivinó
    elif intento_usuario < numero_secreto:
        print("el número secreto es mayor.")
    else:
        print("el número secreto es menor.")

# Este else se ejecuta solo si el bucle no se interrumpió con un break (es decir, si no adivinó)
else:
    print(f"No lo adivinaste. El número era {numero_secreto}.")
