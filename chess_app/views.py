from django.shortcuts import render
from django.http import JsonResponse
from . import game
import json
import chess

board = chess.Board()

def home(request):
    game_state = game.get_game_state(board)
    return render(request, 'chess_app/index.html', context=game_state)

def play_step(request):
    if request.method == 'POST':
        move = json.loads(request.body).get('move')
        game_state = game.play(move, board)
        return JsonResponse(game_state)

def reset_game(request):
    if request.method == 'POST':
        board.reset()
        game_state = game.get_game_state(board)
        return JsonResponse(game_state)
