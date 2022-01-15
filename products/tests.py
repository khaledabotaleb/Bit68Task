import pytest
from rest_framework.test import APIRequestFactory
from products.views import ProductAPIView
from users.models import User
from rest_framework.test import force_authenticate

# Create your tests here.
class ProductTestCases:
    @pytest.mark.django_db
    def test_get_products(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='khaled1')
        view = ProductAPIView.as_view()

        # Make an authenticated request to the view...
        request = factory.get('/api/v1/product/')
        force_authenticate(request, user=user)
        response = view(request)
        assert response.status_code == 200