from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Team, Player
from .forms import TeamForm, PlayerForm, EditPlayerForm
from django.http import HttpResponse

def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'FANTAZI LIGA'})
    else:
        return redirect('demo_app:teams')

@permission_required('demo_app.add_player')
def newPlayer(req):
    if req.method == 'POST':
        form = PlayerForm(req.POST)

        if form.is_valid():
            a = Player(name = form.cleaned_data['name'], surname = form.cleaned_data['surname'])
            a.save()
            return redirect('demo_app:teams')
        else:
            return render(req, 'newplayer.html', {'form': form})
    else:
        form = PlayerForm()
        return render(req, 'newplayer.html', {'form': form})

@permission_required('demo_app.edit_player')
def editPlayer(req):
    if req.method == 'POST':
        form = EditPlayerForm(req.POST)

        if form.is_valid():
            a = Player.objects.get(id=id)
            a.name = form.cleaned_data['name']
            a.surname = form.cleaned_data['surname']
            a.age = form.cleaned_data['age']
            a.goals = form.cleaned_data['goals']
            a.assists = form.cleaned_data['assists']
            teamID = form.cleaned_data['team']
            a.team = Team.objects.get(id=teamID)

            a.save()
            return redirect('demo_app:teams')
        else:
            return render(req, 'editplayer.html', {'form': form})
    else:
        form = PlayerForm()
        return render(req, 'editplayer.html', {'form': form})

@login_required
def player(req, id):
    tmp = get_object_or_404(Player, id=id)
    return render(req, 'player.html', {'player': tmp, 'page_title': tmp.title})

@permission_required('demo_app.add_team')
def newTeam(req):
    if req.method == 'POST':
        form = TeamForm(req.POST)

        if form.is_valid():
            a = Team(title=form.cleaned_data['name'])
            a.save()
            return redirect('demo_app:teams')
        else:
            return render(req, 'newteam.html', {'form': form})
    else:
        form = TeamForm()
        return render(req, 'newteam.html', {'form': form})

@permission_required('demo_app.edit_team')
def editTeam(req):
    if req.method == 'POST':
        form = TeamForm(req.POST)

        if form.is_valid():
            a = Team.objects.get(id=id)
            a.name = form.cleaned_data['name']
            a.save()
            return redirect('demo_app:teams')
        else:
            return render(req, 'editteam.html', {'form': form, 'id': id})
    else:
        a = Team.objects.get(id=id)
        form = TeamForm(instance=a)
        return render(req, 'editteam.html', {'form': form, 'id': id})

@login_required
def team(req,  id):
    tmp = get_object_or_404(Team, id=id)
    return render(req, 'team.html', {'team': tmp, 'page_title': tmp.title})

@login_required
def teams(req):
    tmp = Team.objects.all()
    return render(req, 'teams.html', {'teams': tmp})

@permission_required('demo_app.add_result')
def win():
    a = Team.objects.get(id=id)
    a.wins = a.wins+1
    a.save
    return HttpResponse(status='201')

@permission_required('demo_app.add_result')
def draw():
    a = Team.objects.get(id=id)
    a.draws = a.draws + 1
    a.save
    return HttpResponse(status='201')

@permission_required('demo_app.add_result')
def lose():
    a = Team.objects.get(id=id)
    a.losses = a.losses + 1
    a.save
    return HttpResponse(status='201')