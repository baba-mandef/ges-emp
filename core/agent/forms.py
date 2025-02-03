from django import forms
from django.views import View
from core.agent.models import Agent
from core.grade.models import Grade

# Formulaire pour Agent
class AgentForm(forms.ModelForm):
    grade = forms.ModelChoiceField(queryset=Grade.objects.all(), required=False)
    start = forms.DateField()
    end = forms.DateField(required=False)
    
    class Meta:
        model = Agent
        fields = ['first_name', 'code_mat', 'last_name', 'birth_date', 'base_salary', 'is_active',  'index']
