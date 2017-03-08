from django.db import models

class Volunteer(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    email_address = models.EmailField()
    def __str__(self):
        return self.name
