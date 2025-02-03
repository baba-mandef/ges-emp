from django.contrib import admin
from .models import ElementDetails, PayElement, AgentPayElement, MonthlyPay

# Register your models here.

admin.site.register([ElementDetails, AgentPayElement, MonthlyPay, PayElement])
