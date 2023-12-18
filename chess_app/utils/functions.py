import chess
from .config import piece_weights, position_weights

def get_game_state(board):
    """
    Get the current state of the chess game.

    Parameters:
    - board (chess.Board): The chess board representing the current state of the game.

    Returns:
    dict: A dictionary containing information about the game state, including legal moves,
          promotions, current board position in Forsyth-Edwards Notation (FEN),
          game over status, and check status.
    """
    all_legal_moves = [str(move) for move in board.legal_moves]
    legal_moves, promotions = set(), set()

    for move in all_legal_moves:
        if len(move) == 5:
            promotions.add(move[:4])
        legal_moves.add(move[:4])

    game_state = {
        "legal_moves": ",".join(legal_moves),
        "promotions": ",".join(promotions),
        "curr_board": board.fen(),
        "is_game_over": board.is_game_over(),
        "is_check": board.is_check(),
    }

    return game_state


def get_pieces(board, color):
    """
    Get the positions of pieces on the chess board for a specific color.

    Parameters:
    - board (chess.Board): The chess board representing the current state of the game.
    - color (chess.Color): The color for which to get the piece positions.

    Returns:
    list: A list of tuples containing piece type and position for the specified color.
    """
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
    """
    Calculate the overall score for a player in the chess game.

    Parameters:
    - board (chess.Board): The chess board representing the current state of the game.
    - color (chess.Color): The color for which to calculate the score.

    Returns:
    int: The calculated score based on material, piece positions, and check status.
    """
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
    """
    Evaluate the overall position on the chess board for a given player.

    Parameters:
    - board (chess.Board): The chess board representing the current state of the game.
    - color (chess.Color): The color for which to evaluate the position.

    Returns:
    int: The evaluation score for the specified player, taking into account the opponent's position.
    """
    ai_score = calculate_score(board, chess.BLACK)
    player_score = calculate_score(board, chess.WHITE)

    if color == chess.WHITE:
        return player_score - ai_score
    return ai_score - player_score
