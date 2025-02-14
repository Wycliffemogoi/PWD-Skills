from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20, unique=True)
    ncpwd_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15)
    county = models.CharField(max_length=50)
    subcounty = models.CharField(max_length=50)
    ward = models.CharField(max_length=50)
    LEVEL_OF_EDUCATION_CHOICES = [
        ('apprentice', 'Apprentice'),
        ('high_school', 'High School'),
        ('diploma', 'Diploma'),
        ('bachelors', 'Bachelors Degree'),
        ('masters', 'Masters Degree'),
        ('phd', 'PhD'),
    ]
    level_of_education = models.CharField(max_length=50, choices=LEVEL_OF_EDUCATION_CHOICES)
    skills = models.TextField()

    def __str__(self):
        return self.name