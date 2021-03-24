from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CMSUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.BigIntegerField(validators=[MinValueValidator(
        1000000000), MaxValueValidator(9999999999)], null=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.IntegerField(
        validators=[MinValueValidator(100000), MaxValueValidator(999999)])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'pincode']

    objects = CustomUserManager()

    @property
    def is_admin_user(self):
        return self.is_staff or self.is_superuser

    def __str__(self):
        return self.email
