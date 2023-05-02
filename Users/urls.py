from django.urls import path
from . import views

urlpatterns = [
    path('teacher/',views.TeacherList.as_view(),name='Teachers'),
    path('teacher/<int:id>',views.TeacherDetailAPIView.as_view(),name='Details'),
    path('students/',views.StudentList.as_view(),name='Students'),
    path('students/<int:id>',views.StudentDetailAPIView.as_view(),name='StuDetails'),
]

