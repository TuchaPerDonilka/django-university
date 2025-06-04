from django.contrib import admin
from django.urls import path
from university.views import student_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_list, name='student_list'),
]