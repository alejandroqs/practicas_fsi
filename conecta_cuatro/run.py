import games
import heuristica
#game = games.TicTacToe(h=3,v=3,k=3)
game = games.ConnectFour()

state = game.initial
dif = 0
while(dif < 1 or dif > 3):
    dif_str = raw_input("Elija dificultad:\n1 -> Facil\n2 -> Intermedio\n3 -> Avanzado\n")
    dif = int(str(dif_str).strip())
    d = dif + 2
    if (dif < 1 or dif > 3):
        print("ERROR: Introduzca una dificultad valida\n")
        
p = 0
player=''
while(p < 1 or p > 2):
    p_str = raw_input("Elija Jugador inicial:\n1 -> Maquina\n2 -> Jugador\n")
    p = int(str(p_str).strip())
    print p
    if p==1:
        player='X'
    elif p==2:
        player='O'
    else: 
        print("ERROR: Introduzca un valor valido\n")
    
state.to_move=player
# player = 'X'
while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]
        state = game.make_move((x, y), state)
        player = 'X'
    else:
        print "Thinking..."
        #move = games.minimax_decision(state, game)
        #move = games.alphabeta_full_search(state, game)
        move = games.alphabeta_search(state, game, d, eval_fn=heuristica.m)

        state = game.make_move(move, state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break