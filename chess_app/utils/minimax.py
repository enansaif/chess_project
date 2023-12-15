import chess
import random

piece_weights = {"p": 100, "n": 280, "b": 320, "r": 479, "q": 929, "k": 2000}
position_weights = {
    # Position point from sunfish
    'p': (   0,   0,   0,   0,   0,   0,   0,   0,
            78,  83,  86,  73, 102,  82,  85,  90,
             7,  29,  21,  44,  40,  31,  44,   7,
           -17,  16,  -2,  15,  14,   0,  15, -13,
           -26,   3,  10,   9,   6,   1,   0, -23,
           -22,   9,   5, -11, -10,  -2,   3, -19,
           -31,   8,  -7, -37, -36, -14,   3, -31,
             0,   0,   0,   0,   0,   0,   0,   0),
    'n': ( -66, -53, -75, -75, -10, -55, -58, -70,
            -3,  -6, 100, -36,   4,  62,  -4, -14,
            10,  67,   1,  74,  73,  27,  62,  -2,
            24,  24,  45,  37,  33,  41,  25,  17,
            -1,   5,  31,  21,  22,  35,   2,   0,
           -18,  10,  13,  22,  18,  15,  11, -14,
           -23, -15,   2,   0,   2,   0, -23, -20,
           -74, -23, -26, -24, -19, -35, -22, -69),
    'b': ( -59, -78, -82, -76, -23,-107, -37, -50,
           -11,  20,  35, -42, -39,  31,   2, -22,
            -9,  39, -32,  41,  52, -10,  28, -14,
            25,  17,  20,  34,  26,  25,  15,  10,
            13,  10,  17,  23,  17,  16,   0,   7,
            14,  25,  24,  15,   8,  25,  20,  15,
            19,  20,  11,   6,   7,   6,  20,  16,
            -7,   2, -15, -12, -14, -15, -10, -10),
    'r': (  35,  29,  33,   4,  37,  33,  56,  50,
            55,  29,  56,  67,  55,  62,  34,  60,
            19,  35,  28,  33,  45,  27,  25,  15,
             0,   5,  16,  13,  18,  -4,  -9,  -6,
           -28, -35, -16, -21, -13, -29, -46, -30,
           -42, -28, -42, -25, -25, -35, -26, -46,
           -53, -38, -31, -26, -29, -43, -44, -53,
           -30, -24, -18,   5,  -2, -18, -31, -32),
    'q': (   6,   1,  -8,-104,  69,  24,  88,  26,
            14,  32,  60, -10,  20,  76,  57,  24,
            -2,  43,  32,  60,  72,  63,  43,   2,
             1, -16,  22,  17,  25,  20, -13,  -6,
           -14, -15,  -2,  -5,  -1, -10, -20, -22,
           -30,  -6, -13, -11, -16, -11, -16, -27,
           -36, -18,   0, -19, -15, -15, -21, -38,
           -39, -30, -31, -13, -31, -36, -34, -42),
    'k': (   4,  54,  47, -99, -99,  60,  83, -62,
           -32,  10,  55,  56,  56,  55,  10,   3,
           -62,  12, -57,  44, -67,  28,  37, -31,
           -55,  50,  11,  -4, -19,  13,   0, -49,
           -55, -43, -52, -28, -51, -47,  -8, -50,
           -47, -42, -43, -79, -64, -32, -29, -32,
            -4,   3, -14, -50, -57, -18,  13,   4,
            17,  30,  -3, -14,   6,  -1,  40,  18),
}

def get_pieces(board, color):
    positions = board.piece_map()
    white_positions = []
    black_positions = []
    for pos, piece in positions.items():
        piece_str = str(piece)
        if piece_str.isupper():
            white_positions.append((piece_str.lower(), 63 - pos))
        else:
            black_positions.append((piece_str, pos))
    if color == chess.WHITE:
        return white_positions
    return black_positions

def calculate_score(board, color):
    board_fen = board.board_fen()
    material_score = 0
    for piece, weight in piece_weights.items():
        if color == chess.WHITE:
            piece = piece.upper()
        material_score += board_fen.count(piece) * weight

    board_pieces = get_pieces(board, color)
    position_score = 0
    for piece, pos in board_pieces:
        position_score += position_weights[piece][pos]
    
    check_score = 0
    if color != board.turn:
        if board.is_check():
            check_score += 200
        if board.is_checkmate():
            check_score += 1500

    return material_score + position_score + check_score

def evaluate(board, color):
    ai_score = calculate_score(board, chess.BLACK)
    player_score = calculate_score(board, chess.WHITE)
    
    if color == chess.WHITE:
        return player_score - ai_score
    return ai_score - player_score

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
