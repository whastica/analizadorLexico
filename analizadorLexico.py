# ---------------------------------------------------------------------------------------------------------------------
# Integrantes:
# Whalen Stiven Caicedo
# Juan David Beca Pillimue
# ---------------------------------------------------------------------------------------------------------------------

# 'w' ----> la 'w' crea o sobrescribe el archivo con la actulizacion que le hayamos hecho
# 'a' ----> la 'a' agrega una nueva linea
# 'x' ----> la 'x' crea un archivo desde cero
# 'r' ----> la 'r' para abrir un archivo en modo lectura

# ---------------------------------------------------------------------------------------------------------------------
# Pautas propuestas para tener un codigo funcional a la momento de traducir un pseudocodigo
# ---------------------------------------------------------------------------------------------------------------------
# Para los comentarios en el Psuedocodigo, deben los // tener un espacio con la frase a comentar
# como en este comentario, de no ser asi el traductor tomara eso como una cadena normal y no un comentario
#
# Phyton utiliza las {} para definir diccionarios de tal forma que si las utliza en el pseudocodigo para
# delimitar ciclos o bloques de instrucciones estas seras traducidadas como tal
#
# Phyton es una lp de tipado debil por lo cual no es necesario colocar el tipo de la variable al declararla en el
# pseudocodigo, sin embargo el analizador lexico traducira los siguientes tipos: entero, flotante, boolenano, cadena
# ya que al hacer un casteo estan seran de importancia
#
# Recuerde separar las palabras reservadas de los simbolos y de las variables para una mayor efectividad al momento
# de traducir el pseudocodigo
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------------------------------------------------------------
import os
# funcion valida si es comentario
def esComentario(cadena,lineasTbLex):
    # compara si la palabra enviada es igual a la primera posicion de la lista del fichero tablaLexica
    # el cual es el simbolo de comentarios
    if cadena == lineasTbLex[0][0]:
        return True
    return False

# funcion valida si es palabra reservada
def esPalReservada(cadena,lineasTbLex):
    # i=34 por que apartir de ahi empiezan las palabras reservadas en el fichero tablalexica
    i=34
    # hasta i<=59 por que ese es el numero final de lineas del archivo TablaLexica
    while i<=59:
        # auxiliar sera igual a la primera palabra en la posicion i del fichero tablaLexica
        auxiliar = lineasTbLex[i][0]
        # compara si la palabra enviada es una palabra reservada en el fichero tablaLexica
        if cadena == auxiliar:
            return True
        else:
            auxiliar = lineasTbLex[i][1]
            if cadena == auxiliar:
                return True
        i+=1
    return False

# funcion que valida si es simbolo
def esSimbolo(cadena,lineasTbLex):
    # i=0 por que apartir de ahi empiezan los simbolos reservados en el fichero tablalexica
    i=0
    # Hasta i<33 por que ese es el numero final de simbolos en el archivo TablaLexica
    while i<33:
        auxiliar = lineasTbLex[i][0]
        # compara si la palabra enviada es un simbolo en el fichero tablaLexica
        if cadena == auxiliar:
            return True
        i+=1
    return False

def esCadena(cadena,lineasTbLex):
    # i=0 por que apartir de ahi empiezan los simbolos reservados en el fichero tablalexica
    i=0
    # Hasta i<33 por que ese es el numero final de simbolos en el archivo TablaLexica
    while i<=59:
        auxiliar = lineasTbLex[i][0]
        # compara si la palabra enviada es un simbolo en el fichero tablaLexica
        if cadena != auxiliar:
            return True
        i+=1
    return False

# Funcion que traduce la plabara enviada en su equivalente segun el fichero tablalexica
def equivalencia(cadena,lineasTbLex):
    i=0
    # Recorre las primeras palabras de la tablaLexica
    while i<59:
        # Auxiliar tendra la primera palabra de la linea i de la tabla lexica
        auxiliar = lineasTbLex[i][0]
        # Si la palabra enviada es igual al auxiliar entonces devolvemos su equivalencia traducida
        # es decir la segunda palabra de la linea i del fichero tablaLexica
        if cadena == auxiliar:
            return lineasTbLex[i][1]
        i+=1
    return cadena
def escribirLinea(variableFichero,listaAux,lineasTbLex):
    with open(codigoPython, 'r') as f:
        # LineasPseudo contiene una lista de todas las lineas del pseudocodigo
        lineasCodPhyton = [linea.split() for linea in f]
        f=open(variableFichero,'a')
        #listaAuxiliarString guarda la frase guardada en la lista auxiliar
        listaAuxStr = " ".join(listaAux)
        #Escribe la frase guardada en listaAuxiliarString
        f.write(''+listaAuxStr+'\n')
        # Cierra el fichero
        f.close()

