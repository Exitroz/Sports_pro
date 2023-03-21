from django.db import models

# Create your models here.


class Football(models.Model):
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
    prediction = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.team1} vs {self.team2}'

    # def __unicode__(self):
    #     return 

