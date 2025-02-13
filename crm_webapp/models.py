from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    date_created = models.DateField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Member(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    phone_number=models.IntegerField(null=True)
    joined_date=models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"