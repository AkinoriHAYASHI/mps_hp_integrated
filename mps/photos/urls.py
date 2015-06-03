from django.conf.urls import include, url
from photos.views import PhotosView

urlpatterns = [
    url(r'^slide/',PhotosView.as_view(template_name='photos/photo_slide.html'),name='slide'),
    url(r'',PhotosView.as_view(template_name='photos/photos.html'),name='photos'),
]