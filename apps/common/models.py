import uuid
from django.db import models

class TimeStampedUUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    #add code
    ROLE_CHOICES = [
        ("creator", "Creator"),
        ("reviewer", "Reviewer"),
    ]
    role = models.CharField(
        verbose_name=("Role"),
        choices=ROLE_CHOICES,
        max_length=255,
        default="creator",
    )

    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]
