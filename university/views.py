from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.db.models import Avg, Count
from .models import Student, Subject, Grade
from .forms import StudentForm, SubjectForm, GradeForm

def student_list(request):
    students = Student.objects.annotate(
        avg_grade=Avg('grade__value'),
        grade_count=Count('grade')
    )
    group_filter = request.GET.get('group')
    if group_filter:
        students = students.filter(group__icontains=group_filter)
    sort_by = request.GET.get('sort', 'name')
    if sort_by in ['name', 'group', 'avg_grade']:
        students = students.order_by(sort_by)
    return render(request, 'university/students.html', {
        'students': students,
        'group_filter': group_filter or ''
    })

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'university/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'university/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'university/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

def performance_report(request):
    students_with_grades = Student.objects.annotate(
        avg_grade=Avg('grade__value'),
        grade_count=Count('grade')
    ).filter(grade_count__gt=0)

    if not students_with_grades.exists():
        return render(request, 'university/no_data.html')

    best_student = students_with_grades.order_by('-avg_grade').first()
    worst_student = students_with_grades.order_by('avg_grade').first()

    subjects_stats = Subject.objects.annotate(
        avg_grade=Avg('grade__value'),
        grade_count=Count('grade')
    ).filter(grade_count__gt=0)

    return render(request, 'university/report.html', {
        'best_student': best_student,
        'worst_student': worst_student,
        'subjects_stats': subjects_stats
    })

# Добавленные классы для предметов
class SubjectListView(ListView):
    model = Subject
    template_name = 'university/subject_list.html'
    context_object_name = 'subjects'

class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'university/subject_form.html'
    success_url = reverse_lazy('subject_list')

class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'university/subject_form.html'
    success_url = reverse_lazy('subject_list')

class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'university/subject_confirm_delete.html'
    success_url = reverse_lazy('subject_list')

# Добавленные классы для оценок
class GradeListView(ListView):
    model = Grade
    template_name = 'university/grade_list.html'
    context_object_name = 'grades'

class GradeCreateView(CreateView):
    model = Grade
    form_class = GradeForm
    template_name = 'university/grade_form.html'
    success_url = reverse_lazy('grade_list')

class GradeUpdateView(UpdateView):
    model = Grade
    form_class = GradeForm
    template_name = 'university/grade_form.html'
    success_url = reverse_lazy('grade_list')

class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'university/grade_confirm_delete.html'
    success_url = reverse_lazy('grade_list')