from django.db import models
from core.abstract.models import GesObject
from core.grade.models import Grade
from core.agent.models import Agent


class AgentGrade(GesObject):
   agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="grades")
   grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
   start_at = models.DateField(auto_now_add=True)
   end_at = models.DateField(null=True)

