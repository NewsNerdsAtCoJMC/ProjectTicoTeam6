from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='/media/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False)
    entered = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
