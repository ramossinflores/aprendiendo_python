class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0
    
    def place_ship(self, star_row, star_col, direction, board):
        positions = [] # Lista para almacenar las posiciones que ocupará el barco en el tablero.
        if direction == "H": # Colocación Horizontal
            if star_col + self.size > len(board[0]): # Comprueba si el barco cabe horizontalmente desde la columna inicial.
                return False
            for i in range(self.size): # Itera sobre el tamaño del barco.
                if board[star_row][star_col+i] != " ": # Comprueba si cada celda está libre. Si alguna celda ya está ocupada, retorna False.
                    return False
                positions.append((star_row, star_col + i)) # Si la celda está libre, añade la posición a la lista positions.
        elif direction == "V": # Colocación Vertical
            if star_row + self.size > len(board): # Comprueba si el barco cabe verticalmente desde la fila inicial. Si la suma de la fila inicial y el tamaño del barco excede el número de filas del tablero, no cabe y retorna False.
                return False
            for i in range(self.size): #  Itera sobre el tamaño del barco.
                if board[star_row][star_col+i] != " ": # Comprueba si cada celda está libre. Si alguna celda ya está ocupada, retorna False.
                    return False 
                positions.append((star_row + i, star_col)) # Si la celda está libre, añade la posición a la lista positions.
        else: # Si la dirección no es 'H' ni 'V', retorna False.
            return False
        
        # Colocación del Barco en el Tablero
        for pos in positions: 
            board[pos[0]][pos[1]]  = self.name[0]  # Coloca la inicial del nombre del barco (self.name[0]) en cada celda correspondiente del tablero
        self.positions = positions # Actualiza el atributo positions del barco con las posiciones calculadas.
        return True # Retorna True para indicar que el barco ha sido colocado exitosamente.
    
    def hit(self): # Aumenta los impactos y retorna si el barco ha sido hundido (impactos igual a su tamaño).
        self.hits +=1
        return self.hits == self.size 

# Herencia: Destroyer, Submarine, y Battleship heredan de Ship y definen su nombre y tamaño.
class Destroyer(Ship):
    def __init__(self):
        super().__init__("Destructor", 2)

class Submarine(Ship):
    def __init__(self):
        super().__init__("Submarino", 3)

class Battelship(Ship):
    def __init__(self):
        super().__init__("Acorazado", 4)

class Player:
    def __init__(self, name):
        self.name = name
        self.board = [[" " for _ in range(10)] for _ in range(10)] # Esto crea una lista de listas (una matriz de 10x10) donde cada celda contiene un espacio en blanco (' ').
        self.ships = [] #  La lista de barcos 
        self.hits = [[" " for _ in range(10)] for _ in range(10)] # El tablero de impactos
    
    def place_ships(self): # Permite al jugador colocar sus barcos.
        ships = [Destroyer(), Submarine(), Battelship()]
        for ship in ships:
            while True:
                print(f"{self.name}, coloca tu {ship.name} de tamaño {ship.size}.")
                start_row = int(input("Fila inicial: "))
                start_col = int(input("Columna inicial: "))
                direction = input("Dirección (H para horizontal, V para vertical): ").upper()
                if ship.place_ship(start_row, start_col, direction, self.board):
                    self.ships.append(ship)
                    self.print_board(self.board)
                    break
                else:
                    print("Posición no válida. Inténtalo de nuevo.")

    def print_board(self, board): # se encarga de imprimir el tablero en la consola
        for row in board:  #  Itera sobre cada fila en el tablero (board). Cada row es una lista que representa una fila del tablero.
            print(" ".join(row)) # " ".join(row) convierte la lista row en una cadena de caracteres, uniendo los elementos de la lista con un espacio entre ellos.
        print() # línea en blanco al final de la iteración 

    def attack(self, opponent):
        while True:
            print(f"{self.name}, elige una posición para atacar.")
            row = int(input("Fila: "))
            col = int(input("Columna: "))
            if 0 <= row < 10 and 0 <= col < 10: # Mientras el valor de la comlumna y de la fila estén entre 0 y 9
                if opponent.board[row][col] == ' ': # Si la posición elegida es un espacio vacío, quiere decir que hay agua
                    print("Agua!") # Informa al jugador que el ataque fue al agua.
                    self.hits[row][col] = 'A' #  Marca la celda correspondiente en el tablero de impactos del jugador con 'A' (agua).
                    opponent.board[row][col] = 'A' #  Marca la celda correspondiente en el tablero del oponente con 'A' (agua).
                    break
                elif opponent.board[row][col] != 'A':
                    print("Impacto!") # Informa al jugador que el ataque impactó un barco.
                    self.hits[row][col] = 'T' # Marca la celda correspondiente en el tablero de impactos del jugador con 'T' (impacto).
                    for ship in opponent.ships: # Itera sobre los barcos del oponente
                        if (row, col) in ship.positions: #  Verifica si la posición atacada es parte de uno de los barcos.
                            if ship.hit():
                                print(f"¡Hundido! Has hundido el {ship.name}.") #  Informa al jugador que ha hundido un barco.
                            break
                    opponent.board[row][col] = 'T' #  Marca la celda correspondiente en el tablero del oponente con 'T' (impacto).
                    break
                else:
                    print("Ya has atacado esta posición. Intenta de nuevo.") # Si la celda atacada ya contiene 'A' (agua), significa que ya fue atacada.
            else:
                print("Posición no válida. Intenta de nuevo.") # Si los valores de fila o columna no están dentro del rango de 0 a 9.

    def all_ships_sunk(self): # Verifica si todos los barcos han sido hundidos.
        #Para cada barco, verifica si el número de impactos (ship.hits) es igual al tamaño del barco (ship.size).
        return all(ship.hits == ship.size for ship in self.ships) # all(...) retorna True si todos los barcos cumplen la condición (ship.hits == ship.size).

class BattleshipGame:
    def __init__(self):
        self.player1 = Player("Jugador 1")
        self.player2 = Player("Jugador 2")

    def play(self):
        print("Bienvenido al juego de Batalla Naval ⛴️")
        print("Jugador 1 coloca sus barcos.")
        self.player1.place_ships()
        print("Jugador 2 coloca sus barcos.")
        self.player2.place_ships()

        current_player = self.player1
        opponent = self.player2

        while True:
            current_player.attack(opponent)
            if opponent.all_ships_sunk():
                print(f"¡{current_player.name} ha ganado el juego!")
                break
            current_player, opponent = opponent, current_player

# Crear una instancia del juego y jugar
game = BattleshipGame()
game.play()