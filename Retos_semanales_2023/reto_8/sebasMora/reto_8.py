# Crea un programa que simule el comportamiento del sombrero seleccionador del
# universo mágico de Harry Potter.
# - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
# - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
# - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
# - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
#   Por ejemplo, en Slytherin se premia la ambición y la astucia.

preguntas = {
    "¿Qué cualidad valoras más en un amigo?":
    ["Coraje", "Ambición", "Lealtad", "Inteligencia"],
    "¿Cuál de estas mascotas de Hogwarts preferirías tener?":
    ["León", "Serpiente", "Tejón", "Águila"],
    "¿En qué tipo de aventuras te gustaría embarcarte?":
    ["En busca de emociones y riesgos", "En busca de poder y control",
        "Ayudando a los demás en momentos dificiles", "Explorando el conocimiento y los misterios"],
    "¿Qué asignatura de Hogwarts te resulta más interesante?":
    ["Defensa", "Pociones", "Cuidado", "Adivinación"],
    "Si tuvieras que elegir una cualidad personal, ¿cuál sería la más importante para ti?":
    ["Valentía", "Astucia", "Amabilidad", "Sabiduría"]
}


def seleccionador():
    resultados = []
    for pregunta, respuestas in preguntas.items():
        continuar = True
        print("Pregunta: ", pregunta)
        while continuar == True:
            for index, respuesta in enumerate(respuestas):
                print(index, " - ", respuesta)
            seleccion = input(
                "Respuesta?: Por favor digitela en función de los números de las respuestas: ")
            try:
                seleccion = int(seleccion)
                if seleccion not in ([0, 1, 2, 3]):
                    print("El número debe estar entre 0 y 3")
                    continuar = True
                else:
                    continuar = False
                    resultados.append(seleccion)

            except ValueError:
                print("Solo se admiten números")
                continuar = True

    respuesta = logica(resultados)
    return respuesta


def logica(resultados):
    casas = {
        0: "Gryffindor",
        1: "Slytherin",
        2: "Hufflepuff",
        3: "Ravenclaw"
    }

    contador_0 = 0
    contador_1 = 0
    contador_2 = 0
    contador_3 = 0

    for resultado in resultados:
        if resultado == 0:
            contador_0 += 1
        elif resultado == 1:
            contador_1 += 1
        elif resultado == 2:
            contador_2 += 1
        elif resultado == 3:
            contador_3 += 1

    contadores = [contador_0, contador_1, contador_2, contador_3]
    casa = max(contadores)

    return casas[contadores.index(casa)]


if __name__ == "__main__":
    print("Debe ir a la casa:", seleccionador())
