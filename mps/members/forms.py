from django.db import models
from members.models import Member
from django.forms import ModelForm, Textarea
from django import forms
import re
from django.forms.models import ModelChoiceField


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('last_name','first_name','nickname','gender','twitter','facebook','current_job','previous_job','spacialities','introduction')
        exclude = ('user', 'attendance', 'reg_time',)
        error_messages = {
            'last_name':{
                'required':'※必須',
                'max_length':'※30文字まで'
                },                          
            'first_name':{
                'required':'※必須',
                'max_length':'※30文字まで'
                },
            'nickname':{
                'required':'※必須',
                'max_length':'※30文字まで'
                },
            'current_job':{
                'required':'※必須',
                'max_length':'※30文字まで'
                },
            'previous_job':{
                'required':'※必須',
                'max_length':'※30文字まで'
                },
            'twitter':{
                'required':'※必須',
                'max_length':'※20文字まで'
                },
            'facebook':{
                'required':'※必須',
                'max_length':'※20文字まで'
                },
            'spacialities':{
                'required':'※必須',
                'max_length':'※255文字まで'
                },
            'introduction':{
                'required':'※必須',
                'max_length':'※30文字まで'
                }        
            }
        
        widgets = {
            'gender':forms.RadioSelect,
            'introduction':forms.Textarea,            
        }
        
