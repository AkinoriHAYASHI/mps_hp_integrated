from django.shortcuts import render
from django.views.generic import TemplateView
from organizations import models
from organizations.models import Organization
from django.http.response import Http404

# Create your views here.
class OrganizationsView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(OrganizationsView, self).get_context_data(**kwargs)

        context['organizations_list'] = models.Organization.objects.all()

        return context

class DetailView(TemplateView):
    def get_context_data(self, organization_id, **kwargs):
        
        context = super(DetailView, self).get_context_data(**kwargs)
        
        try:
            organization = Organization.objects.get(id=organization_id)
            context['organization'] = organization
        except organization.DoesNotExist:
            raise Http404
            
        return context