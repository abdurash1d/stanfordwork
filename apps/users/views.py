from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import Group, Permission
from django.http import JsonResponse

from apps.users.models import User, Resume, Student
from apps.users.serializers import (UserSerializer,
                         UserCreateSerializer,
                         GroupSerializer,
                         PermissionSerializer,
                         ResumeSerializer,
                         StudentSerializer)

# class RegisterView(View):
#     def get(self, request):
#         form = UserCreationForm()
#         return render(request, 'users/register.html', {'form': form})

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirect to login after successful registration
#         return render(request, 'users/register.html', {'form': form})

# class LoginView(View):
#     def get(self, request):
#         return JsonResponse({'message': 'Login successful'})

# User Management Views

class UserListView(generics.ListAPIView):
    """
    View to list all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser] 


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a specific user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserCreateView(generics.CreateAPIView):
    """
    View to create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny] 


class GroupViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing groups.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class PermissionListView(generics.ListAPIView):
    """
    View to list all permissions.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAdminUser]


class ResumeListView(generics.ListCreateAPIView):
    """
    View to list all resumes or create a new resume.
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ResumeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a specific resume.
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Resume.objects.filter(user=user)


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    