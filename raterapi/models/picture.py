# user, game, image_url

from django.db import models

class Picture(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    image_url = models.ImageField(max_length=None, upload_to="games")
