from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import UserSerializer

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class RegisterUserView(generics.ListCreateAPIView):  
    queryset = User.objects.all()  
    serializer_class = UserSerializer  
    permission_classes = [AllowAny]  


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions



class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]

    authentication_classes = [JWTAuthentication]  # Add JWT authentication
    permission_classes = [permissions.IsAuthenticated]  # Require authentication



    def perform_create(self, serializer):
        task = serializer.save()
        send_task_assignment_email.delay(task.assigned_user.email, task.title)
 

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]    
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]