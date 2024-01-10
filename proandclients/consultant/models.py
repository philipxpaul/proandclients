from django.db import models

class Consultant(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    qualification = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    expertise = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    language = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()
    country = models.CharField(max_length=255)
    skills = models.TextField()

    def __str__(self):
        return self.name
