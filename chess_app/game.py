import chess
import random
from .predictors import minimax
from .utils.functions import get_game_state

def play(player1_move:str, board, predictor) -> dict:
   '''Function receives a valid move from player1, ai makes a move 
   and returns a list of next legal moves player can make.'''
   
   board.push(chess.Move.from_uci(player1_move))
   if board.legal_moves:
      copy_board = chess.Board(board.fen())
      if predictor == 'minimax':
         move, _ = minimax.predict(copy_board, depth=2, is_ai=True)
      else:
         move = random.choice(list(board.legal_moves))
      board.push(move)

   game_state = get_game_state(board)
   return game_state