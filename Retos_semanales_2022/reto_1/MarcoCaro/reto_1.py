"""Reto #1: ¿ES UN ANAGRAMA?

/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */"""


#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

"""Marco Caro PYandDT\n"""

def anagrama(frase: str|None, palabra: str|None) -> bool|None:

   frase= frase.lower()
   palabra= palabra.lower()

   abc= ['a','b','c','d','e','f','g','h',
         'i','j','k','l','m','n','ñ','o','p',
         'q','r','s','t','u','v','w','x','y','z']

   for letra1, letra2 in zip(frase,palabra):
      if letra1 in abc and letra2 in abc:
         continue
      else:
         return 'Caracter invalido'
   
   return sorted(frase) == sorted(palabra)


def main():

   a= anagrama('amor', 'mora')
   print(a)
   print('-'*80)


if __name__ == '__main__':
   main()
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------