from django_filters import FilterSet
from .models import *



class FacultyFilter(FilterSet):
    class Meta:
        model = Faculty
        fields = {
            'name': ['exact']
        }

class StudentFilter(FilterSet):
    class Meta:
        model = Student
        fields = {
            'faculty': ['exact'],
            'enrollment_date': ['gt', 'lt'],
            'graduation_date': ['gt', 'lt']
        }
class CourseFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'course_name': ['exact'],
            'department': ['exact'],
            'professor': ['exact'],
        }

class SchrduleFilter(FilterSet):
    class Meta:
        model = Schrdule
        fields = {
            'course': ['exact'],
            'classroom': ['exact'],
            'day_of_week': ['exact']
        }


class RecordofcourceFilter(FilterSet):
    class Meta:
        model = Recordofcource
        fields = {
            'course': ['exact'],
            'date_enrolled': ['gt', 'lt'],
            'grade': ['exact']
        }