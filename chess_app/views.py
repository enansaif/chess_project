from django.shortcuts import render
from django.http import JsonResponse
from . import game
import json

def home(request):
    return render(request, 'chess_app/index.html')

def play_step(request):
    if request.method == 'POST':
        move = json.loads(request.body).get('move')
        curr_board, next_legal_moves = game.ai_next_move(move)
        data = {
            'curr_board': curr_board,
            'legal_moves': next_legal_moves,
        }
    return JsonResponse(data)