from django.db import models
from core.abstract.models import GesObject


class Level(GesObject):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    limit = models.IntegerField()

    def __str__(self):
        return self.name
    



