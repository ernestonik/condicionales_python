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
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

num1 = int(input("Primer numero:"))
num2 = int(input("Segundo numero:"))

resta = num1 - num2
print("La diferencia entre", num1, "y", num2, "es igual a", resta)

if num1 < 0:
    print (num1, "es negativo")
elif num1 == 0:
    print (num1, "es igual a cero")
else:
    print (num1, "es positivo")

if num2 < 0:
    print (num2, "es negativo")
elif num2 == 0:
    print (num2, "es igual a cero")
else:
    print (num2, "es positivo")