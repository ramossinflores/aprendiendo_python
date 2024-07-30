cont = 1
while cont:
    print('¡Juguemos! Piedra ✊, papel ✋ o tijera 🖖')
    print('¿Quién es el primero en jugar? ☝️')
    print('Escribe tu nombre: ', end=' ')
    player1 = input()
    print('¿Quién va en segundo? ✌️')
    print('¿Cómo te llamas?: ', end=' ')
    player2 = input()
    print('¡A jugar!')
    print('Deben escribir piedra ✊ o papel ✋ o tijera 🖖 según escojas')
    print(player1.capitalize(), end=' ')
    player1_chosen = input(" escoge: ")
    print(player2.capitalize(), end=' ')
    player2_chosen = input(' tu turno: ')
    allowed_values = ['piedra','papel','tijera']
    if player1_chosen in allowed_values and player2_chosen in allowed_values:
        if player1_chosen == player2_chosen:
            print('¡Empate! 🤝')
        if (player1_chosen == 'tijera' and player2_chosen == 'papel') or (player2_chosen == 'tijera' and player1_chosen == 'papel'):
            print('La tijera corta el papel ✂️\n')
        if (player1_chosen == 'piedra' and player2_chosen == 'tijera') or (player2_chosen == 'piedra' and player1_chosen == 'tijera'):
            print('La piedra 🌑 aplasta la tijera ✂️\n')
        if (player1_chosen == 'papel' and player2_chosen == 'piedra') or (player2_chosen == 'papel' and player1_chosen == 'piedra'):
            print('El papel envuelve la piedra 📰')
    else:
        print('Se ha introducido una elección no válida. Recuerda esribir: Piedra ✊, papel ✋ o tijera 🖖')
    cont = input("Deseas jugar otra vez? \n Teclea s para continuar o cualquier tecla para salir: ")
    if cont != "s":
        break


