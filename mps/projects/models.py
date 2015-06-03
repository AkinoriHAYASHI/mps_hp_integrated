from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 30)
    members = models.TextField()
    summary = models.TextField()
    start = models.DateTimeField()
    complete = models.DateTimeField()
    learnings = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.title