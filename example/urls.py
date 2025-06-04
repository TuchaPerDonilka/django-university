from django.contrib import admin
from django.urls import path, include
from university.views import (
    student_list, performance_report,
    StudentCreateView, StudentUpdateView, StudentDeleteView,
    SubjectListView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView,
    GradeListView, GradeCreateView, GradeUpdateView, GradeDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_list, name='student_list'),
    path('report/', performance_report, name='performance_report'),
    path('student/add/', StudentCreateView.as_view(), name='student_create'),
    path('student/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
    
    # Добавленные пути для предметов
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subject/add/', SubjectCreateView.as_view(), name='subject_create'),
    path('subject/<int:pk>/edit/', SubjectUpdateView.as_view(), name='subject_update'),
    path('subject/<int:pk>/delete/', SubjectDeleteView.as_view(), name='subject_delete'),
    
    # Добавленные пути для оценок
    path('grades/', GradeListView.as_view(), name='grade_list'),
    path('grade/add/', GradeCreateView.as_view(), name='grade_create'),
    path('grade/<int:pk>/edit/', GradeUpdateView.as_view(), name='grade_update'),
    path('grade/<int:pk>/delete/', GradeDeleteView.as_view(), name='grade_delete'),
]