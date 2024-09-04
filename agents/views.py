from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AgentModelForm
from leads.models import Agent
from django.shortcuts import reverse




class AgentListView(LoginRequiredMixin,generic.ListView):
    template_name="agent_list.html"
    def get_queryset(self):
        
        return Agent.objects.all()
    
class CreateAgentView(LoginRequiredMixin, generic.CreateView):
    template_name="agent_create.html"
    form_class=AgentModelForm
    def get_success_url(self):
        
        return reverse("agents:agent-list")
    def form_valid(self, form):
        agent=form.save(commit=False)
        agent.organization= self.request.user.userprofile
        return super(CreateAgentView, self).form_valid(form)
# Create your views here.
