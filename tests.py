import gamelogic as gl
from engines.random_engine import RandomEngine

NUMBEROFRUNS = 1_000_000
def main():
    run_counter = 0
    white_wins = 0
    black_wins = 0
    draws = 0

    white_player = RandomEngine()
    black_player = RandomEngine()
    while run_counter < NUMBEROFRUNS:
        if run_counter % 10000 == 0:
            print(f"Games played so far: {run_counter}")
        tictactoe = gl.Game()
        winner = play_game(white_player, black_player, tictactoe)
        if winner == 1:
            white_wins += 1
        elif winner == 2:
            black_wins += 1
        else:
            draws += 1
        run_counter += 1
    print(f"Simulation finished")
    print(f"Total runs: {run_counter}")
    print(f"White won: {white_wins}, or {(white_wins / run_counter * 100):.2f}%")
    print(f"Black won: {black_wins}, or {(black_wins / run_counter * 100):.2f}%")
    print(f"Draws: {draws}, or {(draws / run_counter * 100):.2f}%")

def play_game(white_player, black_player, tictactoe):
    while not gl.somebody_won(tictactoe) and not gl.is_game_over(tictactoe):
        if tictactoe.white_turn:
            move = white_player.get_move(tictactoe)
        else:
            move = black_player.get_move(tictactoe)
        tictactoe = gl.make_move(tictactoe, move)
        tictactoe.move_counter += 1
        tictactoe.white_turn = not tictactoe.white_turn
    return tictactoe.winner

if __name__ == "__main__":
    main()