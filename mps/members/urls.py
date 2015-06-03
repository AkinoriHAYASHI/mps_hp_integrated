from django.conf.urls import url
from django.contrib.auth.views import login, logout
from members.views import MembersView, RegistrationView, CompleteView, EditView, DetailView

urlpatterns = [
    url(r'^registration/', RegistrationView.as_view(template_name='members/registration.html'), name='registration'),
    url(r'^complete/', CompleteView.as_view(template_name='members/complete.html'), name='complete'), 
    url(r'^login/', login, {'template_name':'members/login.html'}, name="login"),
    url(r'^logout/', logout, {'next_page':'/portal/'}, name="logout"),
    url(r'^(?P<user_id>\d+)/edit/', EditView.as_view(template_name='members/edit.html'), name='edit'),
    url(r'^(?P<user_id>\d+)/detail/', DetailView.as_view(template_name='members/detail.html'), name='detail'),
    url(r'^members/', MembersView.as_view(template_name='members/members.html'), name='members'),
]



