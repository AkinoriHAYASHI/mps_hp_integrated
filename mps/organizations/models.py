from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organization(models.Model):
    name = models.CharField('組織名', max_length=30)
    email = models.EmailField('メールアドレス')
    leader = models.ForeignKey(User, related_name='leader')
    sub_leader = models.ForeignKey(User, related_name='sub_leader')
    core_members = models.ManyToManyField(User, related_name='core_members')
    vision = models.TextField('紹介')
    is_division = models.BooleanField(default=True)
    image = models.ImageField(upload_to='organizations/', null=True, blank=True)
    foundation = models.DateTimeField('設立日')

    def __str__(self):
        return self.name