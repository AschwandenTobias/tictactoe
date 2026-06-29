import gamelogic as gl


class PerfectPlayer:

    def get_move(self, game):
        possible_moves = gl.return_valid_moves(game)

        if game.white_turn:
            best_score = float("-inf")
            best_move = None
            for move in possible_moves:
                gl.make_move(game, move)
                score = minimax(game, 0, False)
                gl.undo_move(game, move)
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_move
        else:
            best_score = float("inf")
            best_move = None
            for move in possible_moves:
                gl.make_move(game, move)
                score = minimax(game, 0, True)
                gl.undo_move(game, move)
                if score < best_score:
                    best_score = score
                    best_move = move
            return best_move
    
def minimax(game, depth, isMaximizing):
    if gl.somebody_won(game):
        if game.winner == 1:
            return 10 - depth
        else:
            return depth - 10
    if gl.is_game_over(game):
        return 0
    if isMaximizing:
        bestScore = float("-inf")
        possible_moves = gl.return_valid_moves(game)
        for move in possible_moves:
            game = gl.make_move(game, move)
            score = minimax(game, depth + 1, False)
            game = gl.undo_move(game, move)
            bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = float("inf")
        possible_moves = gl.return_valid_moves(game)
        for move in possible_moves:
            game = gl.make_move(game, move)
            score = minimax(game, depth + 1, True)
            game = gl.undo_move(game, move)
            bestScore = min(score, bestScore)
        return bestScore

