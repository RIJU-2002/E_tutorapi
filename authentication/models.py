from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if username is None:
            raise TypeError("User should have an username")
        if email is None:
            raise TypeError("User must have a email")
        
        user=self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,username,email,password=None):
        if password is None:
            raise TypeError("Password cannot be none")
        
        user=self.create_user(username,email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user

class User(AbstractBaseUser,PermissionsMixin):
    STATUS_CHOICES=[
        ('student','STUDENT'),
        ('teacher','TEACHER'),
    ]
    SUBJECTS=[
        ('maths','MATHS'),
        ('science','SCIENCE'),
        ('english','ENGLISH'),
        ('history','HISTORY'),
        ('geography','GEOGRAPHY'),
        ('jee','JEE'),
        ('neet','NEET'),
        ('computerscience','COMPUTER SCIENCE'),
    ]
    username=models.CharField(max_length=100,unique=True,db_index=True)
    email = models.EmailField(max_length=200,unique=True,db_index=True)
    is_verfied=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    objects=UserManager()

    def __str__(self):
        return self.name
    def tokens(self):
        refresh=RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
        