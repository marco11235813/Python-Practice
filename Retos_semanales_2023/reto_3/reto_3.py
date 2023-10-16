 """* 3-Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos. """

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
"""Marco Caro PYandDT"""


def game()->str:
    
    game= input('Ingrese puntos del game: ').title().strip('[]').split(',')
    game= [x.strip() for x in game]

    for x in game:
        if x not in ['P1', 'P2']:
            print('Error en la entrada de datos')
            return
        else:
            continue

    valores= ('love','15','30','40', 'Ventaja ')
    P1= 0
    P2= 0
    print('P1---P2\n')


    for punto in game:
        if P1 >= 4 and P2 >= 4:
            pass
        elif P1 == 0 and P2 == 0:
            pass
        else:
            print(valores[P1]+' - '+valores[P2])


        if P1 == 4 and P2 == 4:
            print('Deuce')
        elif punto == 'P1':
            P1 += 1
            if P1 >= 4 and (P1 - P2) == 2:
                print(f'Ha ganado el {punto}')
                return 
            elif P1 == 5 and (P1 - P2) == 1:
                print(valores[P1] + punto)
                continue
        elif punto == 'P2':
            P2 += 1
            if P2 >= 4 and (P2 - P1) == 2:
                print(valores[P2] + punto)
                return 
            elif P2 == 5 and (P2 - P1) == 1:
                print('Ventaja P2')
                continue


    return

# otra manera

def control_entrada_datos()->list|tuple:

    lista= input('Ingrese puntos del game: ').title().strip('[]').split(',')
    lista= [x.strip() for x in lista]

    for x in lista:
        if x not in ['P1', 'P2']:
            print('Error en la entrada de datos')
            return
        else:
            continue

    return lista

def game()->str:

    try:   
        game= control_entrada_datos()

        valores= ('love','15','30','40', 'Ventaja ')
        P1= 0
        P2= 0
        print('P1---P2\n')


        for punto in game:
            if P1 >= 4 and P2 >= 4:
                pass
            elif P1 == 0 and P2 == 0:
                pass
            else:
                print(valores[P1]+' - '+valores[P2])

            if P1 == 4 and P2 == 4:
                print('Deuce')
            elif punto == 'P1':
                P1 += 1
                if P1 >= 4 and (P1 - P2) == 2:
                    print(f'Ha ganado el {punto}')
                    return 
                elif P1 == 5 and (P1 - P2) == 1:
                    print(valores[P1] + punto)
                    continue
            elif punto == 'P2':
                P2 += 1
                if P2 >= 4 and (P2 - P1) == 2:
                    print(valores[P2] + punto)
                    return 
                elif P2 == 5 and (P2 - P1) == 1:
                    print('Ventaja P2')
                    continue
    except TypeError:
        pass

    return


def main():
    print(game())
    return

if __name__ == '__main__':
    main()
    
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------