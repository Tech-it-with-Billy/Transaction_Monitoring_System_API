from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import RegistrationSerializer, ProfileSerializer

class RegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer

class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user