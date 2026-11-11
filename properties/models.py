from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Property(models.Model):
    class PropertyType(models.TextChoices):
        SINGLE = "SINGLE", "Single room"
        BEDSITTER = "BEDSITTER", "Bedsitter"
        ONE_BEDROOM = "ONE_BEDROOM", "One bedroom"
        TWO_BEDROOM = "TWO_BEDROOM", "Two bedroom"
        HOSTEL = "HOSTEL", "Hostel"
        OTHER = "OTHER", "Other"

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending review"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"
        SUSPENDED = "SUSPENDED", "Suspended"

    landlord = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="properties",

    )
    title = models.CharField(max_length=160)
    description = models.TextField()
    area = models.CharField(max_length=100)
    landmark = models.CharField(max_length=160, blank=True)
    property_type = models.CharField(
        max_length=20,
        choices=PropertyType.choices,
    )
    monthly_rent = models.PositiveIntegerField()
    deposit = models.PositiveIntegerField(default=0)
    bedrooms = models.PositiveSmallIntegerField(default=1)
    available_from = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    admin_note = models.TextField(blank=True)
    submitted_at = models.DateTimeField(default=timezone.now)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

class PropertyImage(models.Model):
        property = models.ForeignKey(
            Property,
            on_delete=models.CASCADE,
            related_name="images",
        )
        image = models.ImageField(upload_to="property_images/")
        uploaded_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"Image for {self.property.title}"

    