#  Crea un programa que calcule quien gana más partidas al piedra,
#  papel, tijera, lagarto, spock.
#  - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  - La función recibe un listado que contiene pares, representando cada jugada.
#  - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#    "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
#  - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
#  - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

resultados = ["Player 1", "Player 2", "Tie"]
entradas = {
    "piedra": "🗿",
    "papel": "📄",
    "tijeras": "✂️",
    "lagarto": "🦎",
    "spock": "🖖"
}


def game_result(entrada1: str, entrada2: str) -> str:

    if entrada1 == entrada2:
        return "Tie"
    elif entrada1 == entradas["tijeras"] and entrada2 == entradas["papel"]:
        return "Player 1"
    elif entrada2 == entradas["tijeras"] and entrada1 == entradas["papel"]:
        return "Player 2"
    elif entrada1 == entradas["papel"] and entrada2 == entradas["piedra"]:
        return "Player 1"
    elif entrada2 == entradas["papel"] and entrada1 == entradas["piedra"]:
        return "Player 2"
    elif entrada1 == entradas["piedra"] and entrada2 == entradas["lagarto"]:
        return "Player 1"
    elif entrada2 == entradas["piedra"] and entrada1 == entradas["lagarto"]:
        return "Player 2"
    elif entrada1 == entradas["lagarto"] and entrada2 == entradas["spock"]:
        return "Player 1"
    elif entrada2 == entradas["lagarto"] and entrada1 == entradas["spock"]:
        return "Player 2"
    elif entrada1 == entradas["spock"] and entrada2 == entradas["tijeras"]:
        return "Player 1"
    elif entrada2 == entradas["spock"] and entrada1 == entradas["tijeras"]:
        return "Player 2"
    elif entrada1 == entradas["tijeras"] and entrada2 == entradas["lagarto"]:
        return "Player 1"
    elif entrada2 == entradas["tijeras"] and entrada1 == entradas["lagarto"]:
        return "Player 2"
    elif entrada1 == entradas["lagarto"] and entrada2 == entradas["papel"]:
        return "Player 1"
    elif entrada2 == entradas["lagarto"] and entrada1 == entradas["papel"]:
        return "Player 2"
    elif entrada1 == entradas["papel"] and entrada2 == entradas["spock"]:
        return "Player 1"
    elif entrada2 == entradas["papel"] and entrada1 == entradas["spock"]:
        return "Player 2"
    elif entrada1 == entradas["spock"] and entrada2 == entradas["piedra"]:
        return "Player 1"
    elif entrada2 == entradas["spock"] and entrada1 == entradas["piedra"]:
        return "Player 2"
    elif entrada1 == entradas["piedra"] and entrada2 == entradas["tijeras"]:
        return "Player 1"
    elif entrada2 == entradas["piedra"] and entrada1 == entradas["tijeras"]:
        return "Player 2"
    else:
        return "error"


def registro(jugadas: list) -> list:
    resultados = []
    valores_admitidos = ["🗿", "📄", "✂️", "🦎", "🖖"]
    for jugada in jugadas:
        if ((jugada[0] not in valores_admitidos) or (jugada[1] not in valores_admitidos)):
            return "Entrada incorrecta"
        resultados.append(game_result(jugada[0], jugada[1]))
    return resultados


def ganador(jugadas: list) -> str:
    resultados = registro(jugadas)
    if resultados == "Entrada incorrecta":
        return resultados

    victorias_1 = 0
    victorias_2 = 0

    for resultado in resultados:
        if resultado == "Player 1":
            victorias_1 += 1
        if resultado == "Player 2":
            victorias_2 += 1

    if victorias_1 > victorias_2:
        return "Player 1"
    elif victorias_2 > victorias_1:
        return "Player 2"
    else:
        return "Tie"


if __name__ == "__main__":
    combinaciones = [
        ("🗿", "🗿"),  # Piedra vs. Piedra
        ("🗿", "📄"),  # Piedra vs. Papel
        ("🗿", "✂️"),  # Piedra vs. Tijeras
        ("🗿", "🦎"),  # Piedra vs. Lagarto
        ("🗿", "🖖"),  # Piedra vs. Spock

        ("📄", "🗿"),  # Papel vs. Piedra
        ("📄", "📄"),  # Papel vs. Papel
        ("📄", "✂️"),  # Papel vs. Tijeras
        ("📄", "🦎"),  # Papel vs. Lagarto
        ("📄", "🖖"),  # Papel vs. Spock

        ("✂️", "🗿"),  # Tijeras vs. Piedra
        ("✂️", "📄"),  # Tijeras vs. Papel
        ("✂️", "✂️"),  # Tijeras vs. Tijeras
        ("✂️", "🦎"),  # Tijeras vs. Lagarto
        ("✂️", "🖖"),  # Tijeras vs. Spock

        ("🦎", "🗿"),  # Lagarto vs. Piedra
        ("🦎", "📄"),  # Lagarto vs. Papel
        ("🦎", "✂️"),  # Lagarto vs. Tijeras
        ("🦎", "🦎"),  # Lagarto vs. Lagarto
        ("🦎", "🖖"),  # Lagarto vs. Spock

        ("🖖", "🗿"),  # Spock vs. Piedra
        ("🖖", "📄"),  # Spock vs. Papel
        ("🖖", "✂️"),  # Spock vs. Tijeras
        ("🖖", "🦎"),  # Spock vs. Lagarto
        ("🖖", "🖖"),  # Spock vs. Spock
    ]
    print(ganador([("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")]))
