from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import TeacherSerializer,StudentSerializer
from .models import Teacher,Students
from rest_framework import permissions
from .permissions import IsOwner

# Create your views here.

class TeacherList(ListCreateAPIView):
    serializer_class=TeacherSerializer
    queryset=Teacher.objects.all()
    permission_classes=(permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(username=self.request.user)
    


class TeacherDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=TeacherSerializer
    queryset=Teacher.objects.all()
    permission_classes=(permissions.IsAuthenticated,IsOwner,)
    lookup_field="id"

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(username=self.request.user)
    

class StudentList(ListCreateAPIView):
    serializer_class=StudentSerializer
    queryset=Teacher.objects.all()
    permission_classes=(permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(username=self.request.user)
    


class StudentDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=StudentSerializer
    queryset=Teacher.objects.all()
    permission_classes=(permissions.IsAuthenticated,IsOwner,)
    lookup_field="id"

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(username=self.request.user)
    
