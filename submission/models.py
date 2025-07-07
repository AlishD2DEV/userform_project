from django.db import models

class UserSubmission(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.full_name
