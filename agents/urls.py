from django.urls import path
from agents.views import AgentListView, CreateAgentView

app_name="agents"
urlpatterns = [
    path('', AgentListView.as_view(), name="agent-list"),
    path('create/', CreateAgentView.as_view(), name="agent-create")
]
