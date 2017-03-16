from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=225)
    def __str__(self):
        return self.name
