from django.forms import ModelForm, Form
import django.forms as f
from .models import Team, Player

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name']

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'surname', 'age']

class EditPlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'surname','age', 'team', 'goals', 'assists']