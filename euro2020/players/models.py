from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    team = models.ForeignKey(
        Team, related_name="players", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
