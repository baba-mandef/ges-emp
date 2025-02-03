from django.db import models
from core.abstract.models import GesObject
from core.agent.models.agent import Agent
from core.pay.models.element import PayElement


class AgentPayElement(GesObject):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    element = models.ForeignKey(PayElement, on_delete=models.CASCADE)
    amount = models.IntegerField()
    start_at = models.DateField()
    end_at = models.DateField(null=True)