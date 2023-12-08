from django.shortcuts import render
from django.http import HttpResponse
from . import game
import json

def home(request):
    return render(request, 'chess_app/index.html')

def play_step(request):
    if request.method == 'POST':
        move = json.loads(request.body).get('move')
        print(move)
    return HttpResponse('next_legal_moves')