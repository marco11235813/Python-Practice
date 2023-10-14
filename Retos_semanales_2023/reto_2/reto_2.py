"""2-
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")\n\n"""





#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
"""Marco Caro PYandDT"""

# creamos una funcion constructora del lenguaje leet (la construimos en base a un diccionario donde las llaves son las letras y los valores su correspondiente caracter leet)

# def leet()->dict:
#   dicc= {}
#   while True:

#     letra= input('Ingresa la letra: ').lower()
#     if letra == 'exit':
#       break
#     p= input('Ingresa el caracter: ')
#     dicc.setdefault(letra,p)

#   return dicc


# leet= leet() ## llamamos la funcion para construir el diccionario y tenerlo a disposicion para utilizarlo

# # creamos el convertidor
# def convertidor_leet()->str:
#   promp= input('Ingresa una frase o palabra: ')
#   l= leet
#   new_frase= []
#   for letra in promp:
#     if letra == ' ':
#         new_frase.append(letra)
#         continue
#     else:
#       letra= l[letra]
#       new_frase.append(letra)
  
#   return ''.join(new_frase)




# otra manera
# en este caso la funcion leet crea un fichero con las letras y su correspondiente caracter leet, por lo que se correria la funcion una sola vez
def leet()->dict:

  try:
    f= open('Retos_semanales_2023/reto_2/dicc_leet.txt', 'r')
    print('Ya existe un diccionario')
    return
  except FileNotFoundError:
    with open('dicc_leet.txt', 'w') as f:
        while True:
            letra= input('Ingrese la letra (ingrese exit para terminar): ').lower()
            if letra == 'exit':
               break
            caracter= input('Ingrese el caracter: ')
            f.write(f'{letra}:{caracter}\n')
  return

def convertidor_leet()->str:
    
    new_frase= []
    promp= input('Ingresa una frase o palabra: ').lower()
    
    with open('Retos_semanales_2023/reto_2/dicc_leet.txt', 'r') as f:
        dicc= {}
        temp= f.read().split('\n')
        temp.pop(-1)
        temp= [x.split(':') for x in temp]
    for key,value in temp:
        dicc.setdefault(key, value)

    new_frase= []
    for letra in promp:
        if letra == ' ':
            new_frase.append(letra)
            continue
        else:
            letra= dicc[letra]
            new_frase.append(letra)

  
    return ''.join(new_frase)

def main():
  # leet()
  print(convertidor_leet())
  return

if __name__ == '__main__':
  main()




# ACLARACIONES

# --Utilizamos el segundo valor leet para la letra 'i' ya que el primer caracter tanto de la letra 'i' como de la letra 'l' era el mismo y para evitar errores de lectura y agilizar la misma se recurrio a esto.
# --La funcion leet() en su segunda version, crea un archivo tipo .txt, por lo que con llamar una vez a la funcion ya deja el archivo con las equivalencias de letras/caracteres creado y listo para su uso posterior
#  es decir, no se utiliza en el futuro (salvo casos excepcionales como el que se borre el archivo que contiene las equivalencias)

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------