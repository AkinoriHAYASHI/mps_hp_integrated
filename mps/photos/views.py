from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class PhotosView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(PhotosView, self).get_context_data(**kwargs)
        
        return context