class Game:
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    white_turn = True
    move_counter = 0
    def __str__(self):
        string = "   0  1  2\n"
        i = 0
        for row in self.board:
            string += str(i) + " " + str(row) + "\n"
            i += 1
        string += f"Player 1's turn: {self.white_turn}\n"
        string += f"Movecounter: {self.move_counter}\n"
        return string
        
def main():
    tictactoe = Game()
    while not is_game_over(tictactoe):
        print(tictactoe)
        move = user_input(tictactoe)
        tictactoe = make_move(tictactoe, move)
        tictactoe.move_counter += 1
        tictactoe.white_turn = not tictactoe.white_turn

def user_input(game):
    """
    Gets a new move from a user, this already checks validity
    """
    while True:
        move_str = input("Input your move as follows: rowcol, so 0, 1 would put a symbol in row 0, col 1\n")
        move = parse_move(move_str) 
        if move is None:
            continue
        if move_validity(move, game):
            return move
        print(f"Square unavailable")
    
def parse_move(move):
    if len(move) != 2:
        print("Input move too long")
        return None
    if not move.isdigit():
        return None
    row = int(move[0])
    col = int(move[1])
    return row, col

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
    """
    TODO: Checks if the game is over yet, and adjusts the games game_over if necessary
    """
    return False

def return_valid_moves(game):
    """
    Returns all valid moves
    """
    return []

if __name__=="__main__":
    main()