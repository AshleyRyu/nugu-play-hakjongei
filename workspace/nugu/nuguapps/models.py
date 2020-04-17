from django.db import models

# Create your models here.

class App(models.Model):
    appname = models.CharField(max_length=30)

class School(models.Model):
    university = models.CharField(max_length=20)
    typical = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    start = models.TextField()
    end = models.TextField()
    term = models.TextField()
    first_result = models.TextField()
    interview_date = models.TextField()
    final_result = models.TextField()
    
    