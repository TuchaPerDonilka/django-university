from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    email = models.EmailField(unique=True, verbose_name="Email")
    group = models.CharField(max_length=10, verbose_name="Группа")

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    value = models.IntegerField(verbose_name="Оценка")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.value}"