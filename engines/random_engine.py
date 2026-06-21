import random
import gamelogic as gl


class RandomEngine:

    def get_move(self, game):
        return random.choice(
            gl.return_valid_moves(game)
        )