from django.db import models
from django.contrib.auth.models import AbstractUser

class Faculty(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'
class Professor(models.Model):
    professor_name = models.CharField(max_length=32)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=32) #title - писать по какому предмету преподает профессор
    bio = models.TextField()

    def __str__(self):
        return f'{self.professor_name}'

class Student(AbstractUser):
    # user - usr AbstractUser
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    enrollment_date = models.DateField(null=True, blank=True)
    graduation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.username} - {self.faculty}'


class Course(models.Model):
    course_name = models.CharField(max_length=32)
    description = models.TextField()
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor,  on_delete=models.CASCADE)


class Room(models.Model):
    room_number = models.IntegerField(choices=[(i, str(i)) for i in range(1,21)], verbose_name='room')
    building = models.IntegerField(choices=[(i, str(i)) for i in range(1,4)], verbose_name='Этаж')
    capacity = models.IntegerField(default=0)


class Schrdule(models.Model): # Расписание
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    day_of_week_CHOICES = (
        ('Понедельник','Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Чертверг'),
        ('Пятница', 'Пятница'),
        ('Суббота', 'Суббота'),
        ('Воскресенье', 'Воскресенье'),
    )
    day_of_week = models.CharField(max_length=32, choices=day_of_week_CHOICES,)


class Recordofcource(models.Model):# общая оценка
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField() #дата начала
    grade = models.IntegerField(choices=[(i, str(i)) for i in range(1,11)], verbose_name='Оценка', blank=True, null=True)

