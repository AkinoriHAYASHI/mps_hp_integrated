from django.shortcuts import render
from members.models import Member
from django.views.generic import TemplateView
from members.forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.core.exceptions import PermissionDenied
from django.http.response import Http404

class MembersView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(MembersView, self).get_context_data(**kwargs)
        
        context['members_list'] = Member.objects.all()
        return context
    
class RegistrationView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(RegistrationView, self).get_context_data(**kwargs)
        
        context['usercreation_form'] = UserCreationForm()
        context['registration_form'] = RegistrationForm()
        
        return context
        
    
class CompleteView(TemplateView):
    def post(self,request):
        usercreation_form = UserCreationForm(request.POST)
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid() and usercreation_form.is_valid():
    
            user = usercreation_form.save()
            member = registration_form.save(commit = False)
            member.reg_time = timezone.now()
            member.user = user
            member.save()
            
        
            context = {}
            context['member'] = member
            
            return render(request, 'members/complete.html', context)
    
        else:
            context = {}
            context['usercreation_form'] = usercreation_form
            context['registration_form'] = registration_form
            return render(request, 'members/registration.html', context)
        
        
class EditView(TemplateView):
    def get_context_data(self, user_id, **kwargs):        
        context = super(EditView, self).get_context_data(**kwargs)

        if int(user_id) == self.request.user.id:
            member = Member.objects.get(user=user_id)
            context['member'] = member
            registration_form = RegistrationForm(instance=member)
            context['registration_form'] = registration_form
            
            return context
            
        else:
            raise PermissionDenied
        
class DetailView(TemplateView):
    def get_context_data(self, user_id, **kwargs):
        
        context = super(DetailView, self).get_context_data(**kwargs)
        
        try:
            member = Member.objects.get(user=user_id)
            context['member'] = member
        except Member.DoesNotExist:
            raise Http404
            
        return context