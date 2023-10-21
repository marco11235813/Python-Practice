""" 10- * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos."""



# Un heterograma es una palabra o frase que no contiene ninguna letra repetida
# Un isograma es una palabra o frase en la que cada letra aparece el mismo número de veces.3​
# Un pangrama es una frase en la que aparecen todas las letras del abecedario. 
# Si cada letra aparece sólo una vez, formando por tanto un heterograma, se le llama pangrama perfecto.
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

"""Marco Caro PYandDT\n"""
def abecedario()->list:  ## creamos una funcion abecedario que nos va a brindar todas las letras del abecedario para utilizar como comparacion

    lista= ["a",'b','c','d','e','f'                           
    ,'g','h','i','j','k','l',            
    'm','n','ñ','o','p','q','r'
    ,'s','t','u','v','w','x','y','z']

    return lista

def heterograma(palabra):
    abecd= abecedario() ## llamamos a la funcion abecedario() para asignar la lista con los valores dentro de la variable abecd
    conclusion= 'es un heterograma'  ## inicializamos la variable conclusion como que es un heterograma

    for letra in palabra: ## iteramos sobre la palabra ingresada
        if letra not in abecd: ## si el caracter/letra no es un valor de abecd, continua el bucle
            continue
        else: ## si el caracter letra si es un valor dentro de abecd
            temp=palabra.count(letra)## declaro esta variable con el numero de veces que una letra aprece en la frase/palabra ingresada
            if temp > 1:  ## si el valor de temp es mayor a 1
                conclusion= 'no es un heterograma' ## cambiamos el valor de conclusion a 'no es un heterograma'
                break
            else: ## si el valor de temp si es <= 1
                continue ## continuamos el bucle
    return conclusion

def isograma(palabra):

    abecd= abecedario()
    conclusion= ', es un isograma'
    temp= None ## inicializamos una variable con valor None, vamos a asignar un valor diferente en el futuro para comparacion
    for letra in palabra:
        if letra not in abecd:
            continue
        elif temp == None: ## si temp sigue siendo None, significa que es la primera iteracion del bucle
            temp= palabra.count(letra)## por lo que asignamos el valor de veces que se repite la letra dentro de la frase/palabra
            continue ## continuamos el bucle
        else:
            if palabra.count(letra) != temp: ## comparamos los valores ocn el valor que existe en temp, si alguno de los valores(las repeticiones de cada letra dentro de la frase/palabra), es diferente a temp...
                conclusion= ', no es un isograma' ## entoncecs cambiamos la conclusion a no es un isograma'
            else: ## si los valores son iguales, continuamos evaluando el siguiente valor
                continue

    return conclusion

def pangrama(palabra):

    abced= abecedario()
    
    conclusion= ' y es un pangrama'
    for letra in abced:## iteramos sobre los valores del abecedario de la variable abecd
        if letra in palabra: ## si la letra esta en la frase/palabra continuamos con la siguiente iteracion
            continue
        else:
            conclusion= ' y no es un pangrama' ## si no esta en la frase/palabra, cambiamos el valor de conclusion a 'no es un pangrama'
            break
    return conclusion

def main():

    a= input('Ingrese una palabra o frase: ').lower()
    if len(a) == 0: ## si la longitud de la variable 'a' es 0, quiere decir que no se ingreso ningun caracter
        print('Debes ingresar una palabra o frase')
        return
    else:
        print(f'La palabra/frase: "{a}", {heterograma(a)}{isograma(a)}{pangrama(a)}')
    return '-' * 80


if __name__ == '__main__':
   main()
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------