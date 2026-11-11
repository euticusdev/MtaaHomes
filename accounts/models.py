# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    class Role(models.TextChoices):
        SEEKER = "SEEKER", "House seeker"
        LANDLORD = "LANDLORD", "Landlord"
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.SEEKER,
    )
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        role_display = next(
            (label for value, label in self.Role.choices if value == self.role),
            self.role,
        )
        return f"{self.username} ({role_display})"