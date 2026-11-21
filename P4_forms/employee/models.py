from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(null=False, blank=False)
    gender = models.CharField(max_length=10)  

    def __str__(self):
        return self.name