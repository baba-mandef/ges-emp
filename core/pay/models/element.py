from django.db import models
from core.abstract.models import GesObject


class PayElement(GesObject):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)