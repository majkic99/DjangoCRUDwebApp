from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Team, Player
from .forms import TeamForm, PlayerForm
from .forms import RegisterForm
from django.http import HttpResponse, HttpResponseRedirect


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'FANTAZI LIGA'})
    else:
        return redirect('demo_app:teams')

@permission_required('demo_app.add_player')
def newPlayer(req):
    if req.method == 'POST':
        form = PlayerForm(req.POST)
        print(form)
        if form.is_valid():
            a = Player(name = form.cleaned_data['name'], surname = form.cleaned_data['surname'], age = int(form.cleaned_data['age']))
            a.save()
            return redirect('demo_app:players')
        else:
            return render(req, 'newplayer.html', {'form': form})
    else:
        form = PlayerForm()
        return render(req, 'newplayer.html', {'form': form})

@permission_required('demo_app.edit_player')
def editPlayer(req, id):
    if req.method == 'POST':
        form = PlayerForm(req.POST)


        if form.is_valid():
            a = Player.objects.get(id=id)
            a.name = form.cleaned_data['name']
            a.surname = form.cleaned_data['surname']
            a.age = form.cleaned_data['age']

            a.save()
            return redirect('demo_app:players')
        else:
            return render(req, 'editplayer.html', {'form': form, 'id': id})
    else:
        form = PlayerForm()
        return render(req, 'editplayer.html', {'form': form, 'id': id})

@login_required
def player(req, id):
    tmp = get_object_or_404(Player, id=id)
    return render(req, 'player.html', {'player': tmp})

@permission_required('demo_app.add_team')
def newTeam(req):
    if req.method == 'POST':
        form = TeamForm(req.POST)

        if form.is_valid():
            a = Team(name=form.cleaned_data['name'])
            a.save()
            return redirect('demo_app:teams')
        else:
            return render(req, 'newteam.html', {'form': form})
    else:
        form = TeamForm()
        return render(req, 'newteam.html', {'form': form})

@permission_required('demo_app.edit_team')
def editTeam(req, id):
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
    players = Player.objects.all().filter(team=tmp)
    return render(req, 'team.html', {'team': tmp, 'page_title': tmp.name, 'players': players})

@login_required
def teams(req):
    tmp = Team.objects.all()
    return render(req, 'teams.html', {'teams': tmp})

@permission_required('demo_app.add_result')
def win(req,  id):
    a = Team.objects.get(id=id)
    a.wins = a.wins+1
    a.save()
    return render(req, 'team.html', {'team': a, 'page_title': a.name})

@permission_required('demo_app.add_result')
def draw(req,  id):
    a = Team.objects.get(id=id)
    a.draws = a.draws + 1
    a.save()
    return render(req, 'team.html', {'team': a, 'page_title': a.name})

@permission_required('demo_app.add_result')
def lose(req,  id):
    a = Team.objects.get(id=id)
    a.losses = a.losses + 1
    a.save()
    return render(req, 'team.html', {'team': a, 'page_title': a.name})

@permission_required('demo_app.add_result')
def assist(req,  id):
    a = Player.objects.get(id=id)
    a.assists = a.assists + 1
    a.save()
    return render(req, 'player.html', {'player': a, 'page_title': a.name})

@permission_required('demo_app.add_result')
def goal(req,  id):
    a = Player.objects.get(id=id)
    a.goals = a.goals + 1
    a.save()
    return render(req, 'player.html', {'player': a, 'page_title': a.name})


def players(req):
    tmp = Player.objects.all()
    return render(req, 'players.html', {'players': tmp})


def addtoteam(req):
    teamID = req.GET.get('teamID')
    playerID = req.GET.get('playerID')
    team = get_object_or_404(Team, id=teamID)
    player = get_object_or_404(Player, id=playerID)
    player.team = team
    player.save()
    return render(req, 'player.html', {'player': player})


def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()

                # Login the user
                login(request, user)

                # redirect to accounts page:
                return HttpResponseRedirect('/account')

    # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})

@permission_required('demo_app.delete_player')
def deleteplayer(req,id):
    tmp = get_object_or_404(Player, id=id)
    tmp.delete()
    tmp = Player.objects.all()
    return render(req, 'players.html', {'players': tmp})

@permission_required('demo_app.delete_team')
def deleteteam(req,id):
    tmp = get_object_or_404(Team, id=id)
    tmp.delete()
    tmp = Team.objects.all()
    return render(req, 'teams.html', {'teams': tmp})

@permission_required('demo_app.change_team')
def changeteams(req):
    return render(req, 'changeteams.html')