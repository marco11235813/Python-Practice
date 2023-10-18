"""* 8-Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts:
 *   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas
 *   y crear el algoritmo seleccionador:
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia."""


#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

"""Marco Caro PYandDT\n"""

def preguntas()->str:
    try:
        preg1= int(input('Que prefieres?:\n\n1-Tener mucho dinero\n2- Estudiar mucho\n3- Jugar con mis amigos\n4- Estar de vago\n------> '))
        preg2= int(input('\nDe estas opciones.. que te describe mas?:\n1- La tranquilidad es lo mas importante\n2- Prefiero Estar con mis amigos\n3- No me gustan los muggles\n4- No me gusta que me molesten\n------> '))
        preg3= int(input('\nTe consideras....:\n1- Astuto\n2- Valiente\n3- Con suerte\n4- El mejor\n------> '))
        preg4= int(input('\nQue deseas ser en el futuro?:\n1-Gobernante/jefe\n2- Erudito/Cientifico\n3- Deportista/Comerciante\n4- Viajero/artista\n------> '))
        preg5= int(input('\nA que casa no quieres pertenecer?:\n\n1- Gryffindor\n2- Slytherin\n3- Hufflepuff\n4- Ravenclaw\n------> '))
    except ValueError:
       print('Esa no es una opcion, estudiante')
       return

    opciones = [preg1,preg2,preg3,preg4,preg5]
    
    for x in opciones:
       if x not in range(1,5):
          print('Elige entre las opciones que te doy, mago..')
          return
    return opciones

def sombrero():
    import random
    casas= ('','Gryffindor', 'Slytherin' , 'Hufflepuff' , 'Ravenclaw')
    respuestas= preguntas()
    if type(respuestas) != list:
       return
    else:
        resultado= [casas[x] for x in respuestas]
        for opcion in casas[1::]:
            try:
                resultado.remove(opcion)
            except ValueError:
                continue

        resultado= [x for x in set(resultado)]

        if len(resultado) > 1:
            resultado= str(random.choice(resultado))
 
    return f'\nLa casa a la que irás es {resultado[0]}'

def main():
    temp= sombrero()
    print(temp)
    return

if __name__ == '__main__':
    main()

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------