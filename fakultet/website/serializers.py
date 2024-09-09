from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['username', 'password', 'faculty', 'enrollment_date', 'graduation_date']
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = Student.objects.create_user(**validated_data)
        return user


class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')




class FacultySerializers(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'



class FacultySimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['name']



class StudentSerializers(serializers.ModelSerializer):
    faculty = FacultySimpleSerializers()
    class Meta:
        model = Student
        fields = '__all__'


class StudentSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['username']


class ProfessorSerializers(serializers.ModelSerializer):
    department = FacultySimpleSerializers()
    class Meta:
        model = Professor
        fields = '__all__'


class ProfessorSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['professor_name']



class CourseSerializers(serializers.ModelSerializer):
    department = FacultySimpleSerializers()
    professor = ProfessorSimpleSerializers()
    class Meta:
        model = Course
        fields = ['professor', 'department', 'course_name', 'description']


class CourseSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name']



class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_number']


class SchrduleSerializers(serializers.ModelSerializer):
    course = CourseSimpleSerializers()
    classroom = RoomSimpleSerializers()
    class Meta:
        model = Schrdule
        fields = '__all__'


class RecordofcourceSerializers(serializers.ModelSerializer):
    student = StudentSimpleSerializers()
    course = CourseSimpleSerializers()
    class Meta:
        model = Recordofcource
        fields = ['student', 'course', 'date_enrolled', 'grade']

