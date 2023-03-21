from django.db import models

class Competition(models.Model):
    league_title = models.CharField(max_length=100)
    country = models.CharField(max_length=50)


class Fixtures(models.Model):
    competiton = models.ForeignKey(Competiton, on_delete=models.CASCADE)
    team_a = models.CharField(max_length=100)
    team_b = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    is_favoured = models.BooleanField(default=False)



class Competition(models.Model):
    league_title = models.CharField(max_length=100)
    country = models.CharField(max_length=50)


class Fixtures(models.Model):
    competiton = models.ForeignKey(Competiton, on_delete=models.CASCADE)
    team_a = models.CharField(max_length=100)
    team_b = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    is_favoured = models.BooleanField(default=False)