import chess
from .functions import evaluate

def predict(board, depth, is_ai):
    if depth == 0 or board.is_game_over():
        color = chess.BLACK if is_ai else chess.WHITE
        return None, evaluate(board, color)
    
    eval = -1*float('inf') if is_ai else float('inf')
    best_move = None
    for move in board.legal_moves:
        board.push(move)
        _, curr_eval = predict(board, depth - 1, not is_ai)
        board.pop()
        if is_ai:
            if curr_eval > eval:
                eval = curr_eval
                best_move = move
        else:
            if curr_eval < eval:
                eval = curr_eval
                best_move = move
    return best_move, eval
