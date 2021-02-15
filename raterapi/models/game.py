# title, description, designer, year_released, number_of_players, estimated_time_to_play, age_recommendation, user
from django.db import models

class Game(models.Model):

    title = models.CharField(max_length=75)
    description = models.CharField(max_length=255)
    designer = models.CharField(max_length=75)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    estimated_time_to_play = models.IntegerField()
    age_recommendation = models.CharField(max_length=25)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    