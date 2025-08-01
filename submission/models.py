from django.db import models
from django.utils import timezone


class Submission(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)  # ✅ Make sure this is included
    submitted_at = models.DateTimeField(default=timezone.now)
    personal_details = models.TextField(default="")

    def __str__(self):
        return self.full_name
