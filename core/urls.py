from django.urls import path
from core.agent.views import AgentView, get_grade_info
from django.views.generic.base import RedirectView


urlpatterns = [
    path("", RedirectView.as_view(url="/agents", permanent=True)),  # Redirection permanente
    path('agents', AgentView.as_view(), name='agent_list'),
    path('agents/<str:action>', AgentView.as_view(), name='agent_action'),
    path('agents/<str:action>/<int:pk>', AgentView.as_view(), name='agent_action_pk'),
    path("get-grade-info/", get_grade_info, name="get_grade_info"),

]
