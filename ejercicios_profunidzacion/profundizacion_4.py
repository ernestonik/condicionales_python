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

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

texto_1 = str(input("Ingrese Texto 1: "))
texto_2 = str(input("Ingrese Texto 2: "))
texto_3 = str(input("Ingrese Texto 3: "))

opcion = 0
print('''
    A ver, ¿qué queres hacer?
    1) Ordenar por orden alfabético.
    2) Ordenar por cantidad de letras.
''')

opcion = int(input("Elige una opción: ") )

# por primer letra
if opcion == 1:
    print (" ")
if (texto_1[0] >= texto_2[0]) and (texto_1[0] >= texto_3[0]) and (texto_2[0] >= texto_3[0]):
    print (texto_1, texto_2, texto_3)
elif (texto_1[0] >= texto_2 [0]) and (texto_1[0] >= texto_3[0]) and (texto_2[0] >= texto_3 [0]):
    print (texto_1, texto_2, texto_3)
elif (texto_1[0] >= texto_2 [0]) and (texto_1[0] >= texto_3[0]) and (texto_2[0] <= texto_3 [0]):
    print (texto_1, texto_3, texto_2)
elif (texto_1[0] <= texto_2 [0]) and (texto_1[0] >= texto_3[0]) and (texto_2[0] >= texto_3 [0]):
    print (texto_2, texto_1, texto_3)
elif (texto_1[0] <= texto_2 [0]) and (texto_1[0] <= texto_3[0]) and (texto_2[0] >= texto_3 [0]):
    print (texto_2, texto_3, texto_1)
elif (texto_1[0] >= texto_2 [0]) and (texto_1[0] <= texto_3[0]) and (texto_2[0] <= texto_3 [0]):
    print (texto_3, texto_1, texto_2)
elif (texto_1[0] <= texto_2 [0]) and (texto_1[0] <= texto_3[0]) and (texto_2[0] <= texto_3 [0]):
    print (texto_3, texto_1, texto_2)


tx1 = str(len(texto_1))
tx2 = str(len(texto_2))
tx3 = str(len(texto_3))


if opcion == 2:
    print (" ")
if (tx1 >= tx2) and (tx1 >= tx3) and (tx2 >= tx3):
    print (texto_1, texto_2, texto_3)
elif (tx1 >= tx2) and (tx1 >= tx3) and (tx2 <= tx3):
    print (texto_1, texto_3, texto_2)
elif (tx1 <= tx2) and (tx1 >= tx3) and (tx2 >= tx3):
    print (texto_2, texto_1, texto_3)
elif (tx1 <= tx2) and (tx1 <= tx3) and (tx2 >= tx3):
    print (texto_2, texto_3, texto_1)
elif (tx1 >= tx2) and (tx1 <= tx3) and (tx2 <= tx3):
    print (texto_3, texto_1, texto_2)
elif (tx1 <= tx2) and (tx1 <= tx3) and (tx2 <= tx3):
    print (texto_3, texto_2, texto_1)

print ("Este si que fue dificil!")
