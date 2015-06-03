from django.shortcuts import render
from projects.models import Project
from django.views.generic import TemplateView

# Create your views here.
class ProjectsView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(ProjectsView, self).get_context_data(**kwargs)
        
        context['projects_list'] = Project.objects.all()
        return context