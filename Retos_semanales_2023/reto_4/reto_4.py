"""4-Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)\n"""

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

"""Marco Caro PYandDT\n"""



def generador_contraseña()->str:

    import random


    abecd= ['a','b','c','d','e','f'                            
            ,'g','h','i','j','k','l',            
            'm','n','ñ','o','p','q','r'
            ,'s','t','u','v','w','x','y','z']
    mayusculas= [x.upper() for x in abecd]
    numeros= list(range(0,10))
    simbolos= ['!','#','$','"','&','/','(',')','=','?','¡',',','¿','/','\\',']','[','{','}','-','_','|','°',']']
    acciones= [abecd,mayusculas,numeros,simbolos]

    try:
        longitud= int(input('Ingrese longitud de contraseña (entre 8 y 16 caracteres): '))
        if longitud < 8 or longitud > 16:
           return 'La longitud debe ser de entre 8 a 16 caracteres'
    except ValueError:
       print('Valor incorrecto')
       return
    
    print('Seleccione el numero de los parametros a aplicar(separados por coma):\n\n1-Habilitar mayusculas\n2-Habilitar numeros\n3-Habilitar simbolos\n\n')
    opciones= input('--------> ').split(',')
    parametros= [int(x) for x in opciones]

    contador= 0
    contraseña= []
    muestra= abecd.copy()
    
    for num in parametros:
       random.shuffle(muestra)
       muestra += acciones[num]

    while contador != longitud:
        contador +=1
        caracter= random.choice(muestra)
        contraseña.append(str(caracter))

    random.shuffle(contraseña)
    print(''.join(contraseña))
    return 


def main():
    
    password= generador_contraseña()
    print(password)
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------