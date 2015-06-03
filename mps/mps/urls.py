from django.conf.urls import include, url
from django.contrib import admin
from portal.views import PortalView, GirlsView, OrganizationView, PortalEngView
from projects.views import ProjectsView
import photos.urls
import members.urls
import organizations.urls
from mps import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'mps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^photos/',include(photos.urls,namespace='photos')),
    url(r'^members/', include(members.urls,namespace='members')),
    url(r'^organizations/', include(organizations.urls,namespace='organizations')),
    url(r'^projects/', ProjectsView.as_view(template_name='projects/projects.html'), name='projects'),
    url(r'^organizations/', OrganizationView.as_view(template_name='portal/organizations.html'), name='organizations'),
    url(r'^girls/', GirlsView.as_view(template_name='portal/portal_girls.html'), name='girls'),
    url(r'^english/', PortalEngView.as_view(template_name='portal/portal_eng.html'), name='english'),
    url(r'', PortalView.as_view(template_name='portal/portal.html'), name='portal'),
]
