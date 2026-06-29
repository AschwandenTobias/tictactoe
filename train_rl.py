import torch
import torch.optim as optim
import torch.nn.functional as F

import gamelogic as gl

from models.tictactoe_model import TicTacToeModel
from rl_helpers import board_to_input, move_to_index, choose_training_move


def play_self_play_game(model, epsilon):
    """
    Creates a new game and lets the model play both sides.
    Returns the move history and the winner.
    """

    game = gl.Game()
    history = []

    while not gl.somebody_won(game) and not gl.is_game_over(game):
        board_input = board_to_input(game)

        if game.white_turn:
            current_player = 1
        else:
            current_player = 2

        move = choose_training_move(model, game, epsilon)
        move_index = move_to_index(move)

        history.append((board_input, move_index, current_player))

        gl.make_move(game, move)

    if gl.somebody_won(game):
        winner = game.winner
    else:
        winner = 0

    return history, winner


def train_one_game(model, optimizer, epsilon):
    """
    Plays one self-play game and trains the model from the result.
    """

    history, winner = play_self_play_game(model, epsilon)

    total_loss = 0

    for board_input, move_index, player in history:
        if winner == 0:
            reward = 1
        elif winner == player:
            reward = 0.3
        else:
            reward = -3

        x = torch.tensor(board_input, dtype=torch.float32)

        scores = model(x)

        log_probs = F.log_softmax(scores, dim=0)
        move_log_prob = log_probs[move_index]

        loss = -move_log_prob * reward
        total_loss = total_loss + loss

    optimizer.zero_grad()
    total_loss.backward()
    optimizer.step()

    return total_loss.item(), winner


def main():
    """
    Full training loop.
    """

    model = TicTacToeModel()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    number_of_episodes = 25_000

    white_wins = 0
    black_wins = 0
    draws = 0

    for episode in range(number_of_episodes):
        epsilon = max(0.05, 1.0 - episode / 8000)

        loss, winner = train_one_game(model, optimizer, epsilon)

        if winner == 1:
            white_wins += 1
        elif winner == 2:
            black_wins += 1
        else:
            draws += 1

        if episode % 1000 == 0:
            print(f"Episode: {episode}")
            print(f"Epsilon: {epsilon:.2f}")
            print(f"Loss: {loss:.4f}")
            print(f"White wins: {white_wins}")
            print(f"Black wins: {black_wins}")
            print(f"Draws: {draws}")
            print()

            white_wins = 0
            black_wins = 0
            draws = 0

    torch.save(model.state_dict(), "models/tictactoe_rl.pth")
    print("Training finished.")
    print("Model saved to models/tictactoe_rl.pth")


if __name__ == "__main__":
    main()