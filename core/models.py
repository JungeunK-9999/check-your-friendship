from django.db import models


# Create your models here.

class Player(models.Model):
    is_host = models.BooleanField(default=False)
    name = models.CharField(max_length=30)
    host_number = models.IntegerField(default=0)
    question1 = models.BooleanField(default=False)
    question2 = models.BooleanField(default=False)
    question3 = models.BooleanField(default=False)
    question4 = models.BooleanField(default=False)
    question5 = models.BooleanField(default=False)
    question6 = models.BooleanField(default=False)
    question7 = models.BooleanField(default=False)
    question8 = models.BooleanField(default=False)
    question9 = models.BooleanField(default=False)
    question10 = models.BooleanField(default=False)
    current_question = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.name} {self.is_host} {self.host_number}'
