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
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

num1 = int(input("Primer temperatura"))
num2 = int(input("Segunda temperatura:"))
num3 = int(input("Tercer temperatura"))

promedio = ((num1 + num2 + num3)/ 3)

print ("El promedio de las temperaturas es", promedio)

if ((num1 >= num2) and (num1 >= num3) and (num2 >= num3)):
    print ("La temperatura maxima es:", num1, "la intermedia es", num2, "y la minimina es", num3)
elif ((num1 >= num2) and (num1 >= num3) and (num2 <= num3)):
    print ("La temperatura maxima es:",num1, "la intermedia es", num3, "y la minimina es", num2)
elif ((num1 <= num2) and (num1 >= num3) and (num2 >= num3)):
    print ("La temperatura maxima es:", num2, "la intermedia es", num1, "y la minimina es", num3)
elif ((num1 <= num2) and (num1 <= num3) and (num2 >= num3)):
    print ("La temperatura maxima es:", num2, "la intermedia es", num3, "y la minimina es", num1)
elif ((num1 <= num2) and (num1 <= num3) and (num2 <= num3)):
    print ("La temperatura maxima es:", num3, "la intermedia es", num2, "y la minimina es", num1)
elif ((num1 >= num2) and (num1 <= num3) and (num2 <= num3)):
    print ("La temperatura maxima es:", num3, "la intermedia es", num1, "y la minimina es", num2)
