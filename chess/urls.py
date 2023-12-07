from django.urls import path
from . import views

app_name = 'chess'
urlpatterns = [
    path('', views.home),
    path('play_step', views.play_step, name='play_step'),
]