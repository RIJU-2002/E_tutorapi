from rest_framework import serializers
from .models import Teacher,Students
class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model=Teacher
        fields=['id','name','phone_number','Qualification','subjects','standard','longitude','latitude']



class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Students
        fields=['id','name','phone_number','standard','longitude','latitude']