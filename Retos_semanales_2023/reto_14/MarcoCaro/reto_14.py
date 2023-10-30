"""* Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
 *   ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres"""



#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

"""Marco Caro PYandDT\n"""
def formateo_palabra(string)->str():
   import random
   numero_letras= len(string)

   porcentaje_ayuda= int(len(string)/2) + 1
   indices_random= random.sample(range(len(string)), k= porcentaje_ayuda)
   resultado= list()
   for idx, caracter in enumerate(string):
      if idx in indices_random:
         resultado.append(caracter)
      else:
         resultado.append('_')

   return resultado


def comprobacion_palabra(promp= 'Ingresa una palabra: ')->str|bool:

      capsula= None
      abecd= ["a",'b','c','d','e','f'                            
         ,'g','h','i','j','k','l',            
         'm','n','ñ','o','p','q','r'
         ,'s','t','u','v','w','x','y','z']

      palabra= input(promp).strip().lower()
      for caracter in palabra:
         if caracter not in abecd:
            print('Caracter invalido (solo se admiten letras para una palabra)')
            palabra= False
            break
         else:
            capsula= formateo_palabra(palabra)

      return capsula,palabra,abecd



def ahorcado()->str:
    ## juego del ahorcado

    ##preparamos e inicializamos algunas variables basicas
    intentos= 3                                                 #------------>  variable que utilizamos condicion para terminar el juego
    valores_probados= []                                        # ------------> valores/letras que ya se utilizaron o ingresaron en el input
    repeticiones= 0                                             #------------>  variable que utilizamos para terminar el juego
    
    capsula,palabra,abecd= comprobacion_palabra()

    if type(palabra) == bool:
        return
    else:
        print('Bienvenido al Juego del Ahorcado\n')
        print(f'{capsula}\n')
        while intentos != 0 and repeticiones != 3 and '_' in capsula: ## condiciones 
            ingreso= input('Ingresa una letra o intenta adivinar la palabra completa: ').lower().strip('')
            if len(ingreso) == 1:
                if ingreso not in abecd:
                    print('Caracter invalido')
                elif ingreso in valores_probados:
                    repeticiones +=1
                    if repeticiones == 3:
                        break
                    print('\nYa utilizaste esta letra!')
                    continue
                elif ingreso not in list(palabra):
                    intentos -=1
                    if intentos == 0:
                        break
                    print('\nFallaste! intentalo nuevamente')
                    continue
                else:
                    valores_probados.append(ingreso)                 ## agregamos a una lista, el valor ingresado como input, para comparar con futuros inputs y evitar su repeticion
                    for idx, x in enumerate(palabra):   
                        if x== ingreso:
                            capsula[idx] = ingreso
                    # print(f"{''.join(capsula)}\n")
                    print(f'{capsula}\n')

            elif len(ingreso) == len(capsula):
                if ingreso == palabra:
                    print(f'\nGanaste felicitaciones! La palabra es {ingreso}\n')
                    return '-'*160
                elif ingreso != palabra:
                    intentos -=1
                    if intentos == 0:
                        break
                    print('\nFallaste! intentalo nuevamente')
                    continue
            else:
                print('Solo puedes intentar adivinar de a una letra, o intentar adivinar la palabra completa!!')
                continue

    if repeticiones == 3 or intentos == 0: ## resultados
        print('\nFin del juego\n')
    else:
        print(f'Ganaste felicitaciones! La palabra es {"".join(capsula)}\n')

    return '-'*160



def main():

   a= ahorcado()
   print(a)

   return

if __name__ == '__main__':
   main()