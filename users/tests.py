from django.test import TestCase
from .models import User
import pytest
# Create your tests here.


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create(username="test", email="test@test.com", first_name="test", last_name="test", password="12345678")
    assert user.email == "test@test.com"



