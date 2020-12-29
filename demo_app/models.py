from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=30)
    wins = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    def getPoints(self):
        return self.wins * 3 + self.draws

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE,default=None, null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + self.surname + '-' + str(self.age)

    def getPoints(self):
        return self.goals*5 + self.assists*3