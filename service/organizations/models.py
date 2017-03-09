from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField()
    def __str__(self):
        return self.name
