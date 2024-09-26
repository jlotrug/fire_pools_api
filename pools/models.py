from django.db import models
from django.conf import settings

class League(models.Model):
    league_name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.league_name

class Player(models.Model):
    player_name = models.CharField(max_length=100)
    wins = models.IntegerField(default=0)

class Pool(models.Model):
    week = models.IntegerField(default=0)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    winner = models.ForeignKey(Player, blank=True, null=True, on_delete=models.DO_NOTHING)
    players = models.ManyToManyField(Player , through='GameCard', related_name='players')
    locked = models.BooleanField(default=False)

    def __str__(self):
        return "Week " + self.week
    
class Team(models.Model):
    team_name = models.CharField(max_length=100)
    logo = models.CharField(max_length=100, blank=True, null=True)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    
class Game(models.Model):
    # Made team names can be null so game can be created and then updated
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE)
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE)
    winner = models.ForeignKey(Team, on_delete=models.CASCADE)
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE)

class GameCard(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE)
    wins = models.IntegerField(default=0)
    won = models.BooleanField(default=False)
    monday_score = models.IntegerField(default=0)

class Pick(models.Model):
    choice = models.ForeignKey(Team, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)
    game = models.ForeignKey(Game, on_delete = models.CASCADE)
    gamecard = models.ForeignKey(GameCard, on_delete=models.CASCADE)



# class UserLeague(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     league = models.ForeignKey(League, on_delete=models.CASCADE)

# class PoolUser(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     pool = models.ForeignKey(Pool, on_delete=models.CASCADE)

