from rest_framework import generics, status, permissions
from .permissions import IsAdmin, IsAnalyst, IsOperator
from .serializers import RegistrationSerializer, LoginSerializer, ProfileSerializer
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {'message': 'Registration successful'},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {'error': 'Server error: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validate_data['user']
            
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    'message': 'Login Successful!',
                    'user': {
                        'id': user.id,
                        'firstname': user.firstname,
                        'lastname': user.lastname,
                        'email': user.email,
                        'phone': user.phone_number,
                        'role': user.role,
                        'created_at': user.created_at,
                        'updated_at': user.updated_at
                    },
                    'tokens': {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token)
                    }
                }, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'error': f'Server error: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
    def get(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_object())
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error': f'Server error: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class AdminView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]