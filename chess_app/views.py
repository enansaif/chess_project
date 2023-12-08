from django.shortcuts import render
from django.http import HttpResponse
from . import game

def home(request):
    return render(request, 'chess_app/index.html')

def play_step(request):
    if request.method == 'POST':
        print(request.POST.get('move'))
    return HttpResponse('next_legal_moves')