from django.db import models
from core.abstract.models import GesObject
from core.pay.models.generate import MonthlyPay
from core.pay.models.agent import AgentPayElement

class ElementDetails(GesObject):
    monthly_pay = models.ForeignKey(MonthlyPay, on_delete=models.CASCADE)
    pay_element = models.ForeignKey(AgentPayElement, on_delete=models.CASCADE)