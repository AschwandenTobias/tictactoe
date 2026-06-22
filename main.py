import gamelogic as gl

from engines.human_engine import HumanEngine
from engines.random_engine import RandomEngine


def main():
    white_player = RandomEngine()
    black_player = RandomEngine()

    tictactoe = gl.Game()

    while not gl.somebody_won(tictactoe) and not gl.is_game_over(tictactoe):
        print(tictactoe)

        legal_moves = gl.return_valid_moves(tictactoe)
        print(f"Legal moves: {legal_moves}\nTotal legal moves: {len(legal_moves)}")

        if tictactoe.white_turn:
            move = white_player.get_move(tictactoe)
        else:
            move = black_player.get_move(tictactoe)
        print(f"!Move chosen: {move}!")
        tictactoe = gl.make_move(tictactoe, move)
        tictactoe.move_counter += 1
        tictactoe.white_turn = not tictactoe.white_turn

    print("\nGame over!!!")
    if tictactoe.winner == 1:
        print(f"WhitePlayer won!")
    elif tictactoe.winner == 2:
        print("BlackPlayer won!")
    else:
        print("Game was a draw")
    print(f"Final board state:\n{tictactoe}")

if __name__ == "__main__":
    main()