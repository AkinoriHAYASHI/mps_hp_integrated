from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import default

# Create your models here.
class Member(models.Model):
    first_name = models.CharField('名前（名）', max_length=30)
    last_name = models.CharField('名前（姓）', max_length=30)
    nickname = models.CharField('ニックネーム', max_length=30)
    GENDER_CHOICES = (('female','女'), ('male','男'),)
    current_job = models.CharField('職種', max_length=30)
    previous_job = models.CharField('前職種', max_length=30, null=True, blank=True)
    gender = models.CharField('性別', max_length=12, choices=GENDER_CHOICES, default='female')
    twitter = models.CharField('twitterアカウント', max_length=20, null=True, blank=True)
    facebook = models.CharField('facebookアカウント', max_length=20, null=True, blank=True)
    attendance = models.PositiveIntegerField(default = 0)
    spacialities = models.CharField('得意分野', max_length=255)
    introduction = models.TextField('ひとこと自己紹介')
    reg_time = models.DateTimeField()
    
    user = models.OneToOneField(User)
    
    
    def __str__(self):
        return self.last_name + ' ' + self.first_name
    