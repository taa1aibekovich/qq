from rest_framework import viewsets, generics, status, permissions
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponseRedirect
from django.urls import reverse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import *

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        return Response({
            'user': {
                'email': user.email,
                'username': user.username,
                'token': str(token.access_token),
            }
        }, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.valdated_dataa
        refresh = RefreshToken.for_user(user)
        response = HttpResponseRedirect(reverse('student_list'))
        response.set_cookie('token', str(refresh.access_token))
        return response


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)




class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['username']
    filterset_class = StudentFilter


class FacultyView(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = FacultyFilter


class ProfessorView(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['professor_name']


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['course_name']
    filterset_class = CourseFilter



class RoomView(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers


class SchrduleView(viewsets.ModelViewSet):
    queryset = Schrdule.objects.all()
    serializer_class = SchrduleSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = SchrduleFilter



class RecordofcourceView(viewsets.ModelViewSet):
    queryset = Recordofcource.objects.all()
    serializer_class = RecordofcourceSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecordofcourceFilter




