from django.urls import path

from .views import ProductAPIView

urlpatterns = [ 
    path("product/", ProductAPIView.as_view({"get": "list","post": "create"})),
]
