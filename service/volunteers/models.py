from django.db import models

class Volunteer(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    email_address = models.EmailField()
    avatar = models.ImageField(upload_to="")
    GENDER_CHOICES = (('FEMALE', 'Female'),('MALE', 'Male'),)
    gender = models.CharField(max_length=2,choices=GENDER_CHOICES)

    def __str__(self):
        return self.name
