from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
import datetime

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'consultee'),
        (2, 'consultant'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    phone_number = models.CharField(max_length=15, unique=True)

    def is_consultee(self):
        return self.user_type == 1

    def is_consultant(self):
        return self.user_type == 2

class OTP(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return datetime.datetime.now() - self.created_at < datetime.timedelta(minutes=5)
