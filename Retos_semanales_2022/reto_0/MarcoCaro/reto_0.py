"""
Reto #0: EL FAMOSO "FIZZ BUZZ”

/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"."""






#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

"""Marco Caro PYandDT\n"""

def fizz_buzz(rango: list|tuple|set) -> str|int:

   """ esta funcion recibe un rango de numeros y los imprime por consola.
   sustituyendo los siguientes:
   * - Múltiplos de 3 por la palabra "fizz".
   * - Múltiplos de 5 por la palabra "buzz".
   * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
   
   """

   for num in rango:
      if num % 3 == 0 and num % 5 == 0:
         print('fizzbuzz')
      elif num % 3 == 0:
         print('fizz')
      elif num % 5 == 0:
         print('buzz')
      else:
         print(num)

   return '-'*80


def main():

   a= fizz_buzz(list(range(1,101)))
   print(a)


if __name__ == '__main__':
   main()
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------