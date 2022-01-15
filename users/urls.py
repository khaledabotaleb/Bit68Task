from django.urls import path
from .views import (
    LoginAPIView,
    UserRegisterationApiView,
)


urlpatterns = [
    path("auth/login/", LoginAPIView.as_view(), name="custom_login"),
    path("user/register/", UserRegisterationApiView.as_view(), name="register_user")
]