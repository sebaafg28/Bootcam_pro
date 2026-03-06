


#import random 
#lista = [['perro'], ['mixto'], ['pausa'],['medio'],['juega'],]
#varia = random.choices(lista)

palabra_a_encontrar = 'pausa'
intentos = 5
def obtener_fila_verificada( palabra_ingresada):
    cantidad_letras_de_palabra_a_encontrar = 5

   
    letras_verificadas = []

    for posicion in range(cantidad_letras_de_palabra_a_encontrar): #5

        
        las_letras_son_iguales = palabra_a_encontrar[posicion] == palabra_ingresada[posicion]


        
        la_letra_existe_en_la_palabra = palabra_ingresada[posicion] in palabra_a_encontrar

        if las_letras_son_iguales:
            
            letras_verificadas.append('['+palabra_ingresada[posicion]+']')

        elif la_letra_existe_en_la_palabra:
            letras_verificadas.append('('+palabra_ingresada[posicion]+')')

        else:
            letras_verificadas.append(palabra_ingresada[posicion])

        
    return letras_verificadas

while intentos > 0:
    prueba = input('ingrese su palabra: ')
    resultado = obtener_fila_verificada(prueba)
    intentos = intentos - 1
    print(resultado)
    if prueba == palabra_a_encontrar:
        print('felicidades, ganaste el juego')
        break
    else:
        print(f'te quedan {intentos} intentos')
        if intentos == 0:
            print('perdiste')
    