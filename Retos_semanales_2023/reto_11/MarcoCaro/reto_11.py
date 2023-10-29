""" * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis"""

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

"""Marco Caro PYandDT\n"""
def llamada_api(url= "https://rickandmortyapi.com/api/character")->str|list|tuple|dict|None:

   import requests
   import json

   ## las requests estan paginas por defecto desde la pagina
   response= requests.get(url) ##pedimos la consulta desde la pagina
   count_paginas= response.json()['info']['pages'] ##obtenemos el numero de paginas del atributo/campo 'characters' que nos interesa

   while True:
      for pagina in range(count_paginas):
         url=  f"https://rickandmortyapi.com/api/character/?page= {pagina}" ## recorremos todas las paginas con personajes(ya que cada pagina tiene como maximo 20 personajes)
         response= requests.get(url)  ## volvemos a pedir la consulta de la pagina (va cambiando la pagina donde se consulta a causa de nuestro bucle)
         for personaje in response.json()['results']: ## la key results,los datos de los personajes.
            print(personaje['name']) ## imprimimos el nombre del personaje
         if pagina == count_paginas:
            break
      break

   return

def main():
   a= llamada_api()
   return
if __name__ == '__main__':
   main()
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------