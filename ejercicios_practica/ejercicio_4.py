# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print (texto_1, "es mayor")
else: 
    print (texto_2, "es mayor")

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.

tex_1 = int(texto_1)
tex_2 = int(texto_2)

# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda

if tex_1 > tex_2:
    print (tex_1, "es mayor")
else: 
    print (tex_2, "es mayor")

# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

print ("En respuesta a la pregunta planteada:")
print (''' Por en el codigo ASCII, el caracter 5 tiene asignado el numero
53 mientras que el 7 tiene asignado el numero 55, siendo esta la 
comparacionreal que realiza python''')