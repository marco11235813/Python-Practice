""" * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]"""



# https://www.google.com/search?q=parametros+de+una+url+ejemplos&sca_esv=575503381&rlz=1C1ALOY_esAR976AR976&sxsrf=AM9HkKlFW7GIYuQL372Dci_kcUSwIlZ8rw%3A1697929774913&ei=Llo0ZfOmN6uj1sQProO4mA0&ved=0ahUKEwjz9diooYiCAxWrkZUCHa4BDtMQ4dUDCBA&uact=5&oq=parametros+de+una+url+ejemplos&gs_lp=Egxnd3Mtd2l6LXNlcnAiHnBhcmFtZXRyb3MgZGUgdW5hIHVybCBlamVtcGxvczIIECEYFhgeGB1IyhBQtwVY2g1wAXgBkAEAmAHLAaABzQuqAQUwLjguMbgBA8gBAPgBAcICChAAGEcY1gQYsAPCAgYQABgWGB7CAggQABgWGB4YCsICBRAhGKAB4gMEGAAgQYgGAZAGCA&sclient=gws-wiz-serp
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

"""Marco Caro PYandDT\n"""
def parametros(url):

   # url= 'https://www.google.com/search?q=parametros+de+una+url+ejemplos&sca_esv=575503381&rlz=1C1ALOY_esAR976AR976&sxsrf=AM9HkKlFW7GIYuQL372Dci_kcUSwIlZ8rw%3A1697929774913&ei=Llo0ZfOmN6uj1sQProO4mA0&ved=0ahUKEwjz9diooYiCAxWrkZUCHa4BDtMQ4dUDCBA&uact=5&oq=parametros+de+una+url+ejemplos&gs_lp=Egxnd3Mtd2l6LXNlcnAiHnBhcmFtZXRyb3MgZGUgdW5hIHVybCBlamVtcGxvczIIECEYFhgeGB1IyhBQtwVY2g1wAXgBkAEAmAHLAaABzQuqAQUwLjguMbgBA8gBAPgBAcICChAAGEcY1gQYsAPCAgYQABgWGB7CAggQABgWGB4YCsICBRAhGKAB4gMEGAAgQYgGAZAGCA&sclient=gws-wiz-serp'
   url= url.split('=')
   parametros= list()
   for idx,x in enumerate(url):
      if idx == 0:
         continue
      else:
         x= x.split('&')
         parametros.append(x[0])
   print('-'*100)
   return parametros

def main():
   url= input('Introduce una url: ')
   a= parametros(url)
   print(a)
   return

if __name__ == '__main__':
   main()
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------