from django.db import models


# Create your models here.

class Player(models.Model):
    is_host = models.BooleanField()
    name = models.CharField(max_length=30)
    player_number = models.IntegerField()
    question1 = models.BooleanField()
    question2 = models.BooleanField()
    question3 = models.BooleanField()
    question4 = models.BooleanField()
    question5 = models.BooleanField()
    question6 = models.BooleanField()
    question7 = models.BooleanField()
    question8 = models.BooleanField()
    question9 = models.BooleanField()
    question10 = models.BooleanField()
