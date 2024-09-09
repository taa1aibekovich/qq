from django.urls import path
from .views import *

urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('Student/', StudentView.as_view({'get':'list', 'post':'create'}), name='student_list'),
    path('Student<int:pk>/', StudentView.as_view({'get': 'retrieve', 'put': 'update', 'delete':'destroy'}), name='student_detail'),

    path('faculty/', FacultyView.as_view({'get':'list', 'post':'create'}), name='faculty_list'),
    path('faculty/<int:pk>/', FacultyView.as_view({'get': 'retrieve', 'put': 'update', 'delete':'destroy'}), name='faculty_detail'),

    path('professor/', ProfessorView.as_view({'get':'list', 'post':'create'}), name='course_list'),
    path('professor/<int:pk>/', ProfessorView.as_view({'get': 'retrieve', 'put': 'update', 'delete':'destroy'}), name='professor_detail'),

    path('', CourseView.as_view({'get':'list', 'post':'create'}), name='professor_list'),
    path('<int:pk>/', CourseView.as_view({'get': 'retrieve', 'put': 'update', 'delete':'destroy'}), name='course_detail'),

    path('room/', RoomView.as_view({'get':'list', 'post':'create'}), name='room_list'),
    path('room/<int:pk>/', RoomView.as_view({'get': 'retrieve', 'put': 'update', 'delete':'destroy'}), name='room_detail'),


    path('schrdule/', SchrduleView.as_view({'get':'list', 'post':'create'}), name='schrdule_list'),
    path('schrdule/<int:pk>/', SchrduleView.as_view({'get': 'retrieve', 'put': 'update', 'delete':'destroy'}), name='schrdule_detail'),


    path('recordofcource/', RecordofcourceView.as_view({'get':'list', 'post':'create'}), name='recordofcource_list'),
    path('recordofcource/<int:pk>/', RecordofcourceView.as_view({'get': 'retrieve', 'put': 'update', 'delete':'destroy'}), name='recordofcource_detail'),
]