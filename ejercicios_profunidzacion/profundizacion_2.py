# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

num1 = int(input("Primer numero:"))
num2 = int(input("Segundo numero:"))
num3 = int(input("Tercer numero:"))

num11 = num1 % 2
num22 = num2 % 2
num33 = num3 % 2

if num11 == 0:
    print (num1, "Par")   
else:
    print (num1, "Impar")

if num22 == 0:
    print (num2, "Par")   
else:
    print (num2, "Impar")

if num33 == 0:
    print (num3, "Par")   
else:
    print (num3, "Impar")