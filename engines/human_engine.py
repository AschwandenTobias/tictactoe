import gamelogic as gl

class HumanEngine:

    def get_move(self, game):
        while True:
            move_str = input(
                "Input your move as follows: rowcol, so 0,1 would put a symbol in row 0, col 1\n"
            )

            move = self.parse_move(move_str)

            if move is None:
                continue

            if gl.move_validity(move, game):
                return move

            print("Square unavailable")

    def parse_move(self, move):
        if len(move) != 2:
            print("Input move too long")
            return None

        if not move.isdigit():
            return None

        return int(move[0]), int(move[1])