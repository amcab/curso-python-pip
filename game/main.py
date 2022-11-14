import random 

def escoje_opciones(): 
    opciones = ('piedra', 'papel', 'tijera')
    opcion_user = input('Escoje tu opcion entre piedra, papel o tijera: ')

    if not opcion_user in opciones:
        print('esa opcion no es valida')

    opcion_computador = random.choice(opciones)

    print('Tu opcion es: ', opcion_user)
    print('La opcion del computador es: ', opcion_computador)
    return opcion_user, opcion_computador

def reglas_del_juego(opcion_user, opcion_computador, user_gana, computador_gana):
    if opcion_user == opcion_computador:
        print('Empate!!!')
    elif opcion_user == 'piedra':
        if opcion_computador == 'tijera':
            print('Piedra le gana a tijera')
            print('Jugador gana')
            user_gana +=1
        else: 
            print('Papel gana a piedra')
            print('Computador gana')
            computador_gana +=1
    
    elif opcion_user == 'tijera':
        if opcion_computador == 'papel':
            print('tijera le gana a papel')
            print('Jugador gana')
            user_gana +=1
        else: 
            print('Piedra gana a tijera')
            print('Computador gana')
            computador_gana +=1
    
    elif opcion_user == 'papel':
        if opcion_computador == 'piedra':
            print('Papel le gana a piedra')
            print('Jugador gana')
            user_gana +=1
        else: 
            print('Tijera gana a papel')
            print('Computador gana')
            computador_gana +=1

    return computador_gana, user_gana

def run_game():
  computador_ganadas = 0
  user_ganadas = 0  
  rounds = 1
  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('Computador gana', computador_ganadas)
    print('Jugador gana', user_ganadas)
    rounds += 1

    opcion_user, opcion_computador = escoje_opciones()
    user_ganadas, computador_ganadas = reglas_del_juego(opcion_user, opcion_computador, user_ganadas, computador_ganadas)

    if computador_ganadas == 2:
      print('El ganador es la computadora')
      break

    if user_ganadas == 2:
      print('El ganador es el jugador')
      break

run_game()

