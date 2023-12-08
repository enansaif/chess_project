import chess
import random

board = chess.Board()

def ai_next_move(player1_move:str) -> list:
    '''Function receives a valid move from player1, ai makes a move 
       and returns a list of next legal moves player can make.'''
    
    board.push(chess.Move.from_uci(player1_move))
    
    ai_move = random.choice(list(board.legal_moves))
    board.push(ai_move)
    
    next_legal_moves = ' '.join([str(move) for move in board.legal_moves])
    return str(ai_move), next_legal_moves
