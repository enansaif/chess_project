from django.shortcuts import render
# Create your views here.

def home(request):
    html = "<html><body>Hello cruel world</body></html>"
    return render(request, 'chess/index.html')