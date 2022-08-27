# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print ("La palabra", texto_1, "es mayor que", texto_2)
else:
    print ("La palabra", texto_2, "es mayor que", texto_1)

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

if len(texto_1) > len(texto_2):
    print (texto_1, "tiene mayor logitud")
else:
    print (texto_2, "tiene mayor logitud")
# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

if texto_1[0] > texto_2[0]:
    print ("La primer letra de la primer palabra es mayor")
else:
    print ("La primer letra de la segunda palabra es mayor")

copia_texto_1 = texto_1  # Copia de la variable texto_1

if copia_texto_1 == texto_1:
    print ("Es igual sin lugar a dudas")
else:
    print ("Algo anda mal.upper()")

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

if copia_texto_1 == texto_2:
    print ("Algo anda mal.upper()")
else:
    print ("Es distinto sin lugar a dudas")

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