# Adiciona linea en el fichero con el codigo en python
def adicionarLinea(variableFichero,listaAux,lineasTbLex):
    with open(codigoPython, 'r') as f:
        # LineasPseudo contiene una lista de todas las lineas del pseudocodigo
        lineasCodPhyton = [linea.split() for linea in f]
        f=open(variableFichero,'a')
        #listaAuxiliarString guarda la frase guardada en la lista auxiliar
        listaAuxStr = " ".join(listaAux)
        #Escribe la frase guardada en listaAuxiliarString
        f.write(''+listaAuxStr+'\n')
        # Cierra el fichero
        f.close()

# Escribe comentario empezando el fichero en phyton donde usualmente es su descripcion
def escribirComentarioInicio(variableFichero,cadenaPseudo,lineaPseudo):
    f=open(variableFichero,'w')
    lineaPseudo.pop(0)
    restoCadena = " ".join(lineaPseudo)
    f.write(equivalencia(cadenaPseudo,lineasTbLex)+' '+restoCadena+'\n')
    f.close()
# ---------------------------------------------------------------------------------------------------------------------
# Variables Globales
# ---------------------------------------------------------------------------------------------------------------------
tablaLexica = 'tablaLexica.txt' # archivo txt de la tabla lexica
pseudocodigo = 'pseudocodigo.txt' #archvio txt del pseucodigo
codigoPython = 'traduccionPython.py' #archivo .py en donde vamos a guardar el pseudocodigo ya traducido a python

# Abrimos fichero en modo lectura
with open(pseudocodigo, 'r') as f:
    # LineasPseudo contiene una lista de todas las lineas del pseudocodigo
    lineasPseudo = [linea.split() for linea in f]

# Abrimos fichero en modo lectura
with open(tablaLexica, 'r') as f:
    # LineasTbLex contiene una lista de todas las lineas de la tabla lexica
    lineasTbLex = [linea.split() for linea in f]

'''
recorremos la lista de la tabla lexica e imprimimos cada uno de sus items guardado en lineaTbLex
for lineaTbLex in lineasTbLex:
    print(lineaTbLex[0])
    print('-----------------')

for lineaPseudo in lineasPseudo:
    print(lineaPseudo[0])
    print('-----------------')
'''

#recorremos la lista del pseudocdigo e imprimimos cada uno de sus items guardado en lineaPseudo
for lineaPseudo in lineasPseudo:
    # Si la primera palabra de la linea del fichero del psuedocodigo es un comentario
    if esComentario(lineaPseudo[0],lineasTbLex):
        # Escribira el comentario en la primer linea del Fichero en python
        escribirComentarioInicio(codigoPython,lineaPseudo[0],lineaPseudo)

    # si es una palabra reservada
    elif esPalReservada(lineaPseudo[0],lineasTbLex):
        i=0
        # Creamos una lista auxiliar vacia para ir guardando las palabras a escribir despues de la palabra reservada
        listaAux= []
        # Mientras el iterador sea menor a longitud de la lista con las palabras de la linea del Pseudocodigo
        while i<=len(lineaPseudo):
            # lista auxiliar agrgara a su lista el equivalente a la palabra en la linea del
            # pseudocodigo segun la tabla lexica
            listaAux.append(equivalencia(lineaPseudo[i-1],lineasTbLex))
            i+=1
        listaAux.pop(0)
        if os.stat(codigoPython).st_size == 0:
            escribirLinea(codigoPython,listaAux,lineasTbLex)
        # Adicionamos la linea en el fichero con el codigo en phyton
        adicionarLinea(codigoPython,listaAux,lineasTbLex)

    elif esSimbolo(lineaPseudo[0],lineasTbLex):
        i=1
        # Creamos una lista auxiliar vacia para ir guardando las palabras a escribir despues de la palabra reservada
        listaAux= []
        while i<=len(lineaPseudo):
            # lista auxiliar agrgara a su lista el equivalente a la palabra en la linea del
            # pseudocodigo segun la tabla lexica
            listaAux.append(equivalencia(lineaPseudo[i-1],lineasTbLex))
            i+=1
        # Adicionamos la linea en el fichero con el codigo en phyton
        adicionarLinea(codigoPython,listaAux,lineasTbLex)

    elif esCadena(lineaPseudo[0],lineasTbLex):
        '''
        i=1
        # Creamos una lista auxiliar vacia para ir guardando las palabras a escribir despues de la palabra reservada
        listaAux= []
        print(lineaPseudo)
        while i<=len(lineaPseudo):
            # lista auxiliar agrgara a su lista el equivalente a la palabra en la linea del
            # pseudocodigo segun la tabla lexica
            listaAux.append(equivalencia(lineaPseudo[i-1],lineasTbLex))
            i+=1
        '''
        # Adicionamos la linea en el fichero con el codigo en phyton
        adicionarLinea(codigoPython,lineaPseudo,lineasTbLex)


    

