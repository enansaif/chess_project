from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'chess/index.html')

def play_step(request):
    return HttpResponse('next_legal_moves')