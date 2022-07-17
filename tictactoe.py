# ALUNA: Luiza de Araújo Nunes Gomes
# MATRÍCULA: 190112794

class TicTacToe:
    def __init__(self):
        self.initialize_tictactoe()

    def initialize_tictactoe(self):
        self.current_board = [['_','_','_'],['_','_','_'],['_','_','_']]
        self.player_turn = 'X'
    
    def is_empty(self, x, y):       #checa se o local está vazio, ou seja, tem atualmente o caractere '_'
        if x not in [0, 1, 2] and y not in [0, 1, 2] or self.current_board[x][y] != '_':
            return False
        else:
            return True
        
    def print_board(self):      # imprime o tabuleiro
        for x in [0, 1, 2]:
            for y in [0, 1, 2]:
                if y < 2:
                    print(f'{self.current_board[x][y]}|', end ='')
                else:
                    print(f'{self.current_board[x][y]}')
        
    def win_or_tie(self):
        # Casos com vencedores
        for x in [0, 1, 2]:         # checa se nas verticais ou horizonatis tem casos vencedores
            if (self.current_board[0][x] == self.current_board[1][x] and self.current_board[1][x] == self.current_board[2][x] and self.current_board[2][x] != '_'):
                return self.current_board[2][x]
            if (self.current_board[x][0] == self.current_board[x][1] and self.current_board[x][1] == self.current_board[x][2] and self.current_board[x][2] != '_'):
                return self.current_board[x][2]

        if (((self.current_board[0][0] == self.current_board[1][1] and self.current_board[1][1] == self.current_board[2][2]) or (self.current_board[2][0] == self.current_board[1][1] and self.current_board[1][1] == self.current_board[0][2])) and self.current_board[1][1] != '_'):     # checa se nas diagonais tem casos vencedores
                return self.current_board[1][1]

        for x in [0, 1, 2]:
            for y in [0, 1, 2]:
                if self.current_board[x][y] == '_':
                    return None     # Se ainda há espaços em branco continua
        return 'VELHA'              # Se não continua e não há vitórias, então temos VELHA ou TIE

    def max_value(self):
        maxValue = -2
        x = None
        y = None
        outcome = self.win_or_tie()
        if outcome == 'X':      # Se o resultado for X perdemos um ponto para o maximizador
            return (-1, 0, 0)
        if outcome == 'O':      # Se for O ganhamos um ponto
            return(1, 0, 0)
        if outcome == '_':      # Se não há caminhos, não ganhamos ou perdemos
            return(0, 0, 0)
        for a in [0,1,2]:
            for b in [0,1,2]:
                if self.current_board[a][b] == '_':
                    self.current_board[a][b] = 'O'
                    (minValue, minX, minY) = self.min_value()       # chama a função do mínimo valor para buscar o valor para comparar com o maior valor
                    if minValue > maxValue:
                        maxValue = minValue
                        x = a
                        y = b
                    self.current_board[a][b] = '_'
        return (maxValue, x, y)

    def min_value(self):
        minValue = 2
        x = None
        y = None
        outcome = self.win_or_tie()
        if outcome == 'X':
            return (-1, 0, 0)
        if outcome == 'O':
            return(1, 0, 0)
        if outcome == '_':
            return(0, 0, 0)
        for a in [0,1,2]:
            for b in [0,1,2]:
                if self.current_board[a][b] == '_':
                    self.current_board[a][b] = 'X'
                    (maxValue, maxX, maxY) = self.max_value()       # chama a função do maior valor para buscar o valor para comparar com o maior valor
                    if minValue > maxValue:
                        minValue = maxValue
                        x = a
                        y = b
                    self.current_board[a][b] = '_'
        return (minValue, x, y)
    
    def turn(self):
        round = 0
        while 1:
            self.outcome = self.win_or_tie()
            if self.outcome != None:
                if self.outcome != 'VELHA':
                    print(f'{self.outcome} VENCEU!')
                elif self.outcome == "VELHA":
                    print(f'DEU {self.outcome}!')
                
                self.initialize_tictactoe()
                return
            if self.player_turn == 'X':
                print(f'\nRODADA {round}')
                round = 1 + round
                while True:
                    x, y = input("Escreva as coordenadas da posição que quer alocar o X: ").split()
                    if self.is_empty(int(x), int(y)):
                        self.current_board[int(x)][int(y)] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print("Espaço já preenchido!")
            else:
                (minValue, x, y) = self.max_value()
                print(f'É a vez do jogador "O", este que joga as coordenadas {x} {y}')
                self.current_board[x][y] = 'O'
                self.player_turn = 'X'
            self.print_board()



# Neste programa temos somente um jogador humano contra a o algoritmo MINMAX
board = TicTacToe()
print("Lembrando que o formato de entrada do jogo consite em uma coordenada X Y, dois números de 0 a 2 separados por espaço")
print("(0,0)|(0,1)|(0,2)\n(1,0)|(1,1)|(1,2)\n(2,0)|(2,1)|(2,2)")
board.turn()
