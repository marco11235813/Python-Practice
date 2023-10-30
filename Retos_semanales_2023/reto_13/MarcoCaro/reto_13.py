"""* Crea una función que sea capaz de detectar si existe un viernes 13
 * en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso."""


#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

"""Marco Caro PYandDT\n"""


def viernes_13(año,mes)->str:
    import calendar as c
    meses= ['Enero', 'Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    obj= c.Calendar()
    lista= list()
    for dia in obj.itermonthdays2(año, mes):
        if dia[0] == 13 and dia[1] == 4:
            print(f'El mes {meses[mes-1]} del año {año} tiene un Viernes 13')
            return
        elif dia[0] <=13:
            continue
        else:
            break
    print(f'El mes {meses[mes-1]} del año {año} no tiene un viernes 13')
    return





# etiqueta_dias= ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
# etiqueta_mes= ['Enero', 'Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
# def generar_fecha_dia(Año= 'Ingrese el año: ' ,Mes= 'Ingrese el mes (en numero ej: 1 para enero....): ' ):
   
#    mes= range(1,13)

#    try:
#       año= int(input(Año))
#       mes= int(input(Mes))
#    except ValueError:
#       print('Valor invalido')
#     if mes in (1, 3, 5, 7, 8, 10, 12):
#         dia = range(1,31)
#     elif mes in (4,6,9,11):
#         dia = range(1,30)
#     else:
#         if (anio%4) ==0:
#             dia = range(1,29)
#         else:
#             dia = range(1,28)
#    return 


def main():

   dato= input('Ingresa el año y el mes a buscar separado por coma: ').split(',')
   a= viernes_13(dato[0],dato[1])
   print(a)

   return

if __name__ == '__main__':
   main()
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------