from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    html = "<html><body>Hello cruel world</body></html>"
    return HttpResponse(html)