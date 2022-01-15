from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User
from django.utils.translation import gettext_lazy as _


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["user_id"] = str(user.id)
        return token

    def validate(self, attrs):
        username = attrs.get("email")
        try:
            user = User.objects.get(email=username)
            attrs["email"] = user.email
        except User.DoesNotExist:
            pass
        return super().validate(attrs)


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"},write_only=True)
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = User
        fields = ["first_name", "last_name","email", "password", "password2"]
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 8},
        }

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError({"password": _("password must match")})
        if User.objects.get(username=data['email']):
            raise serializers.ValidationError({"unique": _("A user with that email already exists.")})
        return data

    def save(self):
        user = User(
            username=self.validated_data["email"],
            email = self.validated_data['email'],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
        )
        user.set_password(self.validated_data["password"])
        user.save()
        return user




