"""9- * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del 
 *   lenguaje de programación seleccionado."""

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

"""Marco Caro PYandDT\n"""

def generador():

    import datetime as dt #utilizamos la libreria datetime

    mili= dt.datetime.now() # utilizamos el metodo now que nos devuelve el tiempo actual hasta con milisegundos
    temp= str(mili).replace('-', '').replace(':','').replace('.','').replace(' ', '') #formateamos como string
    temp= [int(x) for x in temp] #convertimos cada valor en int
    print(temp)
    lista= []
    for numero in temp: # realizamos el algoritmo
        contrario= temp[-1]
        if numero == 0:
            continue
        else:
            resultado= numero * contrario
            if resultado > 100: # si el numero generado es mayor a 100, no lo imprime y continua el bucle generador
                continue
            elif resultado in lista:
                resultado= abs(int(resultado *3- numero**2 *4))
                lista.append(resultado)
                print(resultado)
            else:
                lista.append(resultado)
                print(resultado)
                
    return '-' * 80


def main():
    a= generador()
    print(generador)
    return

if __name__ == '__main__':
   main()
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------