from django.db import models
from users.models import User
from datetime import datetime
from django.utils import timezone
import random
import string

def generate_code():
    length = 5
    characters = string.ascii_uppercase + string.digits
    code = ''.join(random.choice(characters) for _ in range(length))
    return code
class Course(models.Model):
    TYPE_CHOICES=[
            ('lecture','lecture')
            ,('section','section')
        ]
    
    DAYS_CHOICES = [
            ('Monday', 'Monday'),
            ('Tuesday', 'Tuesday'),
            ('Wednesday', 'Wednesday'),
            ('Thursday', 'Thursday'),
            ('Friday', 'Friday'),
            ('Saturday', 'Saturday'),
            ('Sunday', 'Sunday'),
        ]
    
    name=models.CharField(max_length=255)
    sessionHour=models.IntegerField(default=2)
    sessionDay=models.CharField(max_length=10,choices=DAYS_CHOICES,default='Sunday')
    type=models.CharField(max_length=10,choices=TYPE_CHOICES,default='lecture')
    code = models.CharField(max_length=5, default=generate_code)
    seessionTime=models.TimeField(default=datetime.now)
    capturingTime=models.IntegerField(default=30)
    sessionPlace=models.CharField(max_length=10,null=True)
    totalNumberOfLectures=models.IntegerField(default=13)
    user=models.ManyToManyField(User,related_name='courses')

    def __str__(self):
        return self.name
    
class Lecture(models.Model):
    name=models.CharField(max_length=255)
    data=models.DateField(default=timezone.now)
    type=models.CharField(max_length=255,null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True,related_name='lecture')
    user=models.ManyToManyField(User,related_name='lecture',blank=True)
    def __str__(self):
        return self.name