"""Reto #2: LA SUCESIÓN DE FIBONACCI

/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */"""






#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

"""Marco Caro PYandDT\n"""

def fibonacci() -> list|int:

   a= 0
   b= 1

   print(a)
   print(b)
   contador= 2
   while contador < 51:
      num= a + b
      a=b
      b=num
      print(num)
      contador += 1


   return '-'*80


def main():
   a= fibonacci()
   print(a)
   return

if __name__ == '__main__':
   main()
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------