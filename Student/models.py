from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    student_id = models.CharField(max_length=20, unique=True)
    enrollment_date = models.DateField()
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"