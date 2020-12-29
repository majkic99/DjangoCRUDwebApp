from django.urls import path
from . import views

app_name = 'demo_app'
urlpatterns = [

    path('', views.index, name='index'),
    path('register/', views.user_register, name='user_register'),
    path('teams/', views.teams, name='teams'),
    path('players/', views.players, name='players'),
    path('teams/<int:id>/', views.team, name='team'),
    path('teams/delete/<int:id>/', views.deleteteam, name='deleteteam'),
    path('teams/win/<int:id>/', views.win, name='addwin'),
    path('teams/draw/<int:id>/', views.draw, name='adddraw'),
    path('teams/lose/<int:id>/', views.lose, name='addloss'),
    path('teams/edit/<int:id>/', views.editTeam, name='editteam'),
    path('teams/new/', views.newTeam, name='newteam'),
    path('players/<int:id>/', views.player, name='player'),
    path('players/delete/<int:id>/', views.deleteplayer, name='deleteplayer'),
    path('player/edit/<int:id>/', views.editPlayer, name='editplayer'),
    path('player/new/', views.newPlayer, name='newplayer'),
    path('players/goal/<int:id>/', views.goal, name='goal'),
    path('players/assist/<int:id>/', views.assist, name='assist'),
    path('players/newteam/' ,views.addtoteam, name='addtoteam'),
    path('changeteams', views.changeteams, name='changeteams')





]
