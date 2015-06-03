from django.shortcuts import render
from django.views.generic import TemplateView


class PortalView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(PortalView, self).get_context_data(**kwargs)

        return context

class GirlsView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(GirlsView, self).get_context_data(**kwargs)

        return context
    
class OrganizationView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(OrganizationView, self).get_context_data(**kwargs)

        return context
    
class PortalEngView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(PortalEngView, self).get_context_data(**kwargs)

        return context