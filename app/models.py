from django.db import models

# Create your models here.
class Employee(models.Model):
    fname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    experiance=models.CharField(max_length=50)
    skills=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    location=models.CharField(max_length=50)

    def __str__(self):
        return self.fname