from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class User(AbstractUser):
    username = models.CharField(_("username"), max_length=150, null=True, blank=True)
    email = models.EmailField(
        _("email address"),
        max_length=125,
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )
    address = models.TextField(_("address"), null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        ordering = ["-id"]
        verbose_name = _("User")
        verbose_name_plural = _("User")

