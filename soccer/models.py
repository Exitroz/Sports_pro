
from django.db import models
from django.contrib.auth.models import User


class FavouriteModel(models.Model):
    Eid = models.IntegerField()
    enabled = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

