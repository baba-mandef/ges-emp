from django.db import models
from core.abstract.models import GesObject
from core.agent.models.agent import Agent


class MonthlyPay(GesObject):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    base_amount = models.IntegerField()
    retained_amount = models.IntegerField()
    paied_amount = models.IntegerField()
    dead_month = models.DateField()