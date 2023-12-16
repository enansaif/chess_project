import chess
from .utils.minimax import predict
from .utils.functions import get_game_state

def play(player1_move:str, board) -> dict:
   '''Function receives a valid move from player1, ai makes a move 
   and returns a list of next legal moves player can make.'''
   
   board.push(chess.Move.from_uci(player1_move))
   if board.legal_moves:
      copy_board = chess.Board(board.fen())
      move, _ = predict(copy_board, depth=2, is_ai=True)
      board.push(move)

   game_state = get_game_state(board)
   return game_state