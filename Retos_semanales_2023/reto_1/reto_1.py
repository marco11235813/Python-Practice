"""1-
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"."""

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
"""Marco Caro PYandDT"""
# Generamos los valores

def elementos()-> list|tuple:

    muestra= list(range(1,101))
    sustituciones= ['fizz','buzz','fizzbuzz' ]

    return muestra, sustituciones



# Creamos el convertidor
def convertidor()->list:

    numeros,cambios= elementos()
    for idx,num in enumerate(numeros):
        if num%3 == 0 and num%5 == 0:
            numeros[idx]= cambios[2]
        elif num%3 == 0:
            numeros[idx]= cambios[0]
        elif num%5 == 0:
            numeros[idx]= cambios[1]
        else:
            continue

    return numeros


def main():

    convertir= convertidor()
    print(convertir)
    return 

if __name__ == '__main__':
    main()