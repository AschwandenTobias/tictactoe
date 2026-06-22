class Game:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.white_turn = True
        self.move_counter = 0
        self.winner = 0

    def __str__(self):
        string = "   0  1  2\n"
        i = 0
        for row in self.board:
            string += str(i) + " " + str(row) + "\n"
            i += 1

        if self.white_turn:
            string += "Player 1's turn\n"
        else:
            string += "Player 2's turn\n"

        string += f"Movecounter: {self.move_counter}\n"
        return string
    

def move_validity(move, game):
    """
    Checks move validity and parses it
    """
    row, col = move
    if (row < 0 or col < 0) or (row > 2 or col > 2):
        print(f"row or col to big/small")
        return False
    return game.board[row][col] == 0

def make_move(game, move):
    row, col = move
    if game.white_turn:
        game.board[row][col] = 1
    else:
        game.board[row][col] = 2
    return game

def is_game_over(game):
    if all(cell != 0 for row in game.board for cell in row):
        return True
    return False

def somebody_won(game):
    board = game.board
    #print(f"Checking if somebody won")
    for row in board:
        if row[0] == row[1] == row[2] != 0:
            game.winner = row[0]
            #print(f"Row win detected, winner: {game.winner}")
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            game.winner = board[0][col]
            #print(f"Col win detected, winner: {game.winner}")
            return True
    if board[0][0] == board[1][1] == board[2][2] != 0:
        game.winner = board[1][1]
        #print(f"Diag left win detected, winner: {game.winner}")
        return True
    if board[0][2] == board[1][1] == board[2][0] != 0:
        game.winner = board[1][1]
        #print(f"Diag right win detected, winner: {game.winner}")
        return True
    
    return False

def return_valid_moves(game):
    """
    Returns all valid moves
    """
    move_list = []
    for row_index, row in enumerate(game.board):
        for col_index, col in enumerate(row):
            if game.board[row_index][col_index] == 0:
                move_list.append((row_index, col_index))
    return move_list
