from django.db import models
from core.abstract.models import GesObject
from core.child.models.level import Level
from core.agent.models.agent import Agent


class Child(GesObject):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    Agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="childrens")
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    
    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"
    

    
    



