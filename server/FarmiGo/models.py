from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Typically hashed

    def __str__(self):
        return self.name


class Farmer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=13)
    aadhar_number = models.CharField(max_length=12, unique=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
