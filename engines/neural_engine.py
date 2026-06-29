import torch

from models.tictactoe_model import TicTacToeModel
from rl_helpers import choose_model_move


class NeuralEngine:
    def __init__(self, model_path="models/tictactoe_rl.pth"):
        self.model = TicTacToeModel()
        self.model.load_state_dict(torch.load(model_path))
        self.model.eval()

    def get_move(self, game):
        return choose_model_move(self.model, game)