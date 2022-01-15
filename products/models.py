from django.db import models
from users.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField(default=0.0)
    seller = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='user_products'
    )

    def __str__(self):
        return self.name
    