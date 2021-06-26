from django.conf import settings
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile for {self.user.username}'
