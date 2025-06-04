from django.shortcuts import render
from .models import Student, Grade
from django.db.models import Avg

def student_list(request):
    students = Student.objects.all()
    # Добавляем средний балл для каждого студента
    for student in students:
        student.avg_grade = Grade.objects.filter(student=student).aggregate(Avg('value'))['value__avg'] or 0
    return render(request, 'university/students.html', {'students': students})