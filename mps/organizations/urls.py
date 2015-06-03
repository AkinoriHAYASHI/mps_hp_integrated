from django.conf.urls import include, url
from organizations.views import DetailView, OrganizationsView

urlpatterns = [
    url(r'^(?P<organization_id>\d+)/detail/', DetailView.as_view(template_name='organizations/detail.html'), name='detail'),
    url(r'', OrganizationsView.as_view(template_name='organizations/organizations.html'), name='organizations'),
]

