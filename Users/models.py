from django.db import models
from authentication.models import User 

# Create your models here.
class Teacher(models.Model):
    SUBJECT_OPTIONS=[
        ('MATHS','MATHS'),
        ('SCIENCE','SCIENCE'),
        ('HISTORY','HISTORY'),
        ('GEOGRAPHY','GEOGRAPHY'),
        ('BIOLOGY','BIOLOGY'),
        ('PHYSICS','PHYSICS'),
        ('LANGUAGE','LANGUAGE'),
    ]
    STANDARDS=[
        ('KINDERGARDEN','KINDERGARDEN'),
        ('CLASS-1 TO CLASS-5','CLASS-1 TO CLASS-5'),
        ('CLASS-6 TO CLASS-10','CLASS-6 TO CLASS-10'),
        ('CLASS 11-12','CLASS 11-12'),
    ]
    username=models.ForeignKey(to=User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    Qualification=models.CharField(max_length=20,default=None)
    subjects=models.CharField(choices=SUBJECT_OPTIONS,max_length=300)
    standard=models.CharField(choices=STANDARDS,max_length=100)
    longitude=models.FloatField(null=True)
    latitude=models.FloatField(null=True)

class Students(models.Model):
    STANDARDS=[
        ('KINDERGARDEN','KINDERGARDEN'),
        ('CLASS-1 TO CLASS-5','CLASS-1 TO CLASS-5'),
        ('CLASS-6 TO CLASS-10','CLASS-6 TO CLASS-10'),
        ('CLASS 11-12','CLASS 11-12'),
    ]
    username=models.ForeignKey(to=User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    standard=models.CharField(choices=STANDARDS,max_length=100)
    longitude=models.FloatField(null=True)
    latitude=models.FloatField(null=True)