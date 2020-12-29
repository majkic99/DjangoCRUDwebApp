from django.urls import path
from . import views

app_name = 'demo_app'
urlpatterns = [

    path('', views.index, name='index'),
    path('teams/', views.teams, name='teams'),
    path('teams/<int:id>/', views.team, name='team'),
    path('teams/win/<int:id>/', views.win, name='addwin'),
    path('teams/draw/<int:id>/', views.draw, name='adddraw'),
    path('teams/lose/<int:id>/', views.lose, name='addloss'),
    path('teams/edit/<int:id>/', views.editTeam, name='editteam'),
    path('teams/new/', views.newTeam, name='newteam'),
    path('players/<int:id>/', views.player, name='player'),
    path('player/edit/<int:id>/', views.editPlayer, name='editplayer'),
    path('player/new/', views.newPlayer, name='newplayer')
]
