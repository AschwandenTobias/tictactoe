import gamelogic as gl
import torch
import random

def board_to_input(game):
    """
    This takes a game and returns the board as a list with 1, 0, -1. Always takes the current players perspektive.
    """
    board = game.board
    parsed_board = []
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if board[row_index][col_index] == 1:
                if game.white_turn:
                    parsed_board.append(1)
                else:
                    parsed_board.append(-1)
            elif board[row_index][col_index] == 2:
                if game.white_turn:
                    parsed_board.append(-1)
                else:
                    parsed_board.append(1)
            else:
                parsed_board.append(0)
    #print(parsed_board)
    return parsed_board

def move_to_index(move):
    row, col = move
    return row * 3 + col

def index_to_move(move):
    row = move // 3
    col = move % 3
    return (row, col)

def choose_model_move(model, game):
    """
    Converts the board first, then runs the model,
    gets all legal moves, and returns the legal move with the highest score.
    """
    converted_board = board_to_input(game)
    x = torch.tensor(converted_board, dtype=torch.float32)
    with torch.no_grad():
        scores = model(x)

    legal_moves = gl.return_valid_moves(game)

    best_move = legal_moves[0]
    best_index = move_to_index(best_move)
    best_score = scores[best_index].item()

    for move in legal_moves:
        index = move_to_index(move)
        score = scores[index].item()

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def choose_training_move(model, game, epsilon):
    """
    Chooses a random move with probability epsilon.
    Otherwise chooses the model's preferred move.
    """

    legal_moves = gl.return_valid_moves(game)

    if random.random() < epsilon:
        return random.choice(legal_moves)

    return choose_model_move(model, game)
#game = gl.Game()
#game.board = [[0, 1, 1], [2, 1, 0], [1, 0, 2]]
#board_to_input(game)