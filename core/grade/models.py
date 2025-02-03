from django.db import models
from core.abstract.models import GesObject


class Grade(GesObject):
   code = models.CharField(max_length=20, unique=True, db_index=True)
   name = models.CharField(max_length=50)
   index = models.IntegerField()

   def __str__(self):
      return f"{self.name}-{self.index}"
