from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from .serializers import (
    MyTokenObtainPairSerializer,
    RegistrationSerializer,
)
# Create your views here.


class LoginAPIView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserRegisterationApiView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()
