from django.shortcuts import render
from django.http import JsonResponse
from . import game
import json
import chess

board = chess.Board()

def home(request):
    legal_moves, promotions = game.get_legal_moves(board)
    context = {
        'legal_moves': legal_moves,
        'promotions': promotions,
        'is_game_over': board.is_game_over(),
        'curr_board': board.fen(),
    }
    
    return render(request, 'chess_app/index.html', context=context)

def play_step(request):
    if request.method == 'POST':
        move = json.loads(request.body).get('move')
        game_state = game.play(move, board)
    return JsonResponse(game_state)
