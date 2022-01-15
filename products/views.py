from products.models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from products.serializers import ProductSerializer
# Create your views here.


class ProductAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        return self.queryset.filter(
            seller=self.request.user
            ).order_by('-price')
