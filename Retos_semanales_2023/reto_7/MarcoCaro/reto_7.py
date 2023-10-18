""" * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades."""


#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

"""Marco Caro PYandDT\n"""

def combinaciones_ganadoras()->list:

    valor= ["🗿","📄","✂️","🦎","🖖"]
    combinaciones= []

    for x in valor:
        for y in valor:
            if x == y:
                continue
            elif x != y and (y,x) not in combinaciones:
                combinaciones.append((x,y))
    ganadoras= [1,0,0,1,1,0,0,0,1,0]
    comb_ganadoras= [(x,y) for x,y in zip(ganadoras,combinaciones)]

    return comb_ganadoras

def permutaciones()->list:

    valor= ["🗿","📄","✂️","🦎","🖖"]
    permutaciones= []

    for x in valor:
        for y in valor:
            permutaciones.append((x,y))

    return permutaciones


def manos()->list:
    import random
    temp= permutaciones()
    temp= random.choices(temp, k= 5)
    primero= [x[0] for x in temp]
    segundo= [x[1] for x in temp]
    dicc = {}
    dicc.setdefault('player1', primero)
    dicc.setdefault('player2', segundo)

    return dicc, temp

def juego()->str:
    
    registro, rondas= manos()
    print(rondas)
    temp= combinaciones_ganadoras()
    print(temp)
    jugadores= ['Player1', 'Player2']
    for mano in rondas:
        if mano[0] == mano[1]:
            print(f'Mano: {mano}----> Tie')
        else:
            for tup in temp:
                if mano == tup[1]:
                    print(f'Mano: {mano}---->Ganador {jugadores[tup[0]]}')
                elif mano == tup[1][::-1]:
                    if tup[0] == 1:
                        print(f'Mano: {mano}---->Ganador {jugadores[0]}')
                    else:
                        print(f'Mano: {mano}---->Ganador {jugadores[1]}')
                else:
                    continue

    return '-' * 80


def main():
    temp= juego()
    print(temp)
    return

if __name__ == '__main__':
    main()

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

