from django.contrib import admin
from django.urls import path, include
from university.views import student_list, performance_report
from university.views import StudentCreateView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_list, name='student_list'),
    path('report/', performance_report, name='performance_report'),
    path('student/add/', StudentCreateView.as_view(), name='student_create'),
    path('student/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
]