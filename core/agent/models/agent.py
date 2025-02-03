from django.db import models
from core.abstract.models import GesObject
from core.extras.tools import generate_unique_code


class Agent(GesObject):
    code_mat = models.CharField(max_length=10, default=generate_unique_code, unique=True, db_index=True)
    first_name = models.CharField(max_length=100)
    index = models.IntegerField(null=True)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    base_salary = models.IntegerField(null=True)
    family_aid = models.IntegerField(null=True)
    children = models.IntegerField(null=True)
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.code_mat} | {self.last_name} {self.first_name}"
    
    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"
    
    class Meta:
        verbose_name = "Agent"
        verbose_name_plural = "Agents"
        ordering = ["last_name"]
    
    
    
    




