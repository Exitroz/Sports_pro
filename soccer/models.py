
from django.db import models
# from fontawesome_5.fields import IconField

class Competition(models.Model):
    league_title = models.CharField(max_length=100)
    country = models.CharField(max_length=50)


class Fixtures(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    team_a = models.CharField(max_length=100)
    team_b = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    is_favoured = models.BooleanField(default=False)



# class Category(models.Model):
#     ...
#     icon = IconField()

