from django.shortcuts import render
from django.http import JsonResponse
from .utils import functions
from .utils import minimax
import json
import chess

board = chess.Board()

def home(request):
    game_state = functions.get_game_state(board)
    return render(request, 'chess_app/index.html', context=game_state)

def play_step(request):
    if request.method == 'POST':
        move = json.loads(request.body).get('move')
        game_state = functions.play(move, board)
        return JsonResponse(game_state)

def reset_game(request):
    if request.method == 'POST':
        board.reset()
        game_state = functions.get_game_state(board)
        return JsonResponse(game_state)

def undo_move(request):
    if request.method == 'POST':
        if board.move_stack and board.turn == chess.WHITE:
            board.pop()
        if board.move_stack and board.turn == chess.BLACK:
            board.pop()
        game_state = functions.get_game_state(board)
        return JsonResponse(game_state)
