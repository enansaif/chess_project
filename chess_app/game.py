import chess
import random

board = chess.Board()

def play(player1_move:str) -> dict:
   '''Function receives a valid move from player1, ai makes a move 
   and returns a list of next legal moves player can make.'''
   
   board.push(chess.Move.from_uci(player1_move))
   if board.legal_moves:
      board.push(random.choice(list(board.legal_moves)))

   all_legal_moves = [str(move) for move in board.legal_moves]
   legal_moves, promotions = set(), set()

   for move in all_legal_moves:
      if len(move) == 5:
         promotions.add(move[:4])
      legal_moves.add(move[:4])
   
   game_state = {
      'legal_moves': ','.join(legal_moves),
      'promotions': ','.join(promotions),
      'curr_board': board.fen(),
      'is_game_over': board.is_game_over(),
      'is_check': board.is_check(),
   }
   
   return game_state
