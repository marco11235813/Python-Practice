""" * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"""

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

"""Marco Caro PYandDT\n"""

def fibonacci(numero)->str:
    """Esta funcion toma un numero mayor o igual a 1 y examina si es parte de la serie de numeros fibonacci.
    en caso de que los sea devuelve una cadena afirmativa, y en caso contrario devuelve una cadena negativa"""
    valores= []
    contador= 0
    num1= 0
    num2= 1
    while contador <= 10 :
        contador += 1

        if len(valores) == 0:
            valores.append(num1)
            valores.append(num2)
        else:
            resultado= num1 + num2
            valores.append(resultado)
            num1 = num2
            num2 = resultado
            continue

    if numero in valores:
        conclusion = 'es fibonacci'
    else:
        conclusion = 'no es fibonacci'
    return conclusion

def primo_o_no(numero)->str:
    """Esta funcion controla que el valor pasado sea o no sea un numero primo
    en caso de cerlo devuelve una cadena diciendo que es primo, en caso contrario
    devuelve una cadena diciendo que no es primo"""
    conclusion= 'es primo'
    for x in range (2,numero):
        if numero%x == 0:
            conclusion = 'no es primo'
            break

    return conclusion

def es_par(numero)->str:
    """Esta funcion analiza un numero para saber si es par o no, en caso de ser par devuelve una cadena diciendo
    que lo es, en caso contrario devuelve una cadena diciendo que no es par"""
    if numero%2 == 0:
        conclusion= 'es par'
    else:
        conclusion= 'no es par'
    return conclusion

def comprobar():
    """esta funcion pide al usuario que ingrese un numero (mayor a 1) para realizarle comprobaciones:
    - si es o no par
    - si pertenece o no a la serie de numeros fibonacci
    - si es primo o no lo es
    
    en caso de pasarle un valor no numerico, devuelve un mensaje de valor invalido y termina la funcion"""
    
    try:
        num= int(input('Ingrese un numero: '))
    except ValueError:
        return 'Valor invalido'
    if num < 1:
        return 'El numero debe ser mayo o igual a 1'
    else:
        fibo= fibonacci(num)
        prim= primo_o_no(num)
        par_o_no= es_par(num)
    
    return f"{num} {prim}, {fibo} y {par_o_no}"

def main():
    temp= comprobar()
    print(temp)
    return

if __name__ == '__main__':
    main()

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------